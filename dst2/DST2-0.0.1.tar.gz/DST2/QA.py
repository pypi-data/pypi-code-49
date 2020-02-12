import DST2.SingleColumnValidation as scv #for ISIN,CUSIP,SEDOL, default checks,unique and blanks
import DST2.MultiColumnsValidation as mcv #for Column changes and score changes given delta
import DST2.MultiFilesValidation as mfv #For addition and deletions
import DST2.Reporting as rp #Quality Reporting
import DST2.DescriptiveReporting as dr
from DST2.core_validations import search_columns,build_index,list_intersection,keyword_remove

import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

import warnings
warnings.filterwarnings('ignore')
class QA_Report(object):
    """
    Creating an abstract level of QA
    """
    def __init__(self,deliverable_name,dfOld,dfNew,indexField):
        self.report = rp.Report(str(deliverable_name)+" Quality Report")
        self.indexField = indexField

        self.sheet_counter = 1

        self.dfOld = dfOld.copy()
        self.dfNew = dfNew.copy()
        if type(indexField) is list:
            self.dfOld, self.indexField= build_index(self.dfOld, indexField)  # for Old if index is a list
            self.dfNew, self.indexField = build_index(self.dfNew, indexField)

        #print(self.dfNew.head())
        #Build default analysis
        #Addition, deletions
        del_size, self.deletions, del_perc = mfv.files_comparison(self.dfOld, self.dfNew, self.indexField)
        add_size, self.additions, add_perc = mfv.files_comparison(self.dfNew, self.dfOld, self.indexField)
        self.error_data = pd.DataFrame(columns=['Errors','Column']) #Will hold all errors found on a single column level
        #Perform Default error check on new
        self.error_report = dr.ErrorReport()
        self.percentage_report = dr.PercentageReport()
        self.summary_report = dr.SummaryReport()

        #Perform some Default Summaries
        summary_file_rows = mfv.file_info(self.dfOld,self.dfNew)
        summary_file_cols = mfv.file_columns(self.dfOld,self.dfNew)

        #ADD SUMMARIES TP REPORT
        self.summary_report.add_summary_report('Number of Companies', summary_file_rows)
        self.summary_report.add_summary_report('Number of Columns', summary_file_cols)

        self.percentage_report.add_percentage_report('Additions',add_size,add_perc)
        self.percentage_report.add_percentage_report('Deletions', del_size, del_perc)
        #For ISIN
        is_isin = search_columns('isin',self.dfNew.columns.tolist())
        #self.isin_error_count = 0
        self.isin_report = pd.DataFrame()
        if len(is_isin)>0:
            for isin_col in is_isin:
                isin_error_counts,isin_error_report = scv.isin_check(dfNew[isin_col])
                self.error_report.add_error_report(isin_col,isin_error_counts) #Perform Check
                #Add the report to the isin_report dataframe
                #rename column
                if len(isin_error_report)>0: #if we find an ISIN error

                    isin_error_report = pd.DataFrame(isin_error_report).rename(columns={isin_col:'Errors'})
                    #create a col indicate what column
                    isin_error_report['Column'] = isin_col
                    #Append
                    self.error_data = self.error_data.append(isin_error_report,ignore_index=True)
                else:
                    pass

        else:
            pass

        #For CUSIP
        is_cusip = search_columns('cusip', self.dfNew.columns.tolist())
        self.cusip_report = pd.DataFrame()
        if len(is_cusip)>0:
            for cusip_col in is_cusip:
                cusip_error_counts,cusip_error_report = scv.cusip_check(dfNew[cusip_col])

                self.error_report.add_error_report(cusip_col,cusip_error_counts) #Perform Check
                #Add the report to the isin_report dataframe
                #rename column
                if len(cusip_error_report)>0: #if we find an CUSIP error
                    cusip_error_report = pd.DataFrame(cusip_error_report).rename(columns={cusip_col:'Errors'})

                    #create a col indicate what column
                    cusip_error_report['Column'] = cusip_col
                    #Append
                    self.error_data = self.error_data.append(cusip_error_report,ignore_index=True)
                else:
                    pass

        else:
            pass

        #FOR SEDOLS
        is_sedol = search_columns('sedol', self.dfNew.columns.tolist())
        self.sedol_report = pd.DataFrame()
        if len(is_sedol)>0:
            for sedol_col in is_sedol:
                sedol_error_counts,sedol_error_report = scv.sedol_check(dfNew[sedol_col])
                self.error_report.add_error_report(sedol_col,sedol_error_counts) #Perform Check
                #Add the report to the isin_report dataframe
                #rename column
                if len(sedol_error_report)>0: #if we find an SEDOL error
                    sedol_error_report = pd.DataFrame(sedol_error_report).rename(columns={sedol_col:'Errors'})
                    #create a col indicate what column
                    sedol_error_report['Column'] = sedol_col

                    #Append
                    self.error_data = self.error_data.append(sedol_error_report,ignore_index=True)
                else:
                    pass

        else:
            pass
    def get_comp_name(self,comp_id, rtncol):
        """
        Returns company name in the main file
        :param comp_id: company id
        :param main_df: main dataframe
        :return: a company name
        """
        new_df = self.dfNew[self.dfNew[self.indexField] == str(comp_id)].copy()
        if not new_df.empty:
            return new_df.reset_index().at[0, rtncol]
        else:
            return 'Invalid Company'
    def top_bottom_company_score_changes(self,df):
        """
        Return the top and bottom companies having changes
        :param df: Score dataframes
        :return: 2 dataframes
        """
        new_df = df[(df['Previous']>0)&(df['Current']>0)]
        #Taking the bottom and top
        if len(new_df)>9:
            top_df = new_df.sort_values(by=['delta'],ascending=False).iloc[:10,:]
            bottom_df = new_df.sort_values(by=['delta'],ascending=True).iloc[:10,:]
        else:
            top_df = new_df.sort_values(by=['delta'], ascending=False)
            bottom_df = new_df.sort_values(by=['delta'],ascending=True)



        return  top_df,bottom_df
    def top_10_companies_col_changes(self,df):
        """
        Return top 10 companies with most changes
        :param df: df
        :return: new_df
        """
        #print(df)

        if len(df) > 9:
            new_rep = df.iloc[:, 0].value_counts()[:10].rename_axis(self.indexField).reset_index(name='Counts').copy()

        else:
            #print(df.iloc[:, 0].value_counts())
            #print(self.indexField)
            new_rep = df.iloc[:, 0].value_counts().rename_axis(self.indexField).reset_index(name='Counts').copy()
        try:
            # Get Company name in the report
            name_col = search_columns('name', self.dfNew.columns.tolist())
            new_df = self.dfNew[[self.indexField, name_col[0]]]
            #Convert the type to string
            new_df[self.indexField] = new_df[self.indexField].astype('str')

            # Perform a merge
            new_rep = new_rep.merge(new_df, how='left', on=self.indexField)


            #Rearrange column
            new_rep = new_rep[[self.indexField, name_col[0], 'Counts']]

            #Get all fre

            return new_rep
        except:
            return new_rep
    def perform_qa(self,columns=None,type='column',all_cols = False,delta=5,keywords=None,takeout_keywords=None):
        """
        Perform QA w.r.t type of QA to be performed
        :param columns: Columns
        :param type: 'score'
        :return: DataFrame
        """

        self.sheet_name = ""
        if type =='score' and all_cols is False:
            if keywords is not None:
                new_columns = search_columns(keywords,self.dfNew.columns.tolist())
                old_columns = search_columns(keywords, self.dfOld.columns.tolist())
                main_cols = list_intersection(new_columns,old_columns)
                if isinstance(takeout_keywords,str) and takeout_keywords is not None and len(str(takeout_keywords))>1:
                    #take_out = [takeout_keywords]
                    #main_cols = [col for col in main_cols if str(takeout_keywords).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords,main_cols)
                elif isinstance(takeout_keywords,list) and takeout_keywords is not None and len(takeout_keywords)>0:
                    #main_cols = [col for t in takeout_keywords for col in main_cols if str(t).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                else:
                    pass

                #Get a unqiue column set of columns
                size, data_report, change_perc = mcv.scores_comparison(self.dfOld, self.dfNew,main_cols, self.indexField,
                                                                       delta=delta)
                self.percentage_report.add_percentage_report('Report ' + str(self.sheet_counter) + ' -S.Score Changes',
                                                             size, change_perc)
                # Sheetname
                self.sheet_name = 'Report ' + str(self.sheet_counter) + ' -S.Score Changes'
                # Get score with previous score but now no score or 0
                no_score_df = data_report[(data_report['Previous'] > 0) & (data_report['Current'] == 0)].copy()
                new_score_df = data_report[(data_report['Previous'] == 0) & (data_report['Current'] > 0)].copy()
                # Get top and bottom companies
                top_companies, bottom_companies = self.top_bottom_company_score_changes(data_report)
                # Create sheets
                top_c = rp.Sheet(self.sheet_name, top_companies, start_col=9)
                bottom_c = rp.Sheet(self.sheet_name, bottom_companies, start_row=len(top_companies) + 3, start_col=9)
                no_score_sheet = rp.Sheet(self.sheet_name, no_score_df, start_col=17)
                new_score_sheet = rp.Sheet(self.sheet_name, new_score_df, start_col=25)

                # Add to percentage report
                try:
                    self.percentage_report.add_percentage_report('Previous BUT No Current', len(no_score_df),
                                                                 (len(no_score_df) / size) * 100)
                    self.percentage_report.add_percentage_report('Current BUT No Previous', len(new_score_df),
                                                                 (len(new_score_df) / size) * 100)
                except:
                    self.percentage_report.add_percentage_report('Previous BUT No Current', len(no_score_df),
                                                                 0)
                    self.percentage_report.add_percentage_report('Current BUT No Previous', len(new_score_df),
                                                                 0)

                # Sheets
                self.sheet_counter = self.sheet_counter + 1
                self.sheet = rp.Sheet(self.sheet_name, data_report)
                self.report.add_to_report(self.sheet)
                # Add the top and bottom to report
                self.report.add_to_report(top_c)
                self.report.add_to_report(bottom_c)
                self.report.add_to_report(no_score_sheet)
                self.report.add_to_report(new_score_sheet)

            else:
                #To get the first intersection
                inter1 = list_intersection(columns,self.dfOld.columns.tolist())
                inter2 = list_intersection(columns,self.dfNew.columns.tolist())
                main_cols = list_intersection(inter1,inter2)
                if isinstance(takeout_keywords,str) and takeout_keywords is not None and len(str(takeout_keywords))>1:
                    #take_out = [takeout_keywords]
                    #main_cols = [col for col in main_cols if str(takeout_keywords).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                elif isinstance(takeout_keywords,list) and takeout_keywords is not None and len(takeout_keywords)>0:
                    #main_cols = [col for t in takeout_keywords for col in main_cols if str(t).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                else:
                    pass
                if len(main_cols)>0:

                    size, data_report, change_perc = mcv.scores_comparison(self.dfOld, self.dfNew, main_cols, self.indexField,delta=delta)
                    #Add percentage
                    self.percentage_report.add_percentage_report('Report '+str(self.sheet_counter)+' - Score Changes',size,change_perc)
                    #Sheetname
                    self.sheet_name = 'Report '+str(self.sheet_counter)+' - Score Changes'
                    #Get score with previous score but now no score or 0
                    no_score_df = data_report[(data_report['Previous']>0)&(data_report['Current']==0)].copy()
                    new_score_df = data_report[(data_report['Previous']== 0) & (data_report['Current'] > 0)].copy()
                    #Get top and bottom companies
                    top_companies,bottom_companies = self.top_bottom_company_score_changes(data_report)
                    #Create sheets
                    top_c = rp.Sheet(self.sheet_name, top_companies, start_col=9)
                    bottom_c = rp.Sheet(self.sheet_name, bottom_companies,start_row=len(top_companies)+3,start_col=9)
                    no_score_sheet = rp.Sheet(self.sheet_name,no_score_df,start_col=17)
                    new_score_sheet = rp.Sheet(self.sheet_name, new_score_df, start_col=25)

                    #Add to percentage report
                    self.percentage_report.add_percentage_report('Previous BUT No Current',len(no_score_df),(len(no_score_df)/size)*100)
                    self.percentage_report.add_percentage_report('Current BUT No Previous', len(new_score_df),
                                                                 (len(new_score_df) / size) * 100)


                    #Sheets
                    self.sheet_counter = self.sheet_counter + 1
                    self.sheet = rp.Sheet(self.sheet_name, data_report)
                    self.report.add_to_report(self.sheet)
                    #Add the top and bottom to report
                    self.report.add_to_report(top_c)
                    self.report.add_to_report(bottom_c)
                    self.report.add_to_report(no_score_sheet)
                    self.report.add_to_report(new_score_sheet)
                else:
                    pass


        elif type=='column' and all_cols is False:
            if keywords is not None:
                new_columns = search_columns(keywords, self.dfNew.columns.tolist())
                old_columns = search_columns(keywords, self.dfOld.columns.tolist())
                main_cols = list_intersection(new_columns, old_columns)

                if isinstance(takeout_keywords,str) and takeout_keywords is not None and len(str(takeout_keywords))>1:
                    #take_out = [takeout_keywords]
                    #main_cols = [col for col in main_cols if str(takeout_keywords).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                elif isinstance(takeout_keywords,list) and takeout_keywords is not None and len(takeout_keywords)>0:
                    #main_cols = [col for t in takeout_keywords for col in main_cols if str(t).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                else:
                    pass
                if len(main_cols)>0:

                    size, data_report, change_perc, _ = mcv.columns_comparison(self.dfOld, self.dfNew, main_cols,
                                                                               self.indexField)
                    self.percentage_report.add_percentage_report('Report ' + str(self.sheet_counter) + ' - S.Column Changes',
                                                                 size, change_perc)
                    # Sheetname
                    self.sheet_name = 'Report' + str(self.sheet_counter) + ' -S.Column Changes'
                    self.sheet_counter = self.sheet_counter + 1
                    self.sheet = rp.Sheet(self.sheet_name, data_report)
                    # Prepare vi data for column information
                    viz_col_data_1 = self.top_10_companies_col_changes(data_report)
                    # Add this viz
                    top_10 = rp.Sheet(self.sheet_name, viz_col_data_1, start_col=9)

                    self.report.add_to_report(self.sheet)
                    self.report.add_to_report(top_10)
                else:
                    pass
            else:
                inter1 = list_intersection(columns, self.dfOld.columns.tolist())
                inter2 = list_intersection(columns, self.dfNew.columns.tolist())
                main_cols = list_intersection(inter1, inter2)
                if isinstance(takeout_keywords,str) and takeout_keywords is not None and len(str(takeout_keywords))>1:
                    #take_out = [takeout_keywords]
                    #main_cols = [col for col in main_cols if str(takeout_keywords).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                elif isinstance(takeout_keywords,list) and takeout_keywords is not None and len(takeout_keywords)>0:
                    #main_cols = [col for t in takeout_keywords for col in main_cols if str(t).lower() not in str(col).lower()]
                    main_cols = keyword_remove(takeout_keywords, main_cols)
                else:
                    pass
                if len(main_cols)>0:
                    size, data_report, change_perc, _ = mcv.columns_comparison(self.dfOld, self.dfNew, main_cols, self.indexField)
                    self.percentage_report.add_percentage_report('Report '+str(self.sheet_counter)+' - Column Changes', size, change_perc)
                    # Sheetname
                    self.sheet_name = 'Report '+str(self.sheet_counter)+' - Column Changes'
                    self.sheet_counter = self.sheet_counter + 1
                    self.sheet = rp.Sheet(self.sheet_name, data_report)
                    #Prepare vi data for column information
                    viz_col_data_1 = self.top_10_companies_col_changes(data_report)
                    #Add this viz
                    top_10 = rp.Sheet(self.sheet_name,viz_col_data_1,start_col= 9)

                    self.report.add_to_report(self.sheet)
                    self.report.add_to_report(top_10)
                else:
                    pass

            viz_col_data_2 = None


        else:#Exception to be added
            #Get index of the column
            if isinstance(self.indexField,str):
                #idx_indexField = self.dfNew.columns.tolist().index(self.indexField)
                cols_new = [col for col in self.dfNew.columns.tolist() if col != self.indexField ]
                cols_old = [col for col in self.dfOld.columns.tolist() if col != self.indexField ]
                main_cols = list_intersection(cols_new,cols_old)
            else:
                cols_new = self.dfNew.columns.tolist()
                cols_old = self.dfOld.columns.tolist()
                main_cols = list_intersection(cols_new,cols_old)

            if isinstance(takeout_keywords, str) and takeout_keywords is not None and len(str(takeout_keywords)) > 1:
                # take_out = [takeout_keywords]
                #main_cols = [col for col in main_cols if str(takeout_keywords).lower() not in str(col).lower()]
                main_cols = keyword_remove(takeout_keywords, main_cols)
            elif isinstance(takeout_keywords, list) and takeout_keywords is not None and len(takeout_keywords) > 0:
                main_cols = keyword_remove(takeout_keywords, main_cols)
                #main_cols = [col for t in takeout_keywords for col in main_cols if
                 #            str(t).lower() not in str(col).lower()]
            else:
                pass

            if len(main_cols)>0:

                #print(cols)
                size, data_report, change_perc, _ = mcv.columns_comparison(self.dfOld, self.dfNew,main_cols , self.indexField)
                self.percentage_report.add_percentage_report('All Cols Changes', size, change_perc)
                # Sheetname
                self.sheet_name = 'All Column Changes'
                #ADD TO REPORT
                # Prepare vi data for column information
                viz_col_data_1 = self.top_10_companies_col_changes(data_report)
                # Add this viz
                top_10 = rp.Sheet(self.sheet_name, viz_col_data_1, start_col=10)
                self.sheet = rp.Sheet(self.sheet_name,data_report)
                self.report.add_to_report(self.sheet)
                self.report.add_to_report(top_10)
            else:
                pass

        #Build Visualization



        #Default Analysis Analysis Performed
        #Build Summary on this report
    def perform_column_qa(self,column,type='comparison'):
        """
        Perform Special QA for a column and provide a summary check, perform blanks check and summary report
        :param column: any column, CAN BE USED FOR SCREENING column
        :return: Dataframe
        """
        #Get the type of a column
        if type=='comparison':

            if is_string_dtype(self.dfNew[column]) and is_string_dtype(self.dfOld[column]):
                special_col = mcv.summary_categorical_comparison(self.dfOld[column],self.dfNew[column])
                self.summary_report.add_summary_report(column, special_col)
            else: #Perform a general
                special_col = mcv.summary_general_comparison(self.dfOld[column], self.dfNew[column])
                self.summary_report.add_summary_report(column, special_col)
        #elif type=='dupilcates':

            #Get the comparison type
        else:
            pass
    def create_report(self):
        """
        Check for all available reports
        :return: Create excel outputs
        """
        #Add descriptive statistics to Report
        summary = self.summary_report.get_summary_report()
        summary_sheet = rp.Sheet("Overall Summary",summary)
        self.report.add_to_report(summary_sheet)

        #Adding Percentage to reports
        percentage_summary = self.percentage_report.get_percentage_report()
        percentage_sheet = rp.Sheet('Overall Summary',percentage_summary,start_col=5)
        self.report.add_to_report(percentage_sheet)



        #Adding Errors to Report
        error_summary = self.error_report.get_error_report()
        try:

            if len(error_summary) > 0:
                error_sheet = rp.Sheet('Overall Summary', error_summary, start_col=9)
                error_data_sheet = rp.Sheet('Overall Summary',self.error_data,start_col=12)
                #Add error to report
                if len(error_summary)>0:
                    self.report.add_to_report(error_sheet)
                if len(self.error_data)>0:
                    self.report.add_to_report(error_data_sheet)
        except:
            pass


        #Create reports for Addition and Deletions
        if len(self.additions)>0:
            add_sheet = rp.Sheet("Additions", self.additions)
            self.report.add_to_report(add_sheet)
        if len(self.deletions)>0:
            del_sheet = rp.Sheet("Deletions", self.deletions)
            self.report.add_to_report(del_sheet)

        #Save Report
        self.report.save_report()

