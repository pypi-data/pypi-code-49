import pandas as pd
import tarfile
from datahen import Scrapers, ScraperJobs, Exports
from tqdm import tqdm
import requests

class Pandas:    
  @classmethod
  def get_recent_export(self, scraper_name, exporter_name):
    
    recent_jobs = ScraperJobs.get_recent_jobs(scraper_name)
    recent_job = next(x for x in recent_jobs if x['status'] == 'done')

    recent_exports = Exports.get_recent_exports(scraper_name)
    recent_export = next(x for x in recent_exports if x['status'] == 'done' and x['job_id'] == recent_job['id'] and x['exporter_name'] == exporter_name)
    recent_export_url = Exports.get_download_url_by_export_id(recent_export['id'])

    archive_response = requests.get(recent_export_url, stream=True)
    archive_file_path = f"/tmp/{recent_export['file_name']}"

    total_size = int(archive_response.headers.get('content-length', 0))
    block_size = 1024

    t = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(archive_file_path, 'wb') as f:
      for data in archive_response.iter_content(block_size):
        t.update(len(data))
        f.write(data)
    t.close()

    if total_size != 0 and t.n != total_size:
      raise EnvironmentError("Something went wrong")

    tar = tarfile.open(archive_file_path)
    export_file_tar_path = tar.getnames()[-1]
    tar.extractall("/tmp")
    export_file_path = f"/tmp/{export_file_tar_path}"

    # TODO: json exporter case
    df = pd.read_csv(export_file_path)

    return df

  @classmethod
  def get_current_job_history(self, scraper_name):
    
    job_history = ScraperJobs.get_current_job_history(scraper_name)
    df = pd.DataFrame(job_history)

    df['time_stamp'] = df['time_stamp'].astype('datetime64[ns]') 
    df.set_index('time_stamp', inplace=True)

    return df