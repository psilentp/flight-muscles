from pylab import *
import transformations as tran
from numpy import *

def make_universe(max_sensory_radius = 2,
                  star_density = 125):
    universe_size = max_sensory_radius*2.1
    num_stars = (universe_size**3)*star_density
    ux = (random.ranf(size = num_stars)-0.5)*universe_size
    uy = (random.ranf(size = num_stars)-0.5)*universe_size
    uz = (random.ranf(size = num_stars)-0.5)*universe_size
    uxyz = vstack((ux,uy,uz))
    distances = linalg.norm(uxyz,axis = 0)
    mask = (distances > max_sensory_radius)
    xyz = uxyz[:,~mask]
    return xyz

def arena_project(xyz,arena_rad = 0.122/2,arena_elevation = 0.128):
    x = xyz[0,:]
    y = xyz[1,:]
    z = xyz[2,:]
    distances = linalg.norm(xyz,axis = 0)
    longitude = arctan2(x,y) + pi
    r = squeeze(linalg.norm([[x],[y]],axis = 0))
    elevation = (z/r)*arena_rad
    mask = (r<arena_rad)| (elevation > (arena_elevation/2)) | (elevation < (arena_elevation/-2))
    return (longitude[~mask],elevation[~mask],distances[~mask])

def digitize_points(longitude,
                    elevation,
                    distance,
                    arena_rad = 0.122/2,
                    arena_elevation = 0.128,
                    display_shape = (96,32)):
    elev_bins = linspace(-0.5*arena_elevation,0.5*arena_elevation,(display_shape[1]+1)*16)
    long_bins = linspace(0,2*pi,(display_shape[0]+1)*16)
    weights = 1/distance**2
    #weights = ones_like(distance)
    img_mtrx = histogramdd([longitude,elevation],bins =(long_bins,elev_bins),weights = weights,normed = False)[0].T
    norm_weight = diff(arctan(elev_bins/arena_rad))
    img_mtrx /= norm_weight[:,newaxis]
    import cv2
    img_mtrx = cv2.pyrDown(img_mtrx)
    img_mtrx = cv2.pyrDown(img_mtrx)
    img_mtrx = cv2.pyrDown(img_mtrx)
    img_mtrx = cv2.pyrDown(img_mtrx,dstsize = display_shape)
    return img_mtrx

def integrate_frame(pts,
                    rotation_vect = np.array([1.0,1.0,0.0]),
                    translation_vect = np.array([0.0,0.0,0.0]),
                    frame_period = 0.1):
    rotational_velocity = linalg.norm(rotation_vect)
    rotational_direction = rotation_vect/rotational_velocity
    dt = frame_period/100.0
    dtheta = rotational_velocity*dt 
    drot = tran.rotation_matrix(dtheta,rotational_direction)
    dtrans = tran.translation_matrix(translation_vect*dt)
    dA = np.dot(dtrans,drot)
    for x in range(int(frame_period/dt)):
        pts_H = vstack([pts,ones(shape(pts)[1])])
        pts = np.dot(dA,pts_H)[:-1,:]
    return pts

def crop_universe(xyzp,max_sensory_radius):
    distances = linalg.norm(xyzp,axis = 0)
    mask = (distances > max_sensory_radius)
    xyzp = xyzp[:,~mask]
    return xyzp
    
def refill_universe(xyzp,star_density,max_sensory_radius,frame_distance):
    xyz = make_universe(star_density = star_density,max_sensory_radius = max_sensory_radius+frame_distance*1.2)
    distances = linalg.norm(xyz,axis = 0)
    mask = (distances > max_sensory_radius)
    xyzp = hstack((xyz[:,mask],xyzp))
    return xyzp
    
def make_translation_pattern(equator_pole,
                             translation_velocity,
                             frame_rate,
                             epoch_duration=2.25,
                             max_sensory_radius = 2,
                             star_density = 50):
    #translate in a direction on the equator.
    from scipy.misc import imresize
    frame_period = 1/frame_rate
    frame_distance = frame_period*translation_velocity
    frames_per_cycle = around(epoch_duration*frame_rate).astype(int)
    ####################
    xyz = make_universe(star_density = star_density,max_sensory_radius = max_sensory_radius+frame_distance)
    ###align the orientation vector with arena coordinates
    unit_vector = np.array([0.,1.,0.])
    zp_offset = (2*pi)/96*4
    orientation_vector = dot(tran.rotation_matrix(equator_pole+zp_offset,[0,0,1])[:3,:3],unit_vector)*translation_velocity
    xyzp = integrate_frame(xyz,
                       rotation_vect = np.array([0.1,0.1,0.1]),
                       translation_vect = orientation_vector,
                       frame_period = 1/frame_rate)
    ###crop to max_sensory_radius
    xyzp = crop_universe(xyzp,max_sensory_radius)
    proj = arena_project(xyzp)
    imgs = digitize_points(*proj,display_shape = display_shape)
    imgs = imgs[:,:,newaxis]
    xyzp = refill_universe(xyzp,star_density,max_sensory_radius,frame_distance)
    #####################
    for i in range(frames_per_cycle):
        xyzp = integrate_frame(xyzp,
                       rotation_vect = np.array([1e-10,1e-10,1e-10]),
                       translation_vect = orientation_vector,
                       frame_period = 1/frame_rate)
        xyzp = crop_universe(xyzp,max_sensory_radius)
        proj = arena_project(xyzp)
        img = digitize_points(*proj,display_shape = display_shape)
        imgs = concatenate((imgs, img[:,:,newaxis]),axis = 2)
        xyzp = refill_universe(xyzp,star_density,max_sensory_radius,frame_distance)
    from scipy import io
    return imgs
    #io.savemat('equator_%03d'%(around(rad2deg(equator_pole))),{'imgs':imgs})

def make_translation_pattern_coromeridian(coromeridian_pole,
                                          translation_velocity,
                                          frame_rate,
                                          epoch_duration=2.25,
                                          max_sensory_radius = 2,
                                          star_density = 50):
    #translate in a direction on the equator.
    from scipy.misc import imresize
    frame_period = 1/frame_rate
    frame_distance = frame_period*translation_velocity
    frames_per_cycle = around(epoch_duration*frame_rate).astype(int)
    ####################
    xyz = make_universe(star_density = star_density,max_sensory_radius = max_sensory_radius+frame_distance)
    ###align the orientation vector with arena coordinates
    
    unit_vector = np.array([0.,1.,0.])
    zp_offset = (2*pi)/96*4
    orientation_vector = dot(tran.rotation_matrix(coromeridian_pole,array([1,0,0]))[:3,:3],unit_vector)
    orientation_vector = dot(tran.rotation_matrix(zp_offset,array([0,0,1]))[:3,:3],orientation_vector)*translation_velocity
    
    xyzp = integrate_frame(xyz,
                       rotation_vect = np.array([0.1,0.1,0.1]),
                       translation_vect = orientation_vector,
                       frame_period = 1/frame_rate)
    ###crop to max_sensory_radius
    xyzp = crop_universe(xyzp,max_sensory_radius)
    proj = arena_project(xyzp)
    imgs = digitize_points(*proj,display_shape = display_shape)
    imgs = imgs[:,:,newaxis]
    xyzp = refill_universe(xyzp,star_density,max_sensory_radius,frame_distance)
    #####################
    for i in range(frames_per_cycle):
        xyzp = integrate_frame(xyzp,
                       rotation_vect = np.array([1e-10,1e-10,1e-10]),
                       translation_vect = orientation_vector,
                       frame_period = 1/frame_rate)
        xyzp = crop_universe(xyzp,max_sensory_radius)
        proj = arena_project(xyzp)
        img = digitize_points(*proj,display_shape = display_shape)
        imgs = concatenate((imgs, img[:,:,newaxis]),axis = 2)
        xyzp = refill_universe(xyzp,star_density,max_sensory_radius,frame_distance)
    from scipy import io
    return imgs
    #io.savemat('equator_%03d'%(around(rad2deg(equator_pole))),{'imgs':imgs})
    
    
def make_spin_pattern_equator(equator_pole,
                              angular_velocity,
                              frame_rate,
                              max_sensory_radius = 2,
                              star_density = 50):
    #Spin the world around a equatorial pole
    from scipy.misc import imresize
    unit_vector = np.array([0.,1.,0.])
    zp_offset = (2*pi)/96*4
    orientation_vector = dot(tran.rotation_matrix(equator_pole+zp_offset,[0,0,1])[:3,:3],unit_vector)*angular_velocity
    xyz = make_universe(star_density = star_density,max_sensory_radius = max_sensory_radius)
    xyzp = integrate_frame(xyz,
                       rotation_vect = orientation_vector,
                       translation_vect = np.array([0,0,0]),
                       frame_period = 1/frame_rate)
    proj = arena_project(xyzp)
    imgs = digitize_points(*proj,display_shape = display_shape)
    imgs = imgs[:,:,newaxis]
    frames_per_cycle = int(((2*pi)/angular_velocity)*frame_rate)
    for i in range(frames_per_cycle):
        xyzp = integrate_frame(xyzp,
                           rotation_vect = orientation_vector,
                           translation_vect = np.array([0,0,0]),
                           frame_period = 1/frame_rate)
        proj = arena_project(xyzp)
        img = digitize_points(*proj,display_shape = display_shape)
        imgs = concatenate((imgs, img[:,:,newaxis]),axis = 2)
    from scipy import io
    return imgs

def make_spin_pattern_coromeridian(coromeridian_pole,
                                   angular_velocity,
                                   frame_rate,
                                   max_sensory_radius = 2,
                                   star_density = 50):
    #Spin the world around a pole around a coronal maridian pole
    from scipy.misc import imresize
    unit_vector = np.array([0.,1.,0.])
    zp_offset = (2*pi)/96*4
    orientation_vector = dot(tran.rotation_matrix(coromeridian_pole,array([1,0,0]))[:3,:3],unit_vector)
    orientation_vector = dot(tran.rotation_matrix(zp_offset,array([0,0,1]))[:3,:3],orientation_vector)*angular_velocity
    xyz = make_universe(star_density = star_density,max_sensory_radius = max_sensory_radius)
    xyzp = integrate_frame(xyz,
                       rotation_vect = orientation_vector,
                       translation_vect = np.array([0,0,0]),
                       frame_period = 1/frame_rate)
    proj = arena_project(xyzp)
    imgs = digitize_points(*proj,display_shape = display_shape)
    imgs = imgs[:,:,newaxis]
    frames_per_cycle = int(((2*pi)/angular_velocity)*frame_rate)
    for i in range(frames_per_cycle):
        xyzp = integrate_frame(xyzp,
                           rotation_vect = orientation_vector,
                           translation_vect = np.array([0,0,0]),
                           frame_period = 1/frame_rate)
        proj = arena_project(xyzp)
        img = digitize_points(*proj,display_shape = display_shape)
        imgs = concatenate((imgs, img[:,:,newaxis]),axis = 2)
    from scipy import io
    return imgs
    
def make_spin_pattern_sagimeridian(sagimeridian_pole,angular_velocity,frame_rate):
    #spin the world around a pole on the mid-sagital meridian.
    from scipy.misc import imresize
    unit_vector = np.array([1.,0.,0.])
    zp_offset = (2*pi)/96*4
    orientation_vector = dot(tran.rotation_matrix(sagimeridian_pole,array([0,1,0]))[:3,:3],unit_vector)
    orientation_vector = dot(tran.rotation_matrix(zp_offset,array([0,0,1]))[:3,:3],orientation_vector)*angular_velocity
    xyzp = integrate_frame(xyz,
                       rotation_vect = orientation_vector,
                       translation_vect = np.array([0,0,0]),
                       frame_period = 1/frame_rate)
    proj = arena_project(xyzp)
    imgs = digitize_points(*proj,display_shape = display_shape)
    imgs = imgs[:,:,newaxis]
    frames_per_cycle = int(((2*pi)/angular_velocity)*frame_rate)
    for i in range(frames_per_cycle):
        xyzp = integrate_frame(xyzp,
                           rotation_vect = orientation_vector,
                           translation_vect = np.array([0,0,0]),
                           frame_period = 1/frame_rate)
        proj = arena_project(xyzp)
        img = digitize_points(*proj,display_shape = display_shape)
        imgs = concatenate((imgs, img[:,:,newaxis]),axis = 2)
    from scipy import io
    io.savemat('sagimeridian_%03d'%(around(rad2deg(sagimeridian_pole))),{'imgs':imgs})

def adjust_depth(imgs,bit_depth=3):
    maxbit = (2**bit_depth)-1
    scaling = (maxbit*0.5)/mean(imgs.flatten())
    imgs *= scaling
    imgs = around(imgs)
    imgs[imgs>maxbit] = maxbit
    return(imgs)

def play_pattern(imgs):
    img = imshow(imgs[:,:,0],cmap = cm.gray,vmin=0,vmax = 7)
    import time
    for i in range(shape(imgs)[-1]):
        time.sleep(0.001)
        img.set_data(imgs[:,:,i])
        draw()