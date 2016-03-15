from pylab import *
import numpy as np

def kill_spines():
    gca().spines['left'].set_visible(False)
    gca().spines['top'].set_visible(False)
    gca().spines['right'].set_visible(False)
    gca().spines['bottom'].set_visible(False)
    [x.set_visible(False) for x in gca().get_xticklabels()]
    [y.set_visible(False) for y in gca().get_yticklabels()]
    [x.set_visible(False) for x in gca().get_xticklines()]
    [y.set_visible(False) for y in gca().get_yticklines()]

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

def plot_data_matrix(cols = cols,
                     rows = rows,
                     
                     row_label_pos = 'left',
                     col_label_pos = 'bottom',
                     
                     row_spine_pos = 'left',
                     col_spine_pos = 'bottom',
                     
                     figsize = figsize,
                     ybounds = ybounds,
                     xbounds = xbounds,
                     
                     xtick_numbers = xtick_numbers,
                     ytick_numbers = ytick_numbers,
                     
                     col_epochs = col_epochs,
                     row_epochs = row_epochs,
                     
                     col_epochs_kwargs = {'alpha':0.2,'color':'b','lw':None},
                     row_epochs_kwargs = {'alpha':0.2,'color':'b','lw':None},
                     
                     col_labels_bottom = col_labels_bottom,
                     row_labels_left = row_labels_left,
                     
                     col_labels_top = col_labels_top,
                     row_labels_right = row_labels_right,
                     
                     gs_left = 0.05,
                     gs_right = 0.95,
                     gs_wspace = 0.1,
                     gs_hspace = 0.5,
                     plot_panel_function = plot_panel_function,
                     show_spines_left = show_spines_left,
                     show_spines_right = show_spines_right,
                     show_spines_top = show_spines_top,
                     show_spines_bottom = show_spines_bottom):
    
    
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

    for panel,col_epoch,col_epochs_kwarg in zip(col_epoch_panels,col_epochs,col_epochs_kwargs):
        sca(panel)
        if col_epoch:
            axvspan(*col_epoch,**col_epochs_kwarg)
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
            sca(row[-1][1])
            gca().yaxis.set_label_position("right")
            gca().set_ylabel(row_label,rotation = -90,va = 'bottom')
    
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
    gs.tight_layout(fig,h_pad=0.3,w_pad = 0.3)
    draw()
    return ax_grid,row_epoch_panels,col_epoch_panels
    
if __name__ == '__main__':
    plot_data_matrix()