#!/usr/bin/env python3
# coding: utf-8

import sqlite3
import pandas as pd

from multiprocessing import Pool
from napoleontoolbox.features import features_type
from napoleontoolbox.file_saver import dropbox_file_saver
from napoleontoolbox.neural_net import lrs_type
from napoleontoolbox.neural_net import activations


class ParalleLauncher():
    def __init__(self,drop_token='', dropbox_backup=True, local_root_directory='../data',user='napoleon',  db_path_suffix = '_run.sqlite', meta_features_types=[features_type.FeaturesType.STANDARD_ADVANCED], meta_layers=[[2048,1024,512,256,128,64,32]], convolutions=[0], activations=[activations.ActivationsType.LEAK_0SUB_0MAX0], meta_n=[126], meta_seeds=[0], epochss=[1], ss=[21], meta_n_past_features=[21], utilities=['f_drawdown'], meta_lrs_types = [lrs_type.LrType.CONSTANT],meta_lrs = [0.01],lower_bounds=[0.02],upper_bounds=[0.4], meta_normalize=[True]):
        # print('Epochs ' + str(epochss))
        # print('Seed ' + str(meta_seeds))
        # print('Training period size ' + str(meta_n))
        # print('Neural net layout ' + str(meta_layers))
        # print('Stationarize ' + str(meta_stationarize))
        # print('Normalize ' + str(meta_normalize))
        # print('Advanced ' + str(meta_advance_features))
        # print('Signals ' + str(meta_advance_signals))
        # print('History ' + str(meta_history))
        # print('Normalized ' + str(meta_normalize))
        # print('Rebalancing ' + str(ss))
        # print('Activation ' + str(activations))
        # print('Convolution' + str(convolutions))
        # print('Utility' + str(utilities))
        # print('n past features ' + str(meta_n_past_features))
        # print('Rebalancing ' + str(ss))
        self.args = []
        self.counter = 1

        for n_past_features in meta_n_past_features:
            for convolution in convolutions:
                for activation in activations:
                    for s in ss:
                        for epochs in epochss:
                            for feature_type in meta_features_types:
                                for seed in meta_seeds:
                                    for layers in meta_layers:
                                        for n in meta_n:
                                            for low_bound in lower_bounds:
                                                for up_bound in upper_bounds:
                                                    for normalize in meta_normalize:
                                                        for lrs_type in meta_lrs_types:
                                                            for lr in meta_lrs:
                                                                for utility in utilities:
                                                                    self.args.append((self,seed, utility, layers, epochs,
                                                                                 n_past_features, n, s, feature_type,
                                                                                 activation, convolution,lr, lrs_type, low_bound, up_bound, normalize))
                                                                    self.counter = self.counter + 1
        self.args.sort()
        self.local_root_directory = local_root_directory
        self.user = user
        self.db_path_suffix = db_path_suffix
        self.filename =  user + db_path_suffix
        self.db_path = self.local_root_directory + self.filename
        self.runs = []
        self.totalRow = 0
        self.instantiateTable()
        self.empty_runs_to_investigate = []
        self.dbx = dropbox_file_saver.NaPoleonDropboxConnector(drop_token=drop_token,dropbox_backup=dropbox_backup)

    def launchParallelPool(self, toRun, use_num_cpu):
        with Pool(processes=use_num_cpu) as pool:
            results = pool.starmap(toRun, self.args)
            print('parallel computation done')

    def launchSequential(self, toRun):
        results=[]
        for meArg in self.args:
            predicted_weights = toRun(*meArg)
            results.append(predicted_weights)
        return results

    def instantiateTable(self):
        sqliteConnection = None
        try:
            sqliteConnection = sqlite3.connect(self.db_path)
            sqlite_create_table_query = '''CREATE TABLE parallel_run (
                                        effective_date date PRIMARY KEY);'''
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")
            cursor.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")

    def addRun(self,run):
        sqliteConnection = None
        try:
            sqliteConnection = sqlite3.connect(self.db_path)
            sqlite_create_table_query = 'alter table parallel_run add column ' + run + ' real'
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")
            cursor.close()
            self.runs.append(run)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")  # adding the column

    def insertResults(self, run, values):
        sqliteConnection = None
        try:
            success = True
            sqliteConnection = sqlite3.connect(self.db_path)
            cursor = sqliteConnection.cursor()
            for i, v in values.iteritems():
                sqlite_insert_query = """INSERT INTO 'parallel_run' ('effective_date', '""" + run + """') VALUES ('""" + str(
                    i) + """','""" + str(v) + """');"""
                cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
            success = False
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The Sqlite connection is closed")
        return success

    def updateResults(self, run, values):
        sqliteConnection = None
        try:
            sqliteConnection = sqlite3.connect(self.db_path)
            cursor = sqliteConnection.cursor()
            for i, v in values.iteritems():
                sqlite_update_query = """UPDATE 'parallel_run' set '""" + run + """' = '""" + str(
                    v) + """' where effective_date = '""" + str(i) + """'"""
                cursor.execute(sqlite_update_query)
            sqliteConnection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The Sqlite connection is closed")


    def addRunWeights(self,run, weights_df):
        sqliteConnection = None
        try:
            table_name = run + '_weight'
            sqliteConnection = sqlite3.connect(self.db_path)
            weights_df.columns = [col.replace(' ','_') for col in weights_df.columns]
            weights_df.to_sql(name=table_name, con=sqliteConnection)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")

    def addRunWeightsPrediction(self,run, string_date, weights_df):
        sqliteConnection = None
        try:
            table_name = run +'_'+string_date+ '_weight_prediction'
            sqliteConnection = sqlite3.connect(self.db_path)
            weights_df.columns = [col.replace(' ','_') for col in weights_df.columns]
            weights_df.to_sql(name=table_name, con=sqliteConnection)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")


    def addRunRecordings(self,run, recordings_df):
        sqliteConnection = None
        try:
            table_name = run + '_recording'
            sqliteConnection = sqlite3.connect(self.db_path)
            recordings_df.to_sql(name=table_name, con=sqliteConnection)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")


    def addRunActivationsFollowUp(self, run, activations_df):
        sqliteConnection = None
        try:
            table_name = run + '_activation'
            sqliteConnection = sqlite3.connect(self.db_path)
            activations_df.to_sql(name=table_name, con=sqliteConnection)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")

    def addResults(self, run, values):
        success = self.insertResults(run,values)
        if not success :
            self.updateResults(run, values)


    def saveResults(self, run, values, weights_df, recordings_df, activations_df, last_predicted_weights_df):
        self.addRun(run)
        self.addResults(run, values)
        self.totalRow = self.datesCount()
        self.addRunWeights(run, weights_df)
        self.addRunWeightsPrediction(run,last_predicted_weights_df.columns[0], last_predicted_weights_df)
        self.addRunRecordings(run, recordings_df)
        self.addRunActivationsFollowUp(run, activations_df)

    def checkRunExistence(self,run):
        sqliteConnection = None
        runExistence=None
        try:
            sqliteConnection = sqlite3.connect(self.db_path)
            sqlite_select_run_query = 'SELECT effective_date,'+run + ' FROM parallel_run'
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_select_run_query)
            sqliteConnection.commit()
            print("SQLite table created")
            cursor.close()
            runExistence = True
        except sqlite3.Error as error:
            print("The run is not present", error)
            runExistence = False
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")  # adding the column
        return runExistence

    def datesCount(self):
        sqliteConnection = None
        try:
            sqliteConnection = sqlite3.connect(self.db_path, timeout=20)
            cursor = sqliteConnection.cursor()
            sqlite_select_query = """SELECT count(*) from parallel_run"""
            cursor.execute(sqlite_select_query)
            totalRows = cursor.fetchone()
            print("Total rows are:  ", totalRows)
            cursor.close()
            return totalRows
        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The Sqlite connection is closed")



    def upload_results_to_dropbox(self):
        print('uploading to dropbox the results '+self.db_path)
        self.dbx.uploadFileToDropbox(filename=self.filename,fullpath = self.db_path)
