import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import datetime
from IPython.display import clear_output, display
from collections import OrderedDict
import weibull
import scipy
import os
from scipy.stats import weibull_min
from .utils import *

file='Wonka'

class PlantPerformance():
    
    def split(self, df, event_type='offspec', quality_type='%FAT CONTENT', color_variable="PRODUCT", process_limits="Wonka", xsize=5, ysize=5):
        """
        crow-amsaa/weibull analysis for events

        Parameters
        ----------
        df: DataFrame
            DataFrame of plant data
        event_type: str, default offspec
            type of events. Current options are: offspec,
            quality, or downtime
        quality_type: str, default none
            if quality is selected for event type, current options
            are ['%FAT CONTENT', '%SHELL CONTENT', 'PH', 'ASH CONTENT']
            for liquor data   
        color_variable: str, default PRODUCT
            PRODUCT, FEED, or AUTO. Other options in later versions
        process_limits: str or iterable, default 'Wonka'
            if event_type is set to quality and control_limits is
            none, an attempt will be made to infer the control limits
            from the spec file. Otherwise, user define control limits
            will set the event trigger for crow-amsaa/weibull. (ucl, lcl).
        xsize: int, default 5
            figure size x dim
        ysize: int, default 5
            figure size y dim
        
        Returns
        -------
        self.crow_fig 
        self.crow 
        self.weibull_fig
        self.weibull
        self.event
        self.current_state
        """
        df.loc[~df["UOM"].isin(['HOUR', 'DATE TIME']), "VALUE"] = pd.to_numeric(df.loc[~df["UOM"].isin(['HOUR', 'DATE TIME'])]["VALUE"], errors='ignore')
#         df.loc[df["UOM"].isin(['HOUR', 'DATE TIME']), "VALUE"] = pd.to_datetime(df.loc[df["UOM"].isin(['HOUR', 'DATE TIME'])]["VALUE"])
        if color_variable == "AUTO":
            feeds = df.loc[(df["Stream Type"].isin(["FEED"])) & (df["Scheduled or Actual"] == "A")]["ITEM"].unique()
            products = df.loc[(df["Stream Type"].isin(["PRODUCT"])) & (df["Scheduled or Actual"] == "A")]["ITEM"].unique()
            if len(feeds) > len(products):
                color_variable = "FEED"
            else:
                color_variable = "PRODUCT"
                
        items = df.loc[(df["Stream Type"].isin([color_variable])) & (df["Scheduled or Actual"] == "A") & (df["Attribute Type"] == "VOLUME")]["ITEM"].reset_index(drop=True)
        items.columns = ["ITEM"]
        if event_type == 'offspec':       
            products = df.loc[df['Stream Type'] == "PRODUCT"]["ITEM"].unique()
            ids = df.loc[(df["ITEM"].isin(products))]["ID"].unique()
            df = df.loc[df["ID"].isin(ids)]
            if df.loc[(df["Stream Type"].isin(["OFFSPEC PRODUCT"]))].shape[0] == 0:
                print("OFFSPEC PRODUCT not in label")
                return 0
            prod_off =  df.loc[(df["Stream Type"].isin(["OFFSPEC PRODUCT", "PRODUCT"])) & (df["Scheduled or Actual"] == "A")]
            prod_off["VALUE"] = pd.to_numeric(prod_off["VALUE"])
            prod_off = prod_off.reset_index(drop=True)
            frac_offspec = prod_off["VALUE"][1::2].reset_index(drop=True) / prod_off["VALUE"][0::2].reset_index(drop=True)
            time = df.loc[(df["ITEM"] == "START TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True)
            dff = pd.DataFrame([items, time, frac_offspec]).T
            dff.columns = ["item", "time", "offspec"]
            dff["time"] = pd.to_datetime(dff["time"])
            dff["offspec"] = pd.to_numeric(dff["offspec"])
            dff["ID"] = df["ID"].unique()

            # calc process boundaries
            lines = pd.to_numeric(dff['offspec']).describe()
            IQR = lines["75%"] - lines["25%"]
            iqr_maximum = 3 * IQR + lines["75%"]
            iqr_minimum = max([- 3 * IQR + lines["25%"], 0])
            lines["iqr_maximum"] = iqr_maximum
            lines["iqr_minimum"] = iqr_minimum

            # make crow-amsaa plot
            control_limit = lines["75%"]
            event = dff.loc[pd.to_numeric(dff['offspec']) > control_limit]
            good = dff.loc[pd.to_numeric(dff['offspec']) <= control_limit]

        if event_type == 'quality':
            item = quality_type
            y = pd.to_numeric(df.loc[df["UOM"] == item]["VALUE"])
            x1 = pd.to_datetime(df.loc[(df["ITEM"] == "START TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"])
            x2 = pd.to_datetime(df.loc[(df["ITEM"] == "END TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"])
            
            # calc process boundaries
            lines = pd.to_numeric(y).describe()
            IQR = lines["75%"] - lines["25%"]
            iqr_maximum = 3 * lines["std"] + lines["50%"]
            iqr_minimum = max([- 3 * lines["std"] + lines["50%"], 0])
            lines["iqr_maximum"] = iqr_maximum
            lines["iqr_minimum"] = iqr_minimum
            if type(process_limits) is str:
                try:
                    process_limits = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(process_limits)),
                                     sheet_name='LIQUOR PROCESS LIMITS')
                    ucl = process_limits.loc[process_limits["QUALITY"] == item]["UCL"].reset_index(drop=True)
                    lcl = process_limits.loc[process_limits["QUALITY"] == item]["LCL"].reset_index(drop=True) 
                except:
                    print('no process limits provided for quality calculation')
                    return 0
            else:
                try:
                    process_limits = pd.DataFrame(process_limits).T
                    ucl = process_limits[0]
                    lcl = process_limits[1]
                except:
                    print('no process limits provided for quality calculation')
                    return 0
            
            
            frac_offspec = df.loc[(df["UOM"] == item)]["VALUE"].reset_index(drop=True)
            if frac_offspec.shape[0] == 0:
                print("quality_type variable not in provided dataframe")
                return 0
            time = df.loc[(df["ITEM"] == "START TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True)
            dff = pd.DataFrame([time, frac_offspec]).T
            dff.columns = ["time", "offspec"]
            dff["time"] = pd.to_datetime(dff["time"])
            dff["item"] = items
            dff["ID"] = df["ID"].unique()
            control_limit = ucl.values[0]
            event = dff.loc[pd.to_numeric(dff['offspec']) > float(control_limit)]     
            good = dff.loc[pd.to_numeric(dff['offspec']) <= float(control_limit)]   
            
        if event_type == 'downtime':
            item = 'downtime'
            x1 = pd.to_datetime(df.loc[(df["ITEM"] == "START TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True))
            x2 = pd.to_datetime(df.loc[(df["ITEM"] == "END TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True))
            prod_off =  df.loc[(df["Stream Type"].isin(["PRODUCT"])) & (df["Scheduled or Actual"] == "A")]
            prod_off = prod_off.reset_index(drop=True)
            downtime = x1[1:] - x2.shift()[1:]
            downtime = pd.to_numeric(downtime.dt.total_seconds()/60/60)
            dff = pd.DataFrame([x1.values[1:], downtime.values]).T
            dff.columns = ["time", "offspec"]
            dff["item"] = items[1:].reset_index(drop=True)
            dff["ID"] = df["ID"].unique()[1:]
            event = dff.loc[pd.to_numeric(dff['offspec']) > 0]
            good =  dff.loc[pd.to_numeric(dff['offspec']) <= 0]
            ucl = lcl = 0 # downtime is when process flow is at 0
            lines = 0
            
        if event_type == "waste":
            item = 'waste'
            prod_off = df.loc[(df["Stream Type"] == "WASTE") & (df["Attribute Type"].isin(["TIME", "VOLUME"]))].groupby("ID", sort=False)["VALUE"].sum().reset_index(drop=True)
            time = df.loc[(df["ITEM"] == "START TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True)
            dff = pd.DataFrame([items, time, prod_off]).T
            dff.columns = ["item", "time", "offspec"]
            dff["ID"] = df["ID"].unique()

            # performance specs
            lines = pd.to_numeric(dff['offspec']).describe()
            IQR = lines["75%"] - lines["25%"]
            iqr_maximum = 3 * IQR + lines["75%"]
            iqr_minimum = max([- 3 * IQR + lines["25%"], 0])
            lines["iqr_maximum"] = iqr_maximum
            lines["iqr_minimum"] = iqr_minimum

            # calc process boundaries
            if type(process_limits) is tuple:
                try:
                    process_limits = pd.DataFrame(process_limits).T
                    ucl = process_limits[0][0]
                    lcl = process_limits[1][0]
                except:
                    print('process limits in improper format')
                    return 0
            else:   
                ucl = lines["75%"] 
                lcl = lines["25%"]
            event = dff.loc[pd.to_numeric(dff['offspec']) > ucl]
            good = dff.loc[pd.to_numeric(dff['offspec']) <= ucl] # waste has no lower control limit
            
        self.event = event
        self.good = df.loc[df["ID"].isin(good["ID"])] ### grabbing whole dataframe
        self.bad = df.loc[df["ID"].isin(event["ID"])]
        self.df = df
        self.dff = dff
        self.event_type = event_type
        self.item = item
        self.ucl = ucl
        self.lcl = lcl
        self.lines = lines
              
    def predict(self, xsize=5, ysize=5):
        df = self.df
        dff = self.dff
        event = self.event
        event_type = self.event_type
        item = self.item
        lines = self.lines
        ucl = self.ucl
        lcl = self.lcl
        
        if event.shape[0] > 3:
            dff["offspec"] = pd.to_numeric(dff["offspec"])
            dff["time"] = pd.to_datetime(dff["time"])

            ### crow-amsaa calculations
            n = event.index[-1] #last fail event number
            time_delta = pd.to_datetime(event.iloc[-1]["time"]) - pd.to_datetime(event.iloc[0]["time"])
            T = time_delta.total_seconds() /60/60 #last fail event hour
            event["time to event"] = pd.to_datetime(event["time"]) - pd.to_datetime(event.iloc[0]["time"])
            event["time to event"] = event["time to event"].dt.total_seconds()/60/60
            MTBF = []
            for index, i in enumerate(event.index):
                if index > 10:
                    MTBF.append(time_to_next_failure(event["time to event"][:index]))
                else:
                    MTBF.append(0)
            df_ca = pd.DataFrame(event["time to event"])
            df_ca['MTBF'] = MTBF
            df_ca['Prediction'] = df_ca['time to event'] + df_ca['MTBF']
            df_ca['Date'] = pd.to_datetime(event["time"])
            df_ca = df_ca.reset_index(drop=True) #calls to event be made before this
            df_ca["Predicted Date"] = df_ca["Date"][0] + pd.to_timedelta(df_ca["Prediction"], unit='hr')
            next_predicted_event = df_ca.iloc[-1]["Predicted Date"]
            last_real_event = df_ca.iloc[-1]["Date"]
            df_ca.Prediction = df_ca.Prediction.shift(1) #to calc error move pred forward one row
            df_ca['Prediction'][0] = 0
            df_ca['Error'] = df_ca['Prediction'] - df_ca['time to event']
            
            if event_type == 'offspec':
                print("{} avg prediction error in hrs: {:.2f}, (N = {})".\
                      format(items.unique(), np.average(np.abs(df_ca['Error'][4:])), df_ca.shape[0]))
                print("{} median prediction error in hrs: {:.2f}, (N = {})".\
                      format(items.unique(), np.median(np.abs(df_ca['Error'][4:])), df_ca.shape[0]))
            else:
                print("{} avg prediction error in hrs: {:.2f}, (N = {})".\
                      format(item, np.average(np.abs(df_ca['Error'][4:])), df_ca.shape[0]))
                print("{} median prediction error in hrs: {:.2f}, (N = {})".\
                      format(item, np.median(np.abs(df_ca['Error'][4:])), df_ca.shape[0]))

            # weibull comparison
            TTF = pd.to_datetime(self.event['time']) - pd.to_datetime(self.event['time'].shift())
            TTF = TTF.dt.total_seconds()/60/60
            fail_times = TTF
            try:
                weibull_analysis = weibull.Analysis(fail_times, unit='hour')
                weibull_analysis.fit()
                print(weibull_analysis.stats)
                weibull_fig, ax = plt.subplots(1,1,figsize=(xsize,ysize))
                weibull_analysis.probplot(ax=ax)
            except:
                print("weibull analysis unsuccessful")
                weibull_analysis = weibull_fig = False

            # display crow-amsaa results
            crow_fig, ax = plt.subplots(1,3,figsize=(xsize*3,ysize))
            ax[0].plot(df_ca['Prediction'][:], ls='', marker='^', alpha=0.5, label='prediction')
            ax[0].plot(df_ca['time to event'][:], ls='', marker='.', alpha=0.5, label='actual')
            ax[0].plot(df_ca['Error'][:], ls='', marker='*', alpha=0.5, label='error')
            ax[0].set_ylabel('cumulative hours')
            ax[0].set_xlabel('cumulative failures')
            ax[0].set_title('crow-amsaa analysis')
            ax[0].legend()

            # display time series
            if (event_type == 'downtime'):
                for index, item in enumerate(dff.item.unique()):
                    ax[1].plot(dff.loc[dff["item"] == item]["time"], dff.loc[dff["item"] == item]["offspec"], ls='--', marker='*', label=item)
                    ax[2].bar(index, event.loc[event["item"] == item]["offspec"].sum(), label=item)
            if (event_type == 'offspec'):
                for index, item in enumerate(dff.item.unique()):
                    ax[1].plot(dff.loc[dff["item"] == item]["time"], dff.loc[dff["item"] == item]["offspec"], ls='', marker='*', label=item)
                    ax[2].bar(index, event.loc[event["item"] == item]["offspec"].count(), label=item)
                ax[1].plot([min(dff["time"]), max(dff["time"])], [lines["75%"], lines["75%"]], c='tab:blue', ls='--', label='iqr bounds')
                ax[1].plot([min(dff["time"]), max(dff["time"])], [lines["25%"], lines["25%"]], c='tab:blue', ls='--')
                ax[1].set_yscale("log")
                               
            if event_type == 'quality':
                for index, item in enumerate(dff.item.unique()):
                    ax[1].plot(dff.loc[dff["item"] == item]["time"], dff.loc[dff["item"] == item]["offspec"], ls='', marker='*', label=item)
                    ax[2].bar(index, event.loc[event["item"] == item]["offspec"].count(), label=item)
                y = pd.to_numeric(df.loc[df["UOM"] == item]["VALUE"])
                x1 = pd.to_datetime(df.loc[(df["ITEM"] == "START TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"])
                x2 = pd.to_datetime(df.loc[(df["ITEM"] == "END TIME") & (df["Scheduled or Actual"] == "A")]["VALUE"])
                ax[1].hlines(y,x1,x2)
                ax[1].set_title(item)
                ax[1].plot([min(dff["time"]), max(dff["time"])], [lines["75%"], lines["75%"]], c='tab:blue', ls='--', label='iqr bounds')
                ax[1].plot([min(dff["time"]), max(dff["time"])], [lines["25%"], lines["25%"]], c='tab:blue', ls='--')
                ax[1].plot([min(x1), max(x2)], [lcl, lcl], c='tab:green', ls='--', label='control limits')
                ax[1].plot([min(x1), max(x2)], [ucl, ucl], c='tab:green', ls='--')
            ax[1].legend(loc=1)
            ax[1].set_title('time series') 
            ax[2].set_title('events by material')
            ax[2].legend(loc=1)
            self.crow_fig, self.crow = crow_fig, df_ca
            if weibull_fig:
                self.weibull_fig, self.weibull = weibull_fig, pd.DataFrame(weibull_analysis.stats).T
            self.event = event
            current_date = df.loc[(df["ITEM"] == "END TIME") & (df["Scheduled or Actual"] == "A")].iloc[-1]["VALUE"]
            current_state = pd.DataFrame([next_predicted_event, last_real_event, current_date]).T
            current_state.columns = ["next_predicted_event", "last_real_event", "current_date"]
            self.current_state = current_state
        else:
            print('no events outside of bounds')   
            
    def moods(self, mode="quality"):
        """
        returns results from moods median test
        
        Parameters
        ----------
        mode: str, default quality
            what Attribute Type to return moods median test on
        
        Returns
        -------
        """
        good = self.good
        bad = self.bad
        moods_table = pd.DataFrame()
        if mode == "quality":
            for atr in good.loc[good["Attribute Type"] == "QUALITY"]["ITEM"].unique(): #wonka will be broken rn switched form UOM
                try:
                    stat, p, m, table = scipy.stats.median_test(good.loc[good["ITEM"] == atr]["VALUE"].astype(float).reset_index(drop=True),
                                                            bad.loc[bad["ITEM"] == atr]["VALUE"].astype(float).reset_index(drop=True))
                    print(atr, "\nstat:\t", stat, "\n p:\t", p, "\n m:\t", m, "\n table:\t", table, "\n")
                    new = pd.DataFrame([atr, stat, p, m, table]).T
                    moods_table = pd.concat([moods_table, new])
                except:
                    pass
        moods_table.columns = ['attribute', 'stat', 'p', 'm', 'table']
        self.moods_table = moods_table
        


def time_to_next_failure(data):
    """
    returns the time to next failure given
    historical fail data
    
    Parameters
    ----------
    data: dictionary entry
        index column starts at 0, is the cummulative failures
        values column starts at 0, is the cummulative days

    Returns
    -------
    MTBF: float
        the calculated mean time between failures
    """
    n = data.index[-1]
    T = data.values[-1]
    beta = n / (n * np.log(T) - np.sum(np.log(data.values[1:])))
    lamb = n / (T**beta)
    lamb_hat = lamb * beta * T ** (beta-1) #failures / hour
    # if no improvements are made the MTBF is:
    return(1/lamb_hat)


def calc_product_metrics(product, data, verbose=0, stream_designation="PRODUCT"):
    """
    compute metrics by product for the data contained in the current window
    
    Parameters
    ----------
    product_recipe: str
        name of excel sheet to read in product recipe
    product: list of str
        products created in single process ID (i.e. same
        feed origin)
    data: pandas DataFrame
        scheduler data
        
    Returns
    -------
    metrics: pandas DataFrame
        computed product metrics
    """
    
    ### Yields
    ids = data.loc[(data["Stream Type"] == stream_designation) & (data["Scheduled or Actual"] == "A") & (data["ITEM"].isin(product))]["ID"].values #process IDs selected based on product
    theo_yield = np.round(np.sum(data.loc[(data["ID"].isin(ids)) & (data["Scheduled or Actual"] == "S") & (data["Stream Type"] == "PRODUCT")]["VALUE"]) /\
                      np.sum(data.loc[(data["ID"].isin(ids)) & (data["Scheduled or Actual"] == "S") & (data["Stream Type"] == "FEED")]["VALUE"]),5) #scheduled yield

    rm_yield = np.round(np.sum(data.loc[(data["ID"].isin(ids)) & (data["Scheduled or Actual"] == "A") & (data["Stream Type"] == "PRODUCT")]["VALUE"]) /\
                      np.sum(data.loc[(data["ID"].isin(ids)) & (data["Scheduled or Actual"] == "A") & (data["Stream Type"] == "FEED")]["VALUE"]),5) #actual yield
    rm_theo_yield = rm_yield / theo_yield
    
    just_before = ids-1
    end_a = data.loc[(data["ITEM"] == "END TIME") & (data['Scheduled or Actual'] == "A") & (data["ID"].isin(just_before))]
    end_a = end_a.reset_index(drop=True)
    start_b = data.loc[(data["ITEM"] == "START TIME") & (data['Scheduled or Actual'] == "A") & (data["ID"].isin(ids))]
    start_b = start_b.reset_index(drop=True)
    end_b = data.loc[(data["ITEM"] == "END TIME") & (data['Scheduled or Actual'] == "A") & (data["ID"].isin(ids))]
    end_b = end_b.reset_index(drop=True)
    if end_a.shape[0] == start_b.shape[0] - 1: #correction for when nothin scheduled before
        end_a = pd.concat([pd.DataFrame(start_b.iloc[0]).T, end_a])
    end_a = end_a.reset_index(drop=True)

    downtime = start_b["VALUE"] - end_a["VALUE"]
    downtime = downtime.sum()
    uptime = end_b["VALUE"] - start_b["VALUE"]
    uptime_total = uptime.sum()

    ### frac uptime
    percent_uptime = uptime_total / (uptime_total + downtime)

    ### Rates
    total_kg_feed = np.sum(data.loc[(data["Stream Type"] == "FEED") & (data["Scheduled or Actual"] == "A") & (data["ID"].isin(ids))]["VALUE"])
    total_kg_product = np.sum(data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A") & (data["ID"].isin(ids)) & (data["Attribute Type"] == "VOLUME")]["VALUE"])
    feed_rate_mean = np.round(total_kg_feed / uptime_total.total_seconds() * 60 * 60, 2) #kg/min
    product_rate_mean = np.round(total_kg_product / uptime_total.total_seconds() * 60 * 60, 2) #kg/min
    
    ### MAC -- later version need to select top 5/30 day moving (DC,B/C)
    kg_feed = data.loc[(data["Stream Type"] == "FEED") & (data["Scheduled or Actual"] == "A") & (data["ID"].isin(ids))].groupby(["ID"], sort=False)["VALUE"].sum()
    kg_feed = kg_feed.reset_index(drop=True)
    kg_product = data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A") & (data["ID"].isin(ids)) & (data["Attribute Type"] == "VOLUME")].groupby(["ID"], sort=False)["VALUE"].sum()
    kg_product = kg_product.reset_index(drop=True)
    feed_rate = kg_feed / uptime.dt.total_seconds() * 60 * 60 #kg/min
    product_rate = kg_product / uptime.dt.total_seconds() * 60 * 60 #kg/min
    best_feed = feed_rate.sort_values(ascending=False)[:5].mean()
    best_product = product_rate.sort_values(ascending=False)[:5].mean()
            
    ### fraction avg vs best
    frac_rate_feed = feed_rate_mean / best_feed
    frac_rate_product = product_rate_mean / best_product
    
    ### FPFQ
    if stream_designation == "PRODUCT":
        total_kg_product = np.sum(data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A") & (data["ID"].isin(ids))]["VALUE"])
        total_offspec = np.sum(data.loc[(data["Stream Type"] == "OFFSPEC PRODUCT") & (data["Scheduled or Actual"] == "A") & (data["ID"].isin(ids))]["VALUE"])
        fpfq = total_kg_product - total_offspec
        fpfq_percent = fpfq / total_kg_product
    else:
        fpfq = None
    
    ### OEE
    oee_percent_feed = frac_rate_feed * rm_theo_yield * percent_uptime
    oee_percent_product = frac_rate_product * rm_theo_yield * percent_uptime
    
    if verbose == 0:
        print(product)
        print("dates: \t\t\t", start_b, " ", end_b)
        print("uptime: \t\t\t", percent_uptime)
        print("theoretical yield: \t\t" ,theo_yield)
        print("actual yield: \t\t\t" , rm_yield)
        print("actual / theoretical yield: \t", rm_theo_yield)
        print("total kg feed: \t\t\t", np.round(total_kg_feed, 2))
        print("total kg product: \t\t", np.round(total_kg_product, 2))
        print("feed rate (kg/hr): \t\t" , np.round(feed_rate_mean, 2))
        print("product rate (kg/hr): \t\t" , np.round(product_rate_mean, 2))
        print("MAC feed (kg/hr): \t\t", np.round(best_feed, 2))
        print("MAC product (kg/hr): \t\t", np.round(best_product, 2))
        print("% rate feed: \t\t\t", np.round(frac_rate_feed, 4))
        print("% rate product: \t\t", np.round(frac_rate_product, 4))
        if fpfq is not None:
            print("FPFQ: \t\t\t\t", np.round(fpfq, 2))
            print("% FPFQ: \t\t\t", np.round(fpfq_percent, 4))
        print("OEE Feed: \t\t\t", np.round(oee_percent_feed, 4))
        print("OEE Product: \t\t\t", np.round(oee_percent_product, 4))
        print('')
    
    if stream_designation == "PRODUCT":
        metrics = pd.DataFrame([product[0], min(start_b["VALUE"]), max(end_b["VALUE"]), percent_uptime, theo_yield, rm_yield, rm_theo_yield, total_kg_feed, total_kg_product,\
                feed_rate_mean, product_rate_mean, best_feed, best_product, frac_rate_feed,\
                frac_rate_product, fpfq, fpfq_percent, oee_percent_feed, oee_percent_product]).T
        metrics.columns = ["PRODUCT", "start", "stop", "uptime", "theoretical yield", "actual yield", "actual/theoretical yield", "total kg feed", "total kg product",\
                    "feed rate (kg/hr)", "product rate (kg/hr)", "MAC feed (kg/hr)", "MAC product (kg/hr)", "% rate feed",\
                    "% rate product", "FPFQ", "% FPFQ", "OEE Feed", "OEE Product"]
    else:
        metrics = pd.DataFrame([product[0], min(start_b["VALUE"]), max(end_b["VALUE"]), percent_uptime, theo_yield, rm_yield, rm_theo_yield, total_kg_feed, total_kg_product,\
                feed_rate_mean, product_rate_mean, best_feed, best_product, frac_rate_feed,\
                frac_rate_product, oee_percent_feed, oee_percent_product]).T
        metrics.columns = ["PRODUCT", "start", "stop", "uptime", "theoretical yield", "actual yield", "actual/theoretical yield", "total kg feed", "total kg product",\
                    "feed rate (kg/hr)", "product rate (kg/hr)", "MAC feed (kg/hr)", "MAC product (kg/hr)", "% rate feed",\
                    "% rate product", "OEE Feed", "OEE Product"]
    return metrics


def calc_line_metrics(metrics, line, verbose=0):
    """
    Calculates line metrics based on weight-averaged
    product metrics
    
    Parameters
    ----------
    metrics: pandas DataFrame
        contains product metrics for line
    line: str
        name of line
        
    Returns
    -------
    line_metrics: pandas DataFrame
        yield, rate, fpfq, and oee for the line
    """
    
    line_yield = np.sum(metrics["actual yield"] * metrics["total kg product"]) / np.sum(metrics["total kg product"])
    line_percent_rate_product = np.sum(metrics["% rate product"] * metrics["total kg product"]) / np.sum(metrics["total kg product"])
    
    if "% FPFQ" in metrics.columns:
        line_percent_fpfq = np.sum(metrics["% FPFQ"] * metrics["total kg product"]) / np.sum(metrics["total kg product"])
    else:
        line_percent_fpfq = None
    line_oee = np.sum(metrics["OEE Product"] * metrics["total kg product"]) / np.sum(metrics["total kg product"])
    line_metrics = pd.DataFrame([line_yield, line_percent_rate_product, line_percent_fpfq, line_oee]).T
    line_metrics.columns = ['Yield', 'Rate', 'FPFQ', 'OEE']
    
    if verbose == 0:
        print("Yield {}: {:.3f}".format(line, line_yield))
        print("Rate {}: {:.3f}".format(line, line_percent_rate_product))
        if line_percent_fpfq:
            print("FPFQ {}: {:.3f}".format(line, line_percent_fpfq))
        print("OEE {}: {:.3f}".format(line, line_oee))
        print('')
    
    return line_metrics


def data_viewer(data, verbose=0):
    """
    #SITE	LINE	DATE	RUN TIME	UPTIME	FEED (KG)	
    #PRODUCT (KG)	RM YIELD%	THEO YIELD	RM % THEO YIELD	
    #FEED RATE (KG/HR)	PRODUCT RATE (KG/HR)	MAC FEED	
    #MAC PROD	%RATE FEED	%RATE PROD	FPFQ	FPFQ %	OEE% FEED	OEE% PROD
    """
    sites = data['Site'].unique()
    lines = data['Line'].unique()
    metrics = pd.DataFrame()
    for site in sites:
        for line in lines:
            # determine process type
            if data.loc[(data["Line"] == line) & (data["Site"] == site)]["Process Type"].nunique() > 1:
                print("more than one process type determined for line")
                break
            else:
                process_type = data.loc[(data["Line"] == line) & (data["Site"] == site)]["Process Type"].unique()[0]
            
            ###############    moving...
            # calc run_time
            start_end = data.loc[(data["Stream Type"] == "TIME") & (data['Scheduled or Actual'] == "A")]
            ### Calculate Uptime
            uptime = datetime.timedelta(0)
            downtime = downtime_previous = datetime.timedelta(0)
            batches = 0
            for i in range(1,start_end.shape[0]+1,2):
                uptime += start_end.iloc[i]["VALUE"] - start_end.iloc[i-1]["VALUE"]
                batches += 1
                if i < start_end.shape[0]-1:
                    downtime += start_end.iloc[i+1]["VALUE"] - start_end.iloc[i]["VALUE"]
                    downtime_previous = downtime
                    if start_end.iloc[i+1]["VALUE"] - start_end.iloc[i]["VALUE"] < datetime.timedelta(0): #raise/except on overlap
                        print(start_end.iloc[i+1]["VALUE"], start_end.iloc[i]["VALUE"])
            
            ### frac uptime
            percent_uptime = uptime / (uptime + downtime)
            #################
            
            ### runtime and uptime
            if verbose == 0:
                print("site: \t\t\t\t", site)
                print("line: \t\t\t\t", line)
                print("runtime (hr): \t\t\t", np.round(uptime.total_seconds()/60/60,4))
                print("uptime: \t\t\t", np.round(percent_uptime, 4))
                print('')
            
            
            ### for multiple products in process
            if data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A")].groupby("ID", sort=False)["ITEM"].unique()[1].shape[0] > 1:
                product_recipe = data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A")]["ITEM"].unique()[0]
                product = data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A")].groupby("ID", sort=False)["ITEM"].unique()[1]
                metrics = calc_product_metrics(product, data, verbose=verbose)
            ### for single product process
            elif process_type == "C":
                for feed in (data.loc[(data["Stream Type"] == "FEED") & (data["Scheduled or Actual"] == "A")]["ITEM"].unique()):
                    new_metrics = calc_product_metrics([feed], data, stream_designation="FEED", verbose=verbose)
                    metrics = pd.concat([metrics, new_metrics])
            else:
                for product in (data.loc[(data["Stream Type"] == "PRODUCT") & (data["Scheduled or Actual"] == "A")]["ITEM"].unique()):
                    new_metrics = calc_product_metrics([product], data, verbose=verbose)
                    metrics = pd.concat([metrics, new_metrics])
                    
            ### compute line metrics
            line_metrics = calc_line_metrics(metrics, line, verbose=verbose)
            
            return metrics, line_metrics