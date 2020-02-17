from mms.logger.cloud_run_logger import CloudRunLogger


if __name__ == '__main__':

    logger = CloudRunLogger(service_name='th-testservice-new',
                            trace_id='1234',
                            project_id='spielwiese-tobias',
                            revision_version='latese',
                            location='europe-west1',
                            local_run=True)


    logger.error('This is a test error')
    logger.info('This is a test info')

