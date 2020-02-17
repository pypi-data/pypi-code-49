# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:52:14 2019

@author: stasb
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import multiprocessing
import sys, os, time#, csv
from datetime import datetime, timedelta
import itertools

class mp:
    def __init__(self, workname, 
                 do_calc=None, 
                 do_save=None,
                 workfolder=None,
                 infolder=None,
                 outfolder=None):
        '''
        Parameters
        ----------
        
        workname : str
            Name of work to be done. Will be used in folder names
            if they aren't specified.
            
        do_calc : function(job, folder)
            User function that made calculations
            
        do_save : function(item, folder)
            User function that save results
        
        folder : str
            Work folder
        '''
        if workname in (None, ''):
            self.workname = 'test_work'
        else:
            self.workname = workname
            
        self.set_funcs(do_calc, do_save)
        self.set_folders(workfolder, infolder, outfolder)

        self.log_path = os.path.join(self.workfolder, self.workname+'_log.csv')
        self.jobs_path = os.path.join(self.workfolder, self.workname+'_jobs.pkl')
        self.error_path = os.path.join(self.workfolder, self.workname+'_error.csv')
        
        self.jobs = mp.read_jobs(self.jobs_path)
        self.log = mp.read_log(self.log_path)
       
    def read_jobs(path):
        return pd.read_pickle(path) if os.path.exists(path) else None
    
    def read_log(path):
        '''
        Reads LOG file
        '''
        
        if os.path.exists(path):
            df = pd.read_csv(path, parse_dates=['datetime'], 
                             infer_datetime_format=True)
            df.drop_duplicates(subset=['hash', 'status'], 
                               keep='last', inplace=True)
            df = df.pivot(index='hash', columns='status', values='datetime')

            # in case when there are no records for some status
            for col in ['start', 'done', 'fail']:
                if col not in df.columns:
                    df[col] = pd.NaT # pandas datetime NaN
            return df

        return None
    
    def set_funcs(self, do_calc, do_save):
        self.do_calc = do_calc
        self.do_save = do_save
        return self
        
    def set_folders(self, workfolder=None, infolder=None, outfolder=None):
        if workfolder in (None, ''):
            self.workfolder = os.path.join(os.getcwd(), self.workname)
        else:
            self.workfolder = workfolder

        if infolder in (None, ''):
            self.infolder = self.workfolder
        else:
            self.infolder = infolder

        if outfolder in (None, ''):
            self.outfolder = self.workfolder
        else:
            self.outfolder = outfolder

        for fldr in [self.workfolder, self.outfolder]:
            if not os.path.exists(fldr):
                os.mkdir(fldr)
        return self
        

    def get_job_table(self, reload_log=False):
        if reload_log:
            self.log = mp.read_log(self.log_path)
            
        if self.jobs is not None:
            if self.log is not None:
                df = pd.merge(self.jobs, self.log, on='hash', how='left')
            else:
                df = self.jobs.copy()
                df['start'] = pd.NaT
                df['done'] = pd.NaT
                df['fail'] = pd.NaT
            done_mask = df.done.notna()
            fail_mask = df.fail.notna()
            df['dt'] = pd.Timedelta(0)
            df.loc[done_mask, 'dt'] = pd.to_timedelta(df['done']-df['start'])
            df.loc[fail_mask, 'dt'] = pd.to_timedelta(df['fail']-df['start'])
            df['seconds'] = df['dt'].dt.total_seconds()
            return df
        return None
    
    def get_remaining_jobs(self, exclude_failed=False):
        df = self.get_job_table()

        if df is not None:
            if exclude_failed:
                mask = df.done.isna()
            else:
                mask = df.done.isna() & df.fail.isna()
            
            return self.jobs[mask]
        return None

    def run(self, p=2, run_async=False):
        '''
        Run parallel multiprocessed calculation.
        '''
        if self.do_calc is None or self.do_save is None:
            raise RuntimeError("do_calc or do_save wasn't specified")
        
        jobs = self.get_remaining_jobs()
        
        if jobs is None:
            raise RuntimeError("Jobs table is empty")
        
        self.manager = multiprocessing.Manager()
        self.queue = self.manager.Queue()
        self.pool = multiprocessing.Pool(processes=p+1)
        
        print('<<< pool of %d workers on %d jobs started >>>'%(p, len(jobs)), flush=True)
        print('<<< use [ctrl+c] to terminate processes >>>', flush=True)
        
        self.pool.apply_async(mp.save_proxy, 
                              args=(len(jobs),
                                    self.do_save,
                                    self.queue, 
                                    self.log_path, 
                                    self.error_path,
                                    self.outfolder))
        todo_jobs = [{'job':job,
                      'do_calc':self.do_calc,
                      'folder':self.infolder,
                      'q':self.queue} for job in jobs.to_dict(orient='records')]
        if run_async:
            self.pool.map_async(mp.calc_proxy, todo_jobs)
        else:
            self.pool.map(mp.calc_proxy, todo_jobs)
        self.pool.close()
        self.pool.join()

    def debug_run(self, job=None):
        '''
        Run calculation and saving for specified job in main process
        for debug and testing.
        '''        
        if job is None:
            job = self.get_remaining_jobs().iloc[0].to_dict()
            
        print('<<< single process run on job %r >>>'%(job,), flush=True)
        t0 = datetime.now()
        
        mp.append_csv(self.log_path,[datetime.now(), job['hash'], 'start'])        
        res = self.do_calc(job, self.infolder)
        
        if res is None:
            mp.append_csv(self.log_path,[datetime.now(), job['hash'], 'fail'])
        else:
            item = {'job':job, 'res':res}
            self.do_save(item, self.outfolder)
            mp.append_csv(self.log_path,[datetime.now(), job['hash'], 'done'])        

        dt = datetime.now()-t0
        mp.print_stat(dt, 0, 1)
        print('<<< single process run finished >>>', flush=True)

    def create_hash(df):
        '''
        Create HASH column for each job
        '''    
        df['hash'] = pd.util.hash_pandas_object(df, index=False).apply(hex)
        #df.hash.apply(int, args=(0,))
        return df

    def generate_jobs(**kwdata):
        '''
        Make Cartesian product of iterables from kwdata
        '''
        df = pd.DataFrame(list(itertools.product(*kwdata.values())), columns=kwdata.keys())
        #cols = ['hash']+list(df.columns)        
        #return df.reindex(cols, axis=1)        
        return mp.create_hash(df)
               
    def append_csv(path, lst, sep=','):
        '''
        Append jobs to csv file.
        '''
#        if not os.path.exists(path):
#            with open(path, 'w') as f: #, newline=''
#                print('datetime','hash','status', sep=sep, file=f)
            
        with open(path, 'a') as f: #, newline=''
            print(*lst, sep=sep, file=f)
#            f.write(sep.join(map(str, lst))+'\n')
    
    def update_todo_jobs(self, jobs):
        '''
        Main method to add jobs in TODO file.
        '''
        if isinstance(jobs, dict):
            jobs = mp.generate_jobs(**jobs)
        
        if not isinstance(jobs, pd.DataFrame):
            raise TypeError("jobs should be pandas DataFrame")
        
        if 'hash' not in jobs.columns:
            jobs = mp.create_hash(jobs)
        
        if self.jobs is None:
            self.jobs = jobs
        elif set(self.jobs.columns) == set(jobs.columns):
            self.jobs = self.jobs.append(jobs)
            self.jobs.drop_duplicates(subset=['hash'], inplace=True)
        
#        self.jobs.to_csv(self.jobs_path, index=False)
        self.jobs.to_pickle(self.jobs_path)
        
        return self

    def reset_done_jobs(self):
        '''
        When you need recalculate all jobs use this method to remove
        DONE file with done jobs.
        '''
        if self.log is not None:
            mask = self.log.done.notna()
            self.log.loc[mask, ['start', 'done']] = pd.NaT
        return self

    def reset_failed_jobs(self):
        '''
        When you need recalculate all jobs use this method to remove
        failed jobs from log
        '''
        if self.log is not None:
            mask = self.log.fail.notna()
            self.log.loc[mask, ['start', 'fail']] = pd.NaT
        return self
        
    def get_failed_jobs(self):
        '''
        Uses FAILED file to retrieve failed jobs. 
        '''
        df = self.get_job_table()
        if df is not None:
            mask = df.fail.notna()
            return self.jobs[mask]
        return None
        
    def dt_to_string(dt):
        '''
            dt : timedelta
        '''
        return '%02d:%02d:%02d:%02d.%03d'%(*pd.Timedelta(dt).components,)[:5]
    
    def now_string():
        return mp.dt_to_string(datetime.now())
    
    def print_stat(dt, est_count, done_count):
        '''
        Print average time per job, estimated time of arrival,
        finish datetime.
        '''
        if done_count == 0:
            return
        name = (' LAST %d '%done_count).center(32,'-')
        avg = dt.total_seconds()/done_count
        eta = timedelta(seconds=avg*est_count)
        fin = datetime.now()+eta
        
        print(name+'\n',
              '< AVG: %.2fs >\n'%avg,
              '< ETA: %s >\n'%mp.dt_to_string(eta),
              '< FIN: %s >\n'%fin.strftime('%d-%b-%Y %H:%M:%S'),
              '-'*32, sep='', flush=True)
        
        
    def plot_cpu_time(df, kind='done', ax=None, **plot_kw):
        if ax is None:
            _, ax = plt.subplots()

        mask = df.done.notna() if kind == 'done' else df.fail.notna()
        kw = {'ls':'', 'marker':'.', 'zorder':0}
        kw.update(plot_kw)

        df.loc[mask].plot(kind='line',
                          x='start', y='seconds', 
                          ax=ax, **kw)
        
        plt.setp(ax.xaxis.get_majorticklabels(), 
                 rotation=90, va='bottom', ha='left', zorder=20)
        ax.tick_params(axis='x', which='major', pad=-10)
        
        ax.set_ylabel('Job time, s')
#        ax.set_title('Work <%s> progress (ETA: %s)'%(workname, str(tmax + mjt*to_be_done_count)[:-10]))
    
    def hist_cpu_time(df, ax=None,
                      show=('cpu_mean', 'done_mean'), 
                      line_kw=({'ls':'--'}, {'ls':'-.'}), 
                      **hist_kw):
        if ax is None:
            _, ax = plt.subplots()
        kw = {'orientation':'horizontal'}
        kw.update(hist_kw)
        orientation = kw['orientation']
        
        ax.hist(df[df.done.notna()].seconds, **kw) # hist
        
        def show_line(ax, fmt, val, orientation, **line_kw):
            kw = {'color':'k', 'ls':'--', 'lw':1}
            kw.update(line_kw)
            if orientation == 'horizontal':
                ax.axhline(val, **kw, label=fmt%val)
#                ax.annotate(fmt%val, (0.5, val),
#                            xycoords=('axes fraction','data'),
#                            ha='center', va='center')
            else:
                ax.axvline(val, **kw, label=fmt%val)
#                ax.annotate(fmt%val, (val, 0.5),
#                            xycoords=('data','axes fraction'),
#                            ha='center', va='center', rotation=90)
        
        cpu_mean = df.seconds.mean()
        ddf = df[df.done.notna()]
        done_mean = 0 if ddf.shape[0]==0 else (ddf.done.max()-ddf.start.min())/ddf.shape[0]/np.timedelta64(1, 's')
        ddf = df[df.seconds.notna()]
        job_mean = 0 if ddf.shape[0]==0 else (ddf.done.max()-ddf.start.min())/ddf.shape[0]/np.timedelta64(1, 's')
        
        data_map = {'cpu_mean':('CPU mean\n%.2f', cpu_mean),
                   'done_mean':('Done mean\n%.2f', done_mean),
                   'job_mean':('Job mean\n%.2f', job_mean)
                   }
        
        for i, s in enumerate(show):
            if s in data_map:
                show_line(ax, *data_map[s], orientation, **line_kw[i])
                                        
        if orientation == 'horizontal':
            ax.set_ylabel('CPU time, s')
            ax.set_xlabel('Jobs count')
        else:
            ax.set_xlabel('CPU time, s')
            ax.set_ylabel('Jobs count')
            
        ax.set_title('Job CPU time')
        ax.legend()
    
    def plot_job_map(df, x='x', y='y', kind='done',
                     ax=None, cax=None, **map_kw):
        if ax is None or cax is None:
            _, (ax, cax) = plt.subplots(1, 2)

        start_mask = df.start.notna()
        done_mask = df.done.notna()
        fail_mask = df.fail.notna()
        
        if kind == 'done':
            mask = start_mask & done_mask
        elif kind == 'fail':
            mask = start_mask & fail_mask
            
        M = pd.DataFrame(0., index=df[y].unique(), columns=df[x].unique())
        C = df[mask].pivot(index=y, columns=x, values='seconds')
        
        kw = {'origin':'lower'}
        kw.update(map_kw)
        h = ax.imshow(M+C, **kw)
        plt.colorbar(h, cax=cax)
        cax.set_ylabel('Job CPU time, s')
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title('Job map (%s/all): %d/%d'%(kind,
                     done_mask.sum() if kind=='done' else fail_mask.sum(),
                     df.shape[0]))
        
    def plot_stat(self, reload_log=False, x='x', y='y', 
                  fig_kw={'figsize':(10,10)}):

        df = self.get_job_table(reload_log)
        
        if df is None:
            return

        fig = plt.figure(**fig_kw)
        
        widths = [0.15, 0.81, 0.04]
        heights = [0.25, 0.75]
        
        gs = fig.add_gridspec(ncols=3,nrows=2,
                              width_ratios=widths,
                              height_ratios=heights)
        
        axh = fig.add_subplot(gs[1:,0]) # histogram
        axp = fig.add_subplot(gs[0,:]) # plot
        axm = fig.add_subplot(gs[1:,1:-1]) # color map
        cax = fig.add_subplot(gs[1:,-1]) # color bar
        
        mp.hist_cpu_time(df, ax=axh)
        mp.plot_cpu_time(df, ax=axp)
        mp.plot_job_map(df,x=x, y=y, ax=axm, cax=cax)
        
        done_mask = df.done.notna()
        ddf = df[done_mask]
        tmin = ddf.start.min()
        tmax = ddf.done.max()
        mjt = (tmax-tmin)/done_mask.sum() # mean job time
        to_be_done_mask = df.done.isna() & df.fail.isna()

        axp.set_title('Work <%s> progress (ETA: %s)'%(self.workname, 
                      str(tmax + mjt*to_be_done_mask.sum())[:-10]))

        fig.tight_layout()
        
        
#    def plot_stat(self, records='all', reload_log=True,
#                  hist_kw={'bins':20, 'color':'mediumseagreen', 'height':0.1, 'alpha':0.5},
#                  bars_kw={'color':'slateblue', 'alpha':0.5},
#                  map_kw={'cmap':'autumn'},
#                  fig_kw={'figsize':(10,10)}):
#        df = self.get_job_table(reload_log)
#        
#        if df is None:
#            return
#        
#        if isinstance(records, int) and records > 0:
#            df = df.tail(records)
#          
#        done_mask = df.done.notna()
#        fail_mask = df.fail.notna()
#        start_mask = df.start.notna()
#        to_be_done_mask = df.done.isna() & df.fail.isna()
#            
#        done_count = (done_mask & start_mask).sum()
#        to_be_done_count = to_be_done_mask.sum()
#
#        fail_count = (fail_mask & start_mask).sum()
#        
#        df['dt'] = pd.to_datetime(df['done']-df['start'])
#        df['seconds'] = df['dt'].dt.total_seconds()
#        
#        ddf = df[df['seconds'].notna()]
#        tmin = ddf.start.min()
#        tmax = ddf.done.max()
#        
#        print('Jobs count (all/done/fail): %s/%s/%s'%(df.shape[0], done_count, fail_count))
#        print('Mean job CPU time:', mp.dt_to_string(ddf.dt.mean()))
#        mjt = (tmax-tmin)/done_count
#        print('Mean job time:', mp.dt_to_string(mjt))
#        print('ETA:', tmax + mjt*to_be_done_count)
#        
##        import matplotlib
##        matplotlib.use('Qt5Agg')
#        
#        fig = plt.figure(**fig_kw)
#        
#        widths = [0.15, 0.81, 0.04]
#        heights = [0.25, 0.75]
#        
#        gs = fig.add_gridspec(ncols=3,nrows=2,
#                              width_ratios=widths,
#                              height_ratios=heights)
#        
#        axh = fig.add_subplot(gs[1:,0]) # histogram
#        axp = fig.add_subplot(gs[0,:]) # plot
#        axc = fig.add_subplot(gs[1:,1:-1]) # color map
#        axb = fig.add_subplot(gs[1:,-1]) # color bar
#
#        # histogram        
#        axh.hist(ddf['seconds'], orientation='horizontal', **hist_kw)
#        cpu_mean = ddf.dt.mean().total_seconds()
#        axh.axhline(cpu_mean, color='k', ls='--', lw=1)
#        axh.annotate('Mean CPU\n%.2f'%cpu_mean, (0.5, cpu_mean),
#                     xycoords=('axes fraction','data'), ha='center', va='center')
#        job_mean = mjt/np.timedelta64(1, 's')
#        axh.axhline(job_mean, color='k', ls='--', lw=1)
#        axh.annotate('Mean job\n%.2f'%job_mean, (0.5, job_mean),
#                     xycoords=('axes fraction','data'), ha='center', va='center')
#        axh.set_ylabel('CPU time, s')
#        axh.set_xlabel('Jobs count')
#        axh.set_title('Job CPU time')
#        
#        # bar plot
#        x_col = 'done'
#        y_col = 'seconds'
#        #df.plot(y=y_col, x=x_col, ax=axp) #ls='', marker='+', color='k',        
#        x = dates.datestr2num(df.loc[done_mask, x_col].apply(str))
#
#        bkw = {'width':0.000005, 'zorder':20}
#        bkw.update(bars_kw)
#        axp.bar(x, df.loc[done_mask, y_col], **bkw)
#        
#        day_locator = dates.DayLocator(interval=1)
#        minute10_locator = dates.MinuteLocator(interval=10)
#        day_formatter = dates.DateFormatter('%Y-%m-%d')
#        minute10_formatter = dates.DateFormatter('%H:%M')
#        
#        axp.xaxis.set_major_locator(day_locator)
#        axp.xaxis.set_major_formatter(day_formatter)
#
#        axp.xaxis.set_minor_locator(minute10_locator)
#        axp.xaxis.set_minor_formatter(minute10_formatter)
#        
#        #axp.tick_params(axis='x', rotation=90)#, horizontalalignment='right')
#        #axp.xaxis.set_tick_params(which='major', rotation=90, labelleft=True)
#        #axp.xaxis.set_tick_params(which='major', rotation=90)
#        plt.setp(axp.xaxis.get_majorticklabels(), 
#                 rotation=90, va='bottom', ha='left')
#        axp.tick_params(axis='x', which='major', pad=-10)
#
#        axp.set_ylabel('Job time, s')
#        axp.set_title('Work <%s> progress (ETA: %s)'%(self.workname, str(tmax + mjt*to_be_done_count)[:-10]))
#        axp.grid(True, color='k', zorder=10, alpha=0.5)
#
#        # job map        
#        C = df.pivot(columns='x', index='y', values='seconds')
#        h = axc.imshow(C, **map_kw)
#        plt.colorbar(h, cax=axb)
#        axb.set_ylabel('Job CPU time, s')
#        
#        # jobs in progress
#        in_progress = df.loc[start_mask & df.done.isna() & df.fail.isna()]
#        if in_progress.shape[0] > 0:
#            axc.plot(in_progress['x'],
#                     in_progress['y'],
#                     ls='', marker='o',
#                     markersize=10,
#                     markerfacecolor='none',
#                     markeredgecolor='k')
#        
#        # failed jobs
#        failed_jobs = df.loc[start_mask & df.fail.notna()]
#        if failed_jobs.shape[0] > 0:
#            axc.plot(failed_jobs['x'],
#                     failed_jobs['y'],
#                     ls='', marker='x',
#                     markersize=10,
#                     markerfacecolor='none',
#                     markeredgecolor='k')
#            
#        axc.set_xlabel('x')
#        axc.set_ylabel('y')
#        axc.set_title('Job map (all-done-fail): %d-%d-%d'%(df.shape[0], done_count, fail_count))
#        fig.tight_layout()
#        plt.show()        
                
    def save_proxy(N, do_save, queue, log_path, error_path, outfolder):
        '''
        This function acts in separate process and saves calculated 
        results from queue.
        '''
        t0 = datetime.now()
        t10 = t0
        i = 0
        if not os.path.exists(log_path):
            with open(log_path, 'w') as f: #, newline=''
                print('datetime','hash','status', sep=',', file=f)
        
        while i < N:
            if queue.empty():
                time.sleep(0.1)
            else:
                try:
                    item = queue.get()
                    status = item['status']
                    job = item['job']
                    job_dt = item['datetime']
    #                mp.append_csv(log_path,[datetime.now(), item])
    #                i += 1
                    mp.append_csv(log_path,[job_dt, job['hash'], status])
    #                
                    if status == 'done':
                        print('< SAVE #%d/%d >'%(i,N), flush=True)
                        do_save(item, outfolder)
                        i += 1
                    elif status == 'fail':
                        i += 1
    
                    if i%10 == 0:
                        dt = datetime.now()-t0
                        mp.print_stat(dt,N-i,i)
                        dt10 = datetime.now()-t10
                        t10 = datetime.now()
                        if i > 10:
                            mp.print_stat(dt10,N-i,10)
                except BaseException as e:
                    mp.append_csv(error_path,[datetime.now(), item, e])
        # finishing
        dt = datetime.now()-t0
        mp.print_stat(dt,N-i,i)
        print('<<< pool finished working on %d jobs >>>'%(N), flush=True)
        
    def calc_proxy(arg):
        '''
        This function is wrapper around do_calc user function.
        Runs in multiple processes, calls do_calc, work on exceptions.
        '''
        job = arg['job']
        do_calc = arg['do_calc']
        queue = arg['q']
        
#        log_path = arg['log_path']
        print('< CALC:', job, '>', flush=True)
        t0 = datetime.now()
        queue.put({'job':job, 'datetime':t0, 'status':'start'})
        try:
            res = do_calc(job, arg['folder'])
        except BaseException as e:
            print('< EXCEPTION: %r >'%e, flush=True)
            res = None
        finally:
            now = datetime.now()
            t = now - t0
            print('< JOB %r DONE >\n< CPU: %.2fs >'%(job,t.total_seconds()), 
                  flush=True)
            if res is None:
                queue.put({'job':job, 'datetime':now, 'status':'fail'})
            else:
                queue.put({'job':job, 'res':res, 'datetime':now, 'status':'done'})
        pass
        
    def test_calc(job, folder):
        # actual calculation work will be done here!
        time.sleep(np.random.randint(1,5))
        #if np.random.randint(1,4) > 2:
        #    raise RuntimeError('Calculation error')
        res = job['x']*job['y']
        return res
    
    def test_save(item, folder):
        # results will be saved here
        print('Saving result: ', item['res'], 
              'of job:', item['job'],
              'into folder', folder, flush=True)
        pass
    
if __name__ == '__main__':
    jobs = mp.generate_jobs(x = list(range(5)), y = list(range(5))[::-1])
    m = mp('mp_test_work', do_calc=mp.test_calc, do_save=mp.test_save)
#    m.plot_stat()
    m.update_todo_jobs(jobs).reset_failed_jobs()
#    m.debug_run()
    m.run(p=2)
