import pandas as pd
try:
    from plotly.offline import iplot
    import cufflinks as cf
    cf.go_offline()
except ImportError:
    raise Exception("This plotly code only works within a jupyter notebook")


class NBplot:
    '''
    Work in Jupyter notebooks only.
    Set of plots for a single time series and groups.

    '''
    def __init__(self, db):
        '''
        db is an instance of a DataBase class that contains the time series.
        '''
        self.db = db

    def sgplot_dp(self, tscode):
        '''
        plot of a single driving profile
        tscode is time series code. Eg. 'ev_user_W3_85e59'
        '''
        df = self.db.db[tscode]['timeseries'].copy()
        if self.db.db[tscode]['kind'] != 'driving':
            raise Exception("code '{}' does not correspond to a driving profile".format(tscode))

        cnt = df.groupby([df.index,'state'])['state'].count()
        cn = pd.DataFrame(cnt).rename(columns={'state':'count'}).unstack(level=-1).fillna(0)
        cn.columns = cn.columns.droplevel()
        rr = (cn.T/cn.T.sum(axis=0)).T
        figa = rr.iplot(kind='area', fill=True,asFigure=True)
        figb = df['distance'].iplot(asFigure=True)
        fig = cf.subplots([figa,figb],shape=(2,1),shared_xaxes=True)
        fig['layout']['yaxis'].update({'title': 'Location', 'rangemode':"tozero",'domain': [0.7, 1.0]})
        fig['layout']['yaxis2'].update({'title': 'Distance (km)','rangemode':"tozero",'domain': [0.0, 0.65]})
        return iplot(fig, show_link=False)

    def sgplot_ga(self, tscode):
        '''
        plot of a single grid availability profile
        tscode is time series code. Eg. 'ev_user_W3_85e59_avai_65t2p'
        '''
        df = self.db.db[tscode]['timeseries'].copy()
        if self.db.db[tscode]['kind'] != 'availability':
            raise Exception("code '{}' does not correspond to a grid availability profile".format(tscode))

        dt = df[['state', 'consumption','charging_point','charging_cap','soc']]
        cnt = dt.groupby([dt.index,'state'])['state'].count()
        cn = pd.DataFrame(cnt).rename(columns={'state':'count'}).unstack(level=-1).fillna(0)
        cn.columns = cn.columns.droplevel()
        rr = (cn.T/cn.T.sum(axis=0)).T
        figa = rr.iplot(kind='area', fill=True,asFigure=True)
        dk = dt[['consumption','charging_cap']]
        figb = dk.iplot(asFigure=True)
        dd = dt['soc']
        figc = dd.iplot(asFigure=True)
        fig = cf.subplots([figa,figb,figc],shape=(3,1),shared_xaxes=True)
        fig['layout']['xaxis'].update({'tickfont':{'family': 'Arial, sans-serif','size': 13,'color': 'black'}})
        fig['layout']['yaxis'].update({'title': 'Location','titlefont': {'size':12},'showgrid': False,'showline':True,'rangemode':"tozero", 'zeroline' : True,'domain': [0.75, 1.0],'tickformat' : '%','tickfont': {'family': 'Arial, sans-serif','size': 12,'color': 'black'},'linewidth':2})
        fig['layout']['yaxis2'].update({'title': '','titlefont': {'size':12},'showgrid': True,'showline':True,'rangemode':"tozero",'domain': [0.4, 0.7],'tickfont': {'family': 'Arial, sans-serif','size': 12,'color': 'black'},'linewidth':2})
        fig['layout']['yaxis3'].update({'title': 'SOC','titlefont': {'size':12},'showgrid': True,'showline':True,'rangemode':"tozero",'domain': [0.0, 0.35],'tickformat' : '%','tickfont': {'family': 'Arial, sans-serif','size': 12,'color': 'black'},'linewidth':2})
        fig['layout'].update({'paper_bgcolor': 'white','plot_bgcolor': 'white','margin': dict(l=10, r=10, t=20, b=10, pad=0),'width': 800,'height': 450,'showlegend': True})
        return iplot(fig,show_link=False)

    def sgplot_ged(self, tscode):
        '''
        plot of grid electricity demand profiles associated with the same grid availability profile
        tscode is time series code. Eg. 'ev_user_W3_85e59_avai_65t2p'
        '''
        if self.db.db[tscode]['kind'] != 'charging':
            raise Exception("code '{}' does not correspond to a grid electricity demand profile".format(tscode))
        df = pd.DataFrame()
        availcode = self.db.db[tscode]['input']
        for k in self.db.db.keys():
            if self.db.db[k]['kind'] == 'charging':
                if self.db.db[k]['input'] == availcode:
                    tmp = self.db.db[k]['timeseries'].copy()
                    tmp.loc[:,'option'] = self.db.db[k]['option']
                    df = df.append(tmp, sort=False)

        dt = df[['state','actual_soc','charge_grid','option']]
        cnt = dt.groupby([dt.index,'state'])['state'].count()
        cn = pd.DataFrame(cnt).rename(columns={'state':'count'}).unstack(level=-1).fillna(0)
        cn.columns = cn.columns.droplevel()
        rr = (cn.T/cn.T.sum(axis=0)).T
        figc = rr.iplot(kind='area', fill=True,asFigure=True)
        dff = dt.pivot_table(index=dt.index, columns='option', values='actual_soc',aggfunc='sum')
        figa = dff.iplot(asFigure=True)
        dg = dt.pivot_table(index=dt.index, columns='option', values='charge_grid',aggfunc='sum')
        figb = dg.iplot(asFigure=True)
        fig = cf.subplots([figa,figb,figc],shape=(3,1),shared_xaxes=True)
        fig['layout']['xaxis'].update({'tickfont':{'family': 'Arial, sans-serif','size': 14,'color': 'black'}})
        fig['layout']['yaxis'].update({'title': 'SOC','titlefont': {'size':14},'showgrid': False,'showline':True,'rangemode':"tozero", 'zeroline' : True,'domain': [0.7, 1.0],'tickformat' : '%','tickfont': {'family': 'Arial, sans-serif','size': 14,'color': 'black'},'linewidth':2})
        fig['layout']['yaxis2'].update({'title': 'Actual charge (kWh)','titlefont': {'size':14},'showgrid': True,'showline':True,'rangemode':"tozero",'domain': [0.25, 0.65],'tickfont': {'family': 'Arial, sans-serif','size': 12,'color': 'black'},'linewidth':2})
        fig['layout']['yaxis3'].update({'title': 'Location','titlefont': {'size':14},'showgrid': True,'showline':True,'rangemode':"tozero",'domain': [0.0, 0.2],'tickformat' : '%','tickfont': {'family': 'Arial, sans-serif','size': 12,'color': 'black'},'linewidth':2})
        fig['layout'].update({'paper_bgcolor': 'white','plot_bgcolor': 'white','margin': dict(l=10, r=10, t=20, b=10, pad=0),'width': 800,'height': 450,'showlegend': True})
        return iplot(fig,show_link=False)
