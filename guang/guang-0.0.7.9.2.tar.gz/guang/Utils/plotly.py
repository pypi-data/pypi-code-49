import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px

def imshow(
        img,
        zmin=None,
        zmax=None,
        origin=None,
        color_continuous_scale=None,
        color_continuous_midpoint=None,
        range_color=None,
        title=None,
        template=None,
        width=None,
        height=None
           ):
    return px.imshow(
        img,
        zmin=None,
        zmax=None,
        origin=None,
        color_continuous_scale=None,
        color_continuous_midpoint=None,
        range_color=None,
        title=None,
        template=None,
        width=None,
        height=None)
imshow.__doc__ = px.imshow.__doc__


class Subplots:
    def __init__(self, rows=1, cols=1, **kwargs):
        self.rows = rows
        self.cols = cols
        x_title = kwargs.get('x_title', 'x_title')
        y_title = kwargs.get('y_title', 'y_title')
        self.fig = make_subplots(rows=rows, cols=cols, x_title=x_title, y_title=y_title)
        self.count = 0

    def plot(self, x, y, **kwargs):
        '''
        Params:
            --label: look like matplotlib's legend
            --mode: 'lines', 'markers', 'lines+markers', 'text'
            --marker_color
            --line_color
            --marker_size

        '''
        label = kwargs.get('label', self.count + 1)
        mode = kwargs.get('mode', 'lines')  #
        line_color = kwargs.get('line_color', None)
        marker_color = kwargs.get('marker_color', None)
        marker_size = kwargs.get('marker_size', None)
        row, col = np.divmod(self.count, self.cols)
        row, col = int(row + 1), int(col + 1)

        self.fig.add_trace(go.Scatter(x=x, y=y, mode=mode, marker_color=marker_color,
                                      line_color=line_color,
                                      marker_size=marker_size,
                                      name=label),
                           row=row, col=col)

        self.count += 1

    def show(self, *args, **kwargs):
        self.fig.show(*args, **kwargs)


class Multiplots:
    def __init__(self, **kwargs):
        #         self.title = 'title'
        self.title = 'fig.title'
        self.fig = go.Figure()
        self.xlabel = 'fig.xlabel'
        self.ylabel = 'fig.ylabel'
        self.count = 0
        self.annotations = []

    def plot(self, *args, **kwargs):
        '''
        Params:
            :param label: look like matplotlib's legend.
            :param mode: 'lines'(default), 'markers', 'lines+markers', 'text'
            :param line_width: corresponding lines mode.
            :param marker_size: corresponding of markers mode.
            :param text: hovering text
        '''
        if (len(args) >1 and type(args[0]) != type(args[1])) or len(args)==1:
            y = args[0]
            x = np.arange(len(y))
        else:
            y = args[1]
            x = args[0]

        label = kwargs.get('label', self.count + 1)
        mode = kwargs.get('mode', 'lines')  #
        line_width = kwargs.get('line_width', None)
        marker_size = kwargs.get('marker_size', None)
        text = kwargs.get('text', f'f(x)')
        self.fig.add_trace(go.Scatter(x=x, y=y,
                                      mode=mode,
                                      name=label,
                                      text=text,
                                      marker_line_width=line_width,
                                      marker_size=marker_size))
        self.count += 1

    def show(self, *args, **kwargs):
        Multiplots.show.__doc__ = self.fig.show.__doc__


        self.annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,  # title
                                     xanchor='left', yanchor='bottom',
                                     text=self.title,
                                     font=dict(family='Arial',
                                               size=30,
                                               color='rgb(37,37,37)'),
                                     showarrow=False))
        #
        self.annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,  # X axis
                                     xanchor='center', yanchor='top',
                                     text=self.xlabel,
                                     font=dict(family='Arial',
                                               size=15,
                                               color='rgb(150,150,150)'),
                                     showarrow=False))

        self.fig.update_layout(
            # title=f'{self.title:}',
            overwrite=False,

            yaxis=dict(
                title=self.ylabel,
                showgrid=True,

                zeroline=False,
                showline=True,
                showticklabels=True,),

            xaxis=dict(
                # title=self.xlabel,
                showline=True,
                showgrid=True,
                showticklabels=True,
                linecolor='rgb(204, 204, 204)',
                linewidth=2,
                ticks='outside',
                tickfont=dict(
                    family='Arial',
                    size=12,
                    color='rgb(82, 82, 82)'),
                        ),
            annotations=self.annotations
        )
        self.fig.show(*args, 
                      config={'editable': True,
                            'scrollZoom': False,
                             }, 
                      **kwargs)

    def write_html(self, *args, **kwargs):
        Multiplots.write_html.__doc__ = self.fig.write_html.__doc__
        return self.fig.write_html(*args, **kwargs)

    def write_image(self, *args, **kwargs):
        Multiplots.write_image.__doc__ = self.fig.write_image.__doc__
        return self.fig.write_image(*args, **kwargs)


class Scatter3d():
    def __init__(self, **kwargs):
        self.fig = go.Figure()


    def scatter3d(self,x, y, z, mode=None, color_line=None,color_marker=None,marker_size=4,line_width=2):
        """
        Params:
            :param mode: 'lines', 'markers', 'lines+markers'(default), 'text'
            :param marker_size: corresponding of markers mode.
        """
        if color_marker is None:
            color_marker = None#z
        if color_line is None:
            color_line = None#'darkblue'

        self.fig.add_trace(go.Scatter3d(x=x,y=y,z=z, 
                                        mode=mode,
                                        
                                        marker=dict(
                                        size=marker_size,
                                        color=color_marker,
                                        colorscale='Viridis',
                                        ),
                                        
                                        line=dict(
                                            color=color_line,
                                            width=line_width
                                                  ),
                                    ))
    def show(self,*args, **kwargs):
        
        self.fig.update_layout(
            width=800,
            height=700,
            autosize=False,
            scene=dict(
                camera=dict(
                    up=dict(
                        x=0,
                        y=0,
                        z=1
                    ),
                    eye=dict(
                        x=0,
                        y=1.0707,
                        z=1,
                    )
                ),
                aspectratio = dict( x=1, y=1, z=0.7 ),
                aspectmode = 'manual'
            ),
        )
        self.fig.show(*args, 
                      config={'editable': True,
                            'scrollZoom': True,
                             },**kwargs)

    def write_html(self, *args, **kwargs):
        Multiplots.write_html.__doc__ = self.fig.write_html.__doc__
        return self.fig.write_html(*args, **kwargs)

    def write_image(self, *args, **kwargs):
        Multiplots.write_image.__doc__ = self.fig.write_image.__doc__
        return self.fig.write_image(*args, **kwargs)

class Surface():
    def __init__(self, **kwargs):
        self.fig = go.Figure()


    def surface(self,**kwargs):
        """
        point x= y= z= 
        or z=
        x, y, z should be 2D array.
        """

        self.fig.add_surface(**kwargs)
        
    def show(self,*args, **kwargs):
        
        self.fig.update_layout(
            width=800,
            height=700,
            autosize=False,
            margin=dict(l=65, r=50, b=65, t=90), 

        )
        self.fig.show(*args, 
                      config={'editable': True,
                            'scrollZoom': True,
                             },**kwargs)

    def write_html(self, *args, **kwargs):
        Multiplots.write_html.__doc__ = self.fig.write_html.__doc__
        return self.fig.write_html(*args, **kwargs)

    def write_image(self, *args, **kwargs):
        Multiplots.write_image.__doc__ = self.fig.write_image.__doc__
        return self.fig.write_image(*args, **kwargs)