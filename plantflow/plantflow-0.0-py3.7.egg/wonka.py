import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import datetime
from .utils import my_colors
from .analysis import *
from collections import OrderedDict
from scipy.stats import weibull_min
import os

class WonkaSimulator():

    master = None
    
    def create(self, 
               products, 
               days=365, 
               transitions=False, 
               transition_matrix_mu=None, 
               transition_matrix_sigma=None,
               changeover=False, 
               changeover_matrix_mu=None, 
               changeover_matrix_sigma=None,
               mass_balance_percent_qualities=False, 
               mass_balance_other_qualities=False, 
               down_time_events=None):
        """
        Generates production data for a single line
    
        Parameters
        ----------
        products: dictionary
            dictionary containing schedule template for each product
        days: int
            days plant is in operation
        transitions: boolean, default False
            if True will simulate a transition loss in kg of products
            produced as offspec
        transition_matrix_mu: dataframe
            mean transition loss matrix
        transition_matrix_sigma: dataframe
            std transition loss matrix
        changeover: boolean, default False
            if True will simulate a change over loss in mins of downtime
        changeover_matrix_mu: dataframe
            mean changeover loss matrix
        changeover_matrix_sigma: dataframe
            std changeover loss matrix
        mass_balance_percent_qualities: boolean, default False
            if True will normalize QUALITY attribute rows containing
            % in UOM to sum 1
        mass_balance_other_qualities: boolean, default False
            if True will normalize QUALITY attribute rows not containing
            % in UOM to sum to 1
        down_time_events: list, default None
            list of days to simulate a 24 hour downtime

        Returns
        -------
        master: DataFrame
            Simulation outcome file
        """
        event = 0
        prev_var = None
        master = pd.DataFrame()
        var = random.choice(list(products.keys()))
        template = products[var]
        day_one = template["VALUE"][0]
        for i in range(days*3):
            if i > 0:
                var = random.choice(list(products.keys()))
                template = products[var]

            ### calc transition loss in kg
            if transitions: 
                if prev_var:
                    mu_transition_loss = transition_matrix_mu[prev_var][var]
                    sigma_transition_loss = transition_matrix_sigma[prev_var][var]

                    transition_loss = int(np.random.normal(loc = mu_transition_loss,
                                                       scale = sigma_transition_loss * 0.05))
                    if transition_loss < 0:
                        transition_loss = 0
                else:
                    transition_loss = 0
            else: 
                transition_loss = 0

            ### calc changeover in min
            if changeover: 
                if prev_var:
                    mu_changeover_loss = changeover_matrix_mu[prev_var][var]
                    sigma_changeover_loss = changeover_matrix_sigma[prev_var][var]

                    changeover_loss = int(np.random.normal(loc = mu_changeover_loss,
                                                       scale = sigma_changeover_loss * 0.05))
                    if changeover_loss < 0:
                        changeover_loss = 0
                    changeover_mins = datetime.timedelta(minutes = changeover_loss)
                else:
                    changeover_mins = datetime.timedelta(minutes = 0)
            else:
                changeover_mins = datetime.timedelta(minutes = 0)

            prev_var = var # set the previous product state

            ### infer rate from the templates
            time_delta = template.loc[(template["ITEM"] == "END TIME") & (template["Scheduled or Actual"] == "S")]["VALUE"][1] -\
                            template.loc[(template["ITEM"] == "START TIME") & (template["Scheduled or Actual"] == "S")]["VALUE"][0] 
            kg = np.sum(template.loc[(template["Stream Type"] == "FEED") & (template["Scheduled or Actual"] == "S")]["VALUE"])
            kg_hr_rate = kg/time_delta.total_seconds() #total kg/hr rate

            the_feeds = template.loc[(template["Stream Type"] == "FEED") & (template["Scheduled or Actual"] == "S")]["VALUE"].values
            the_products = template.loc[(template["Stream Type"] == "PRODUCT") & (template["Scheduled or Actual"] == "S")]["VALUE"].values
            scheduled = np.concatenate((the_feeds, the_products))

            ### stochastic scheduling
            while True:
                campaign_multiplier = np.round(random.randint(1,10)*random.random(),3) #used to set product/feed ratios
                if campaign_multiplier > 0:
                    break
            campaign = scheduled * campaign_multiplier #first place of stochasity is in scheduling
            total_kg = np.sum(campaign) #total kg processed
            seconds = int(total_kg/kg_hr_rate) #total seconds to run
            process_time = datetime.timedelta(seconds=seconds)

            ### permutate qualities
            new_percents = self._percent_quality(template, sigma=0.05, mass_balance=mass_balance_percent_qualities) #helper functions
            new_others = self._other_quality(template, sigma=0.05, mass_balance=mass_balance_other_qualities) #helper functions

            ### new yields
            new_yields = self._yield_quality(template, campaign=campaign, campaign_multiplier=campaign_multiplier, transition_loss=transition_loss)  #helper functions

            ### new times
            if i == 0:
                new_times = self._time_shift(template, process_time) #if first batch ignore new_start_time  #helper functions
            else:
                new_times = self._time_shift(template, process_time, new_start_time)  #helper functions
            new_entry = pd.concat([new_times, new_yields, new_percents, new_others]).sort_index()


            #### NEED TO FIX CHANGEOVER OCCURANCE?? #####
            if changeover:
                new_start_time = new_times.loc[(new_times["ITEM"] == "END TIME") & (new_times["Scheduled or Actual"] == "A")]["VALUE"].values[0] \
                    + changeover_mins

            else:
                new_start_time = new_times.loc[(new_times["ITEM"] == "END TIME") & (new_times["Scheduled or Actual"] == "A")]["VALUE"].values[0]

            if down_time_events is not None:
                if event < down_time_events.index[-1]:
                    if (new_start_time - day_one).days > min(down_time_events.values[event:]):
                        event += 1
                        new_start_time = new_start_time + datetime.timedelta(days=1)

            new_entry["ID"] = i + 1
            master = pd.concat([master, new_entry])
            template = new_entry
            if (template["VALUE"][0] - day_one).days > days:
                break
        self.master = master


    def _time_shift(self, template, process_time=None, new_start=None):
        """
        helper function for wonka_simulator. Generates new starting times
        for products on the line based on time attributed in the template
    
        Parameters
        ----------
    
        template: DataFrame
            one of the product templates passed in from wonka_generator (see 
            product under wonka_generator)
        process_time: datetime timedelta, default None
            new process_time based on a campaign multiplier (hard coded to
            random integer 1-10 currently) and process rate infered from
            template
        new_start: datetime date, default None
            new_start based on changeover loss, unplanned down time
            in minutes and the previous end time 
        
        Returns
        -------
    
        times: DataFrame
            data frame of the new start/end times for the process
        
        """
        times = template.loc[(template['Attribute Type'] == 'TIME')]
        indeces = times.index
        if not process_time:
            process_time = times.loc[times["Scheduled or Actual"] == "S"]["VALUE"][1] - times.loc[times["Scheduled or Actual"] == "S"]["VALUE"][0]
        if not new_start:
            new_start = times.loc[times["Scheduled or Actual"] == "S"]["VALUE"][0] + process_time
        times["VALUE"][indeces[0]] = new_start
        times["VALUE"][indeces[1]] = new_start + process_time
        times["VALUE"][indeces[2]] = new_start
        times["VALUE"][indeces[3]] = new_start + process_time
        return times


    def _percent_quality(self, template, sigma=0.05, mass_balance=False):
        """
        reads in QUALITY column of PRODUCT with % in UOM label
        with option to mass balance.
    
        Parameters
        ----------
        template: DataFrame
            one of the product templates passed in from wonka_generator (see 
            product under wonka_generator)
        sigma: float, default 0.05
            sigma value to perturb template %QUALITY
        mass_balance: boolean, default False
            whether or not to perform a mass balance around the 
            qualities

        Returns
        -------
        product_breakdown: DataFrame
            new % qualities
        """
        product_breakdown = template.loc[(template['Attribute Type'] == 'QUALITY') & (template['Stream Type'] == 'PRODUCT') & (template['UOM'].str.contains('%'))]
        for i in product_breakdown.index:
            new_value = np.random.normal(loc = product_breakdown['VALUE'][i],
                                         scale = product_breakdown['VALUE'][i]*sigma)
            product_breakdown["VALUE"][i] = new_value
            if mass_balance:
                product_breakdown["VALUE"] = product_breakdown["VALUE"].div(product_breakdown["VALUE"].sum(), axis=0)
        return product_breakdown   


    def _other_quality(self, template, sigma=0.05, mass_balance=False):
        """
        reads in QUALITY column of PRODUCT withOUT % in UOM label
        with option to mass balance.
    
        Parameters
        ----------
        template: DataFrame
            one of the product templates passed in from wonka_generator (see 
            product under wonka_generator)
        sigma: float, default 0.05
            sigma value to perturb template QUALITY
        mass_balance: boolean, default False
            whether or not to perform a mass balance around the 
            qualities

        Returns
        -------
        product_other: DataFrame
            new qualities
        """
        product_other = template.loc[(template['Attribute Type'] == 'QUALITY') & (template['Stream Type'] == 'PRODUCT') & (~template['UOM'].str.contains('%'))]
        for i in product_other.index:
            new_value = np.random.normal(loc = product_other['VALUE'][i],
                                         scale = product_other['VALUE'][i]*sigma)
            product_other["VALUE"][i] = new_value
        if mass_balance:
                product_breakdown["VALUE"] = product_breakdown["VALUE"].div(product_breakdown["VALUE"].sum(), axis=0)
        return product_other   


    def _yield_quality(self, template, sigma=0.05, campaign=None, campaign_multiplier=None, transition_loss=0):
        """
        determines the product yield for wonka_simulator
    
        Parameters
        ----------
        template: DataFrame
            one of the product templates passed in from wonka_generator (see 
            product under wonka_generator)
        sigma: float, default 0.05
            sigma value to perturb template yield
        campaign: float, default None
            total kg of feed processed
        campaign_multiplier: int, default None
            number of campaigns from the template
        transition_loss: float, default 0
            kg lost to offspec material

        Returns
        -------
        overall_yield: DataFrame
            new yields from campaigned/not campaigned
            feeds
        """
        overall_yield = template.loc[(template['Attribute Type'] == 'VOLUME')]
        feeds = overall_yield.loc[(overall_yield['Stream Type'] == "FEED") & (overall_yield["Scheduled or Actual"] == "A")]
        products = overall_yield.loc[((overall_yield['Stream Type'] == "PRODUCT") |
                                      (overall_yield['Stream Type'] == "WASTE")) &
                                    (~overall_yield['Stream Type'].str.contains("OFFSPEC")) &
                                     (overall_yield["Scheduled or Actual"] == "A")]
        offspec = overall_yield.loc[(overall_yield['Stream Type'].str.contains("OFFSPEC"))]
        scheduled = overall_yield.loc[(overall_yield["Stream Type"] == "FEED") | 
                                      (overall_yield["Stream Type"] == "PRODUCT")].loc[overall_yield["Scheduled or Actual"] == "S"]

        #break into three separate loops for feed, not offspec, and offspec, and scheduled
        for index, sub_index in enumerate(scheduled.index):
            if campaign is not None:
                overall_yield["VALUE"][sub_index] = campaign[index]
        for index, sub_index in enumerate(feeds.index):
            if campaign is not None:
                new_value = np.random.normal(loc = overall_yield['VALUE'][sub_index]*campaign_multiplier,
                                             scale = overall_yield['VALUE'][sub_index]*campaign_multiplier*sigma)
                overall_yield["VALUE"][sub_index] = new_value
            else:
                new_value = np.random.normal(loc = overall_yield['VALUE'][sub_index],
                                             scale = overall_yield['VALUE'][sub_index]*sigma)
                overall_yield["VALUE"][sub_index] = new_value
            
        for index, sub_index in enumerate(products.index):
            if sub_index < products.index[-1]:
                if campaign is not None:
                    new_value = np.random.normal(loc = overall_yield['VALUE'][sub_index]*campaign_multiplier,
                                                 scale = overall_yield['VALUE'][sub_index]*campaign_multiplier*sigma)
                    overall_yield["VALUE"][sub_index] = new_value
                elif overall_yield.loc[(overall_yield["ITEM"] == overall_yield["ITEM"][sub_index]) &(overall_yield["Scheduled or Actual"] == "S")].shape[0] != 0:
                    new_value = np.random.normal(loc = overall_yield.loc[(overall_yield["ITEM"] == overall_yield["ITEM"][sub_index]) &\
                                       (overall_yield["Scheduled or Actual"] == "S")]['VALUE'],
                                             scale = overall_yield.loc[(overall_yield["ITEM"] == overall_yield["ITEM"][sub_index]) &\
                                       (overall_yield["Scheduled or Actual"] == "S")]['VALUE']*sigma)[0]
                    overall_yield["VALUE"][sub_index] = new_value
                else:
                    new_value = np.random.normal(loc = overall_yield['VALUE'][sub_index],
                                             scale = overall_yield['VALUE'][sub_index]*sigma)
                    overall_yield["VALUE"][sub_index] = new_value
            else:
                new_value = np.sum(overall_yield.loc[(overall_yield["Stream Type"] == 'FEED') &\
                                                     (overall_yield['Scheduled or Actual'] == 'A')]["VALUE"]) -\
                            np.sum(overall_yield.loc[(overall_yield['Scheduled or Actual'] == 'A') &\
                                                    ~overall_yield.index.isin([sub_index])].loc[~(overall_yield["Stream Type"] == 'FEED') &
                                                    (~overall_yield['Stream Type'].str.contains("OFFSPEC"))]["VALUE"])
            
                overall_yield["VALUE"][sub_index] = new_value
        for index, sub_index in enumerate(offspec.index):
            if campaign is not None:
                new_value = np.random.normal(loc = overall_yield['VALUE'][sub_index]*campaign_multiplier,
                                             scale = overall_yield['VALUE'][sub_index]*campaign_multiplier*sigma)\
                            + transition_loss
            else:
                new_value = np.random.normal(loc = overall_yield['VALUE'][sub_index],
                                             scale = overall_yield['VALUE'][sub_index]*sigma)
                overall_yield["VALUE"][sub_index] = new_value

            overall_yield["VALUE"][sub_index] = new_value
        return overall_yield

    def gen_plots(self, color_variable='AUTO', output_stream_type='PRODUCT', size=(15,5)):
        """
        generates time_series, kde, and downtimes
        in terms of color_variable
    
        Parameters
        ----------
        color_variable: str, default AUTO
            Stream Type by which to designate
            colors. Other options FEED or PRODUCT
        """
        df = self.master
        df.loc[~df["UOM"].isin(['HOUR', 'DATE TIME']), "VALUE"] = pd.to_numeric(df.loc[~df["UOM"].isin(['HOUR', 'DATE TIME'])]["VALUE"], errors='ignore')
        df.loc[df["UOM"].isin(['HOUR', 'DATE TIME']), "VALUE"] = pd.to_datetime(df.loc[df["UOM"].isin(['HOUR', 'DATE TIME'])]["VALUE"])
        if color_variable == "AUTO":
            feeds = df.loc[(df["Stream Type"].isin(["FEED"])) & (df["Scheduled or Actual"] == "A")]["ITEM"].unique()
            products = df.loc[(df["Stream Type"].isin(["PRODUCT"])) & (df["Scheduled or Actual"] == "A")]["ITEM"].unique()
            if len(feeds) > len(products):
                color_variable = "FEED"
            else:
                color_variable = "PRODUCT"
        time_filter_start = min(df.loc[(df["ITEM"] == "START TIME")]["VALUE"])
        time_filter_end = max(df.loc[(df["ITEM"] == "END TIME")]["VALUE"]) #datetime.datetime(2019, 12, 1)
        distinguished = df.loc[df['Stream Type'] == color_variable]["ITEM"].unique()
        fig, ax = plt.subplots(1, 3, figsize=size)
        cols = my_colors()
        downtime_dic = []
        for item in distinguished:
            col = next(cols)

            ### Apply Filters
            ids = df.loc[(df["ITEM"] == item)]["ID"].unique()
            ids_prev = ids - 1
            dff = df.loc[df["ID"].isin(ids)] # filter color_variable
            dff_prev = df.loc[df["ID"].isin(ids_prev)] # filter color_variable


            temp = dff[(dff["ITEM"] == "START TIME") & (dff["Scheduled or Actual"] == "A")]["VALUE"] < time_filter_end # filter by end date
            ids = dff.loc[list(temp.index[temp])]["ID"]
            ids_prev = ids - 1
            dff = dff.loc[dff["ID"].isin(ids)]
            dff_prev = dff_prev.loc[dff_prev["ID"].isin(ids_prev)]

            temp = dff[(dff["ITEM"] == "START TIME") & (dff["Scheduled or Actual"] == "A")]["VALUE"] > time_filter_start # filter by start date
            ids = dff.loc[list(temp.index[temp])]["ID"]
            ids_prev = ids - 1
            dff = dff.loc[dff["ID"].isin(ids)]
            dff_prev = dff_prev.loc[dff_prev["ID"].isin(ids_prev)]

            ### Plot Data
            x1 = pd.to_datetime(dff.loc[(dff["ITEM"] == "START TIME") & (dff["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True))
            x2 = pd.to_datetime(dff.loc[(dff["ITEM"] == "END TIME") & (dff["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True))
            x3 = pd.to_datetime(dff_prev.loc[(dff_prev["ITEM"] == "END TIME") & (dff_prev["Scheduled or Actual"] == "A")]["VALUE"].reset_index(drop=True))
            time = x2 - x1
            if df.iloc[0]["ID"] == dff.iloc[0]["ID"]:
                downtime = x1[1:].reset_index(drop=True) - x3 #no previous for first run in dataframe
            else:
                downtime = x1 - x3
            production = dff.loc[(dff["Stream Type"] == output_stream_type) & (dff["UOM"] == "KG")].groupby("ID")["VALUE"].sum().reset_index(drop=True)
            rate = production.div(time.dt.total_seconds()/60/60)
            try:
                ax_downtime = ax[0].twinx()
                if df.iloc[0]["ID"] == dff.iloc[0]["ID"]:
                    ax_downtime.plot([x3,x1[1:]],[0,0],c=col,linewidth=5)
                else:
                    ax_downtime.plot([x3,x1],[0,0],c=col,linewidth=5)
                ax_downtime.set_ylim(0,1)
                ax_downtime.set_yticks([0,0])
            except:
                print("downtime calc fail for {}".format(item))
                pass
            downtime_dic.append(downtime.sum())
            ax[0].plot([x1,x2],[rate,rate],c=col,label=item)
            ax[0].set_xlim(time_filter_start, time_filter_end)
            ### Set Axes Attributes
            ax[0].set_xlabel("Date")
            ax[0].set_ylabel("Rate (kg/hr)")
            ax[0].set_title("Time Series")
            ax[1].set_title("KDE")
            ax[1].set_xlabel("Rate (kg/hr)")
            rate.plot.kde(ax=ax[1], label=item)

        ddf = pd.DataFrame([i.total_seconds()/60/60/24 for i in downtime_dic], index=[i for i in distinguished]).T
        ddf.plot.bar(ax=ax[2])
        ax[2].set_title("Total Downtime")
        ax[2].set_ylabel("Days")
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())

class DataPrep():
    
    down_days = None
    file = "Wonka"
    
    def generate_events(self, days=365, lam=500, k=5, loc=0, sort='none'):
        """
        inserts unplanned downtime into plant operations 

        Parameters
        ----------
        days: int, default 365
            total days for which plant is simulated
        lam: int, default 500
            scale, characteristic life; eta; hours
        k: float or int, default 5
            shape, type of failure (infant <1, age >1, chance =1); beta
        loc: float or int, default 0
            shift factor
        sort: str, default none
            possible options: ascending, descending, none
        """
        lam_days = lam/24
        n = int(days / lam_days * 1.2) # number of samples
        x = weibull_min.rvs(k, loc=loc, scale=lam, size=n)
        if sort == 'ascending':
            x.sort() #change if wanting to create variability w/ time
        elif sort =='descending':
            x.sort()
            x = np.flip(x)
        down_days = []
        for i, index in enumerate(x):
            down_days.append(np.sum(x[:i]))
        down_days = (pd.DataFrame(down_days)/24)[0].astype(int)
        self.down_days = down_days
        self.x = x
        self.days = days
        self.lam = lam
        self.k = k
        self.loc = loc
    
    def gen_plots(self):
        """
        plots the downtime events/distributions
        """
        fig, axs = plt.subplots(1, 2, figsize=(10,5))
        pdf = make_pdf(weibull_min, (self.k, 0, self.lam))
        pdf.plot(lw=2, ls=':', ax=axs[0], label='weibull')
        pd.DataFrame(self.x, columns=['kde']).plot.kde(ax=axs[0], label='kde')
        plt.legend()
        (self.down_days - self.down_days.shift()).plot(ls='',marker='.', ax=axs[1])
        axs[0].set_title('weilbull and kde')
        axs[0].set_xlabel('time to failure (hrs)')
        axs[1].set_title('time lapse between downtime events')
        axs[1].set_xlabel('event number')
        axs[1].set_ylabel('days between events')
    
    def load_data(self, product='brownies'):
        """
        loads the according datafiles
        
        Parameters
        ----------
        product: str, default brownies
            options are brownies, bars, or liquor
            
        Returns
        ----------
        corresponding datafiles
        """
        file = self.file
        if product == 'brownies':
            brownie = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                 sheet_name='BROWNIES')
            dc_brownie = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='DARK CHOCOLATE BROWNIES')
            almond_brownie = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='ALMOND BROWNIES')
            dc_almond_brownie = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='DARK CHOCOLATE ALMOND BROWNIES')
            brownies = [brownie, dc_brownie, almond_brownie, dc_almond_brownie]
            brownie_dic = {'Brownie': brownie,
                       'DC Brownie': dc_brownie,
                       'Almond Brownie': almond_brownie,
                       'DC Almond Brownie': dc_almond_brownie}

            changeover_matrix_mu = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Brownie Changeover Matrix Mu',
                                             index_col=0)
            changeover_matrix_sigma = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Brownie Changeover Matrix Sigma',
                                             index_col=0)
            transition_matrix_mu = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Brownie Transition Matrix Mu',
                                             index_col=0)
            transition_matrix_sigma = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Brownie Transition Matrix Sigma',
                                             index_col=0)
            self.products = brownie_dic
            self.changeover_matrix_mu = changeover_matrix_mu
            self.changeover_matrix_sigma = changeover_matrix_sigma
            self.transition_matrix_mu = transition_matrix_mu
            self.transition_matrix_sigma = transition_matrix_sigma
        elif product == 'bars':
            mc_bar = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                         sheet_name='MILK CHOCOLATE BAR')
            dc_bar = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='DARK CHOCOLATE BAR')
            mc_almond_bar = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='MILK CHOCOLATE ALMOND BAR')
            dc_almond_bar = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='DARK CHOCOLATE ALMOND BAR')
            bars = [mc_bar, dc_bar, mc_almond_bar, dc_almond_bar]
            bar_dic = {'MC Bar': mc_bar,
                       'DC Bar': dc_bar,
                       'MC Almond Bar': mc_almond_bar,
                       'DC Almond Bar': dc_almond_bar}

            changeover_matrix_mu = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Bars Changeover Matrix Mu',
                                             index_col=0)
            changeover_matrix_sigma = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Bars Changeover Matrix Sigma',
                                             index_col=0)
            transition_matrix_mu = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Bars Transition Matrix Mu',
                                             index_col=0)
            transition_matrix_sigma = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                             sheet_name='Bars Transition Matrix Sigma',
                                             index_col=0)
            self.products = bar_dic
            self.changeover_matrix_mu = changeover_matrix_mu
            self.changeover_matrix_sigma = changeover_matrix_sigma
            self.transition_matrix_mu = transition_matrix_mu
            self.transition_matrix_sigma = transition_matrix_sigma
        elif product == 'liquor':
            cote_divoire = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                         sheet_name="COTE D'IVOIRE")
            ghana = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='GHANA')
            indonesia = pd.read_excel(os.path.join(os.path.dirname(__file__), '../data/{}.xlsx'.format(file)),
                                     sheet_name='INDONESIA')
            liquors = [cote_divoire, ghana, indonesia]
            liquor_dic = {"Cote d'Ivoire": cote_divoire,
                       'Ghana': ghana,
                       'Indonesia': indonesia}
            self.products = liquor_dic