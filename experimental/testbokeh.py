# myapp.py

import numpy as np

from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc, vplot

from bokeh.models import CustomJS, ColumnDataSource, BoxSelectTool, Range1d, Rect
from bokeh.plotting import figure, output_file, show

from bokeh.client import push_session

#output_file("boxselecttool_callback.html")

source = ColumnDataSource(data=dict(x=[], y=[], width=[], height=[]))
source2 = ColumnDataSource(data=dict(x=[], y=[], width=[], height=[]))

callback = CustomJS(args=dict(source=source), code="""
        // get data source from Callback args
        var data = source.get('data');

        /// get BoxSelectTool dimensions from cb_data parameter of Callback
        var geometry = cb_data['geometry'];

        /// calculate Rect attributes
        var width = geometry['x1'] - geometry['x0'];
        var height = geometry['y1'] - geometry['y0'];
        var x = geometry['x0'] + width/2;
        var y = geometry['y0'] + height/2;

        /// update data source with new Rect attributes
        data['x'].push(x);
        data['y'].push(y);
        data['width'].push(width);
        data['height'].push(height);

        // trigger update of data source
        source.trigger('change');
    """)

box_select = BoxSelectTool(callback=callback)

p = figure(plot_width=400,
           plot_height=400,
           tools=[box_select],
           title="Select Below",
           x_range=Range1d(start=0.0, end=1.0),
           y_range=Range1d(start=0.0, end=1.0))

rect = Rect(x='x',
            y='y',
            width='width',
            height='height',
            fill_alpha=0.3,
            fill_color='#009933')

#ds = r1.data_source

p.add_glyph(source, rect, selection_glyph=rect, nonselection_glyph=rect)

sess_holder = dict()
def ds_callback():
    print('here')
    
def update():
    print p.document._all_models_by_name.__dict__.keys()
    #for key,value in p.__dict__.items():
    #    print(key,value)

#source.add_callback(ds_callback)
# put the button and plot in a layout and add to the document

curdoc().add_root(vplot(p))
curdoc().add_periodic_callback(update, 1000)


session = push_session(curdoc())
sess_holder['session'] = session

session.loop_until_closed() # run forever

