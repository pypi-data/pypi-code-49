

def api_endpoint(endpoint, **kwargs):

	dc_account_url = 'https://api.deepcrawl.com/accounts/'

	if endpoint == 'session':
		return 'https://api.deepcrawl.com/sessions'

	if endpoint == 'projects':
		return dc_account_url + str(kwargs['account_id']) + '/projects'

	if endpoint == 'project':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id'])

	if endpoint == 'majestic':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/majestic_configuration'

	if endpoint == 'issues':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/issues'

	if endpoint == 'issue':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/issues/' + str(kwargs['issue_id'])

	if endpoint == 'crawls':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/crawls'

	if endpoint == 'reports':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/crawls/' + str(kwargs['crawl_id']) + '/reports'

	if endpoint == 'report_rows':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/crawls/' + str(kwargs['crawl_id']) + '/reports/' + str(kwargs['report_id']) + '/report_rows'

	if endpoint == 'report_generate':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/crawls/' + str(kwargs['crawl_id']) + '/reports/' + str(kwargs['report_id']) + '/downloads'

	if endpoint == 'report_download':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/crawls/' + str(kwargs['crawl_id']) + '/reports/' + str(kwargs['report_id']) + '/downloads/' + str(kwargs['report_download_id'])

	if endpoint == 'crawl_schedules':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/schedules'

	if endpoint == 'crawl_schedule':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/schedules/' + str(kwargs['schedule_id'])

	if endpoint == 'report_trend':
		return dc_account_url + str(kwargs['account_id']) + '/projects/' + str(kwargs['project_id']) + '/crawls/' + str(kwargs['crawl_id']) + '/reports/' + str(kwargs['report_id']) + '/statistics/report_trend'

	print('endpoint not recognised')