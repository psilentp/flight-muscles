import numpy as np
import pyopencl as cl
import time

def opencl_warp(movie,A,output_shape = (1024,1024)):
    #tick = time.clock()
    n_fr = np.shape(movie)[0]
    y_pix = np.shape(movie)[1]
    x_pix = np.shape(movie)[2]

    x_out = output_shape[0]
    y_out = output_shape[1]
    
    A_p = np.linalg.inv(A).astype(np.float32)
    dest_coords_img = np.dstack(np.meshgrid(range(x_out),range(y_out))).astype(np.float32)
    dest_coords_vec = dest_coords_img.reshape(-1,2)
    dest_coords_vec = np.hstack((dest_coords_vec,np.ones(x_out*y_out)[:,np.newaxis]))
    
    src_coords_vec = np.dot(A_p,dest_coords_vec.T).T
    src_coords_vec = src_coords_vec[:,:2].copy()
    src_coords_img = src_coords_vec.reshape(x_out,y_out,2)
    
    C11 = (src_coords_vec[:,0].astype(int)+1-src_coords_vec[:,0]) * (src_coords_vec[:,1].astype(int)+1-src_coords_vec[:,1])
    C12 = (src_coords_vec[:,0].astype(int)+1-src_coords_vec[:,0]) * (src_coords_vec[:,1] - src_coords_vec[:,1].astype(int))
    C21 = (src_coords_vec[:,0] - src_coords_vec[:,0].astype(int)) * (src_coords_vec[:,1].astype(int)+1 - src_coords_vec[:,1])
    C22 = (src_coords_vec[:,0] - src_coords_vec[:,0].astype(int)) * (src_coords_vec[:,1] - src_coords_vec[:,1].astype(int))
    src_coef = np.vstack((C11,C12,C21,C22)).T
    platform = cl.get_platforms()[0]
    devices = platform.get_devices()
    
    gpu = devices[1]
    cpu = devices[0]
    
    ctx = cl.Context(devices=devices)
    queue1 = cl.CommandQueue(ctx,devices[1])

    mf = cl.mem_flags    
    #get gpu and cpu buffer size
    gpu_num_frames = gpu.global_mem_size/(4*4*x_out*y_out)
    cpu_num_frames = cpu.global_mem_size/(2*4*x_out*y_out)
    print gpu_num_frames
    img_g =  cl.Buffer(ctx, mf.READ_ONLY , size = 4*gpu_num_frames*x_pix*y_pix)# hostbuf=movie.astype(int32).copy())
    src_coords_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=src_coords_vec.astype(np.float32).copy())
    src_coef_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=src_coef.astype(np.float32).copy())

    print x_pix
    prg = cl.Program(ctx, """
    __kernel void custom_interp(__global int *img_g,
                                __global float2* src_coords_g,
                                __global float4* src_coef_g,
                                __global int* out_img_g) {
        int3 pos = (int3)(get_global_id(0), get_global_id(1),get_global_id(2));
        int3 size = (int3)(get_global_size(0), get_global_size(1), get_global_size(2));

        int src_size_x = %s;
        int src_size_y = %s;
        int src_y =  src_coords_g[pos.y*size.z + pos.z].x;
        int src_z = src_coords_g[pos.y*size.z + pos.z].y;
        
        int framepos = pos.x*size.y*size.z;
        int framepos_in = pos.x*src_size_y*src_size_x;
        //int src_row = src_y*size.y;
        int src_row = src_y*src_size_x;
        int rowpos = pos.y*size.z;
        
        float4 Q,C;
        if ((src_y >= 0) & (src_z >= 0) & (src_y < src_size_y-1) & (src_z < src_size_x-1))
        {
          Q.x = img_g[framepos_in + src_row + (src_z)];
          Q.y = img_g[framepos_in + src_row + (src_z)+1];
          Q.z = img_g[framepos_in + (src_y+1)*src_size_x + (src_z)];
          Q.w = img_g[framepos_in + (src_y+1)*src_size_x + (src_z)+1];
          
          C.x = src_coef_g[rowpos+pos.z].x;
          C.y = src_coef_g[rowpos+pos.z].y;
          C.z = src_coef_g[rowpos+pos.z].z;
          C.w = src_coef_g[rowpos+pos.z].w;
          out_img_g[framepos + rowpos + pos.z] = dot(C,Q);
        }
        else{
          out_img_g[framepos + rowpos + pos.z] = 0;
        }
    }"""%(x_pix,y_pix)).build()

    out_img_np = np.zeros(shape = (n_fr,x_out,y_out),dtype = np.int32)
    out_img_g = cl.Buffer(ctx, mf.WRITE_ONLY, 4*gpu_num_frames*x_out*y_out)
    
    for i in range(n_fr/gpu_num_frames):
        #print i
        cl.enqueue_copy(queue1, img_g, movie[gpu_num_frames*i:gpu_num_frames*(i+1)].astype(np.int32).copy())
        prg.custom_interp(queue1, (gpu_num_frames,x_out,y_out), None,img_g, src_coords_g, src_coef_g, out_img_g)
        cl.enqueue_copy(queue1, out_img_np[gpu_num_frames*i:gpu_num_frames*(i+1)], out_img_g)
    
    #finish up
    residual = np.mod(n_fr,gpu_num_frames)
    l_frame = n_fr-residual
    cl.enqueue_copy(queue1, img_g, movie[-1*residual:].astype(np.int32).copy())
    prg.custom_interp(queue1, (residual,x_out,y_out), None,img_g, src_coords_g, src_coef_g, out_img_g)
    cl.enqueue_copy(queue1, out_img_np[-1*residual:], out_img_g)
    #tock = time.clock()
    #return src_coords_vec
    return out_img_np