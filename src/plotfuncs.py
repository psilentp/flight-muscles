# -*- coding: utf-8 -*-

from pylab import *
import numpy as np

def kill_spines():
    ax = gca()
    if 'polar' in gca().spines.keys():
        ax.spines['polar'].set_visible(False)
        ax.yaxis.grid(False)
        ax.xaxis.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
    else:
        ax.spines['left'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        [x.set_visible(False) for x in ax.get_xticklabels()]
        [y.set_visible(False) for y in ax.get_yticklabels()]
        [x.set_visible(False) for x in ax.get_xticklines()]
        [y.set_visible(False) for y in ax.get_yticklines()]

### Test settings for plot data matrix function
cols = 12
rows = 2

ybounds = [(-3,3) for j in range(rows)]  
xbounds = [(0,4) for i in range(cols)]

ytick_numbers = [3 for j in range(rows)]
xtick_numbers = [5 for j in range(cols)]

figsize = (10,5)

col_epochs = None
row_epochs = None

col_labels_bottom = ['col\nlbl\n' + str(i) for i in range(cols)]
row_labels_left = ['row\nlbl\n' + str(j) for j in range(rows)]

col_labels_top = ['col\nlbl\n' + str(i) for i in range(cols)]
row_labels_right = ['row\nlbl\n' + str(j) for j in range(rows)]

show_spines_left = False
show_spines_right = [True for j in range(rows)]

show_spines_top = False
show_spines_bottom = [False for j in range(cols)]
show_spines_bottom[-1] = True
plot_panel_function = lambda row,col: (row,col)

def pull_ax_spines(xtick_numbers = 5,ytick_numbers = 5,left = True,bottom=True):
    xbound = gca().get_xbound()
    ybound = gca().get_ybound()
    kill_spines()
    if left:
        gca().spines['left'].set_visible(True)
        gca().spines['left'].set_position(('outward',10))
        [y.set_visible(False) for y in gca().get_yticklines()[1::2]]
        yticks(np.linspace(ybound[0],ybound[1],ytick_numbers))
    if bottom:
        gca().spines['bottom'].set_visible(True)
        gca().spines['bottom'].set_position(('outward',10))
        [y.set_visible(False) for y in gca().get_xticklines()[1::2]]
        xticks(np.linspace(xbound[0],xbound[1],xtick_numbers))
    #yticks(np.linspace(ybound[0],ybound[1],yticknum))
    
def plot_data_matrix(cols = cols,
                     rows = rows,
                     
                     row_label_pos = 'left',
                     col_label_pos = 'bottom',
                     
                     row_spine_pos = 'left',
                     col_spine_pos = 'bottom',
                     
                     figsize = figsize,
                     ybounds = ybounds,
                     xbounds = xbounds,
                     
                     xtick_numbers = 3,
                     ytick_numbers = 3,
                     
                     col_epochs = col_epochs,
                     row_epochs = row_epochs,
                     
                     col_epochs_kwargs = {'alpha':0.2,'color':'b','lw':None},
                     row_epochs_kwargs = {'alpha':0.2,'color':'b','lw':None},
                     
                     col_labels_bottom = 'no_lbl',
                     row_labels_left = 'no_lbl',
                     
                     col_labels_top = 'no_lbl',
                     row_labels_right = None,
                     col_axvlines = None,
                     col_axvlines_kwargs = {'color':'k','ls':'--'},
                     gs_left = 0.05,
                     gs_right = 0.95,
                     gs_wspace = 0.1,
                     gs_hspace = 0.5,
                     plot_panel_function = plot_panel_function,
                     show_spines_left = True,
                     show_spines_right = True,
                     show_spines_top = True,
                     show_spines_bottom = True):
    
    if not(type(col_axvlines) == list):
        col_axvlines = [col_axvlines for j in range(cols)]
    if not(type(col_axvlines_kwargs) == list):
        col_axvlines_kwargs = [col_axvlines_kwargs for j in range(cols)]
        
    if not(type(ytick_numbers) == list):
        ytick_numbers = [ytick_numbers for j in range(rows)]
    
    if not(type(xtick_numbers) == list):
        xtick_numbers = [xtick_numbers for j in range(cols)]
    
    if not(type(xbounds) == list):
        xbounds = [xbounds for j in range(cols)]
        
    if not(type(ybounds) == list):
        ybounds = [ybounds for i in range(rows)]
        
    if not(type(row_labels_left) == list):
        row_labels_left = [row_labels_left for j in range(rows)]
        
    if not(type(row_labels_right) == list):
        row_labels_right = [row_labels_right for j in range(rows)]
        
    if not(type(col_labels_top) == list):
        col_labels_top = [col_labels_top for i in range(cols)]
    
    if not(type(col_labels_bottom) == list):
        col_labels_bottom = [col_labels_bottom for i in range(cols)]
        
    if not(type(row_epochs) == list):
        row_epochs = [row_epochs for j in range(rows)]
        
    if not(type(col_epochs) == list):
        col_epochs = [col_epochs for i in range(cols)]
        
    if type(col_epochs_kwargs) == dict:
        col_epochs_kwargs = [col_epochs_kwargs for i in range(cols)]
    
    if type(row_epochs_kwargs) == dict:
        row_epochs_kwargs = [row_epochs_kwargs for j in range(rows)]
    
    if show_spines_left is True:
        show_spines_left = [True for j in range(rows)]
    elif show_spines_left is False:
        show_spines_left = [False for j in range(rows)]
    
    if show_spines_right is True:
        show_spines_right = [True for j in range(rows)]
    elif show_spines_right is False:
        show_spines_right = [False for j in range(rows)]
        
    if show_spines_top is True:
        show_spines_top = [True for j in range(cols)]
    elif show_spines_top is False:
        show_spines_top = [False for j in range(cols)]
        
    if show_spines_bottom is True:
        show_spines_bottom = [True for j in range(cols)]
    elif show_spines_bottom is False:
        show_spines_bottom = [False for j in range(cols)]

    fig = figure(figsize = figsize)                     
    from matplotlib import gridspec
    # set up the GridSpec
    gs = gridspec.GridSpec(rows,cols)
    
    col_epoch_panels = [fig.add_subplot(gs[:,i]) for i in range(cols)]
    row_epoch_panels = [fig.add_subplot(gs[j,:]) for j in range(rows)]
    
    [col_pan.patch.set_alpha(0.0) for col_pan in col_epoch_panels]
    [row_pan.patch.set_alpha(0.0) for row_pan in row_epoch_panels]
                     
    ax_grid = [[fig.add_subplot(gs[j,i],sharex = col_epoch_panels[i],
                                        sharey = row_epoch_panels[j]) for i in range(cols)] for j in range(rows)]
    
    for j in range(rows):
        for i in range(cols):
            sca(ax_grid[j][i])
            gca().patch.set_alpha(0.0)
            plot_panel_function(i,j)
            
    for panel,row_epoch,row_epochs_kwarg in zip(row_epoch_panels,row_epochs,row_epochs_kwargs):
        sca(panel)
        if row_epoch:
            axhspan(*row_epoch,**row_epochs_kwarg)
        kill_spines()

    for panel,col_epoch,col_epochs_kwarg,col_axvline,col_axvlines_kwarg in zip(col_epoch_panels,
                                                            col_epochs,
                                                            col_epochs_kwargs,
                                                            col_axvlines,
                                                            col_axvlines_kwargs):
        sca(panel)
        if col_epoch:
            axvspan(*col_epoch,**col_epochs_kwarg)
        if not(col_axvline is None):
            axvline(col_axvline,**col_axvlines_kwarg)
        kill_spines()
    
    #set row spines
    for row,ybound,yticknum,show_spine in zip(ax_grid,ybounds,ytick_numbers,show_spines_left):
        for panel in row:
            sca(panel)
            kill_spines()
        sca(row[0])
        gca().set_ybound(*ybound)
        if show_spine:
            gca().spines['left'].set_visible(True)
            gca().spines['left'].set_position(('outward',10))
            yticks(np.linspace(ybound[0],ybound[1],yticknum))
            [y.set_visible(False) for y in gca().get_yticklines()[1::2]]
            
    for row,ybound,yticknum,show_spine in zip(ax_grid,ybounds,ytick_numbers,show_spines_right):
        #gca().set_ybound(*ybound)
        if show_spine:
            sca(row[-1])
            row[-1] = [row[-1],twinx()]
            sca(row[-1][1])
            gca().set_ybound(*ybound)
            kill_spines()
            gca().spines['right'].set_visible(True)
            gca().spines['right'].set_position(('outward',10))
            plt.tick_params(axis='y', which='both', labelleft='off', labelright='on')
            yticks(np.linspace(ybound[0],ybound[1],yticknum))
            [y.set_visible(False) for y in gca().get_yticklines()[::2]]
    
    #set row labels
    for row,row_label in zip(ax_grid,row_labels_left):
        if row_label:
            sca(row[0])
            gca().set_ylabel(row_label)
            
    for row,row_label in zip(ax_grid,row_labels_right):
        if row_label:
            if type(row[-1]) == list:
                sca(row[-1][1])
                gca().yaxis.set_label_position("right")
                gca().set_ylabel(row_label,rotation = -90,va = 'bottom')
            else:
                sca(row[-1])
                gca().yaxis.set_label_position("right")
                gca().set_ylabel(row_label,rotation = -90,va = 'bottom')
                #sca(row[-1])
            #
            #
    
    #set col spines
    for panel,xbound,xticknum,show_spine in zip(ax_grid[-1],xbounds,xtick_numbers,show_spines_bottom):
        if type(panel) == list:
            panel = panel[0]
        sca(panel)    
        gca().set_xbound(*xbound)
        if show_spine:
            gca().spines['bottom'].set_visible(True)
            gca().spines['bottom'].set_position(('outward',10))
            xticks(np.linspace(xbound[0],xbound[1],xticknum))
            [x.set_visible(False) for x in gca().get_xticklines()[1::2]]
            
    for panel,xbound,xticknum,show_spine in zip(ax_grid[0],xbounds,xtick_numbers,show_spines_top):
        if type(panel) == list:
            panel = panel[0]
        sca(panel)
        gca().set_xbound(*xbound)
        if show_spine:
            gca().spines['top'].set_visible(True)
            gca().spines['top'].set_position(('outward',10))
            xticks(np.linspace(xbound[0],xbound[1],xticknum))
            [x.set_visible(False) for x in gca().get_xticklines()[::2]]
        
    for panel,col_label in zip(ax_grid[-1],col_labels_bottom):
        if type(panel) == list:
            panel = panel[0]
        if col_label:
            sca(panel)
            gca().set_xlabel(col_label)
    for panel,col_label in zip(ax_grid[0],col_labels_top):
        if type(panel) == list:
            panel = panel[0]
        if col_label:
            sca(panel)
            gca().set_title(col_label)
        
    #gs.update(left=gs_left, right=gs_right, wspace=gs_wspace,hspace = gs_hspace)
    gs.tight_layout(fig,h_pad=0.1,w_pad = 0.1)
    draw()
    return ax_grid,row_epoch_panels,col_epoch_panels

class DivergingCMapCreator(object):
    hsv_arr = np.zeros((1,50,3))
    
    def get_sincurve(self,gam,end,cent):
        """return normalized sin**gam curve"""
        rng = np.linspace(0,np.pi,50)
        return (((np.sin(rng)**gam))*(cent-end))+(end)

    def get_sigcurve(self,k0,start,stop):
        """return normalized sigmoid"""
        rng = np.linspace(0,1,50)
        return (stop-start)/(1+np.exp(k0*(0.5-rng)))+start

    def set_hsvs(self,hk,hstart,hstop,
                  sgam,send,scent,
                  vgam,vend,vcent):
        """create the colormap in HSV space"""
        self.hsv_arr[0,:,0] = self.get_sigcurve(hk,hstart,hstop)
        self.hsv_arr[0,:,1] = self.get_sincurve(sgam,send,scent)
        self.hsv_arr[0,:,2] = self.get_sincurve(vgam,vend,vcent)
        return self.hsv_arr

    def get_mpl_cmap(self):
        """return a matplotlib colormap"""
        from matplotlib.colors import LinearSegmentedColormap
        import matplotlib.colors as mplcols
        rgb = mplcols.hsv_to_rgb(self.hsv_arr)
        in_map = np.linspace(0,1,50)
        cdict = {'red':np.vstack  ((in_map,rgb[0,:,0],rgb[0,:,0])).T,
                 'green':np.vstack((in_map,rgb[0,:,1],rgb[0,:,1])).T,
                 'blue':np.vstack ((in_map,rgb[0,:,2],rgb[0,:,2])).T,
        }
        return LinearSegmentedColormap('custom', cdict)
        
cm_creator = DivergingCMapCreator()
def plot_hsvs(hk,hstart,hstop,
                  sgam,send,scent,
                  vgam,vend,vcent):
        """show the colormap"""
        dta = cm_creator.set_hsvs(hk,hstart,hstop,
                      sgam,send,scent,
                      vgam,vend,vcent)
        from matplotlib import gridspec
        from scipy.misc import face
        import plotfuncs as plf
        import matplotlib.colors as mplcols
        gs = gridspec.GridSpec(2,2)
        
        plb.subplot(gs[0,0])
        plb.plot(dta[0,:,:])
        plb.gca().set_ybound(0,1)
        plf.pull_ax_spines()
        
        plb.subplot(gs[1,0])
        plb.imshow(mplcols.hsv_to_rgb(dta),aspect = 'auto')
        plf.kill_spines()
        from scipy.misc import ascent
        
        plb.subplot(gs[:,1])
        plb.imshow(ascent()[::5,::5],cmap = cm_creator.get_mpl_cmap())

#from ipywidgets import interact

#zto = (0,1,0.1)
#interact(plot_hsvs,hk = (0,1000,10),
#                   hstart = (0,1,0.01),
#                   hstop = (0,1,0.01),
#                   sgam = (0,20,0.1),
#                   send = zto,
#                   scent = zto,
#                   vgam = (0,20,0.1),
#                   vend = zto,
#                   vcent = zto)

if __name__ == '__main__':
    plot_data_matrix()