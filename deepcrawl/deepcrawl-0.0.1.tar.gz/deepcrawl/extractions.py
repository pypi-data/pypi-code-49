class DeepCrawlExtraction:

	def __init__(self, extraction_data):
		
		self.label = extraction_data['label']
		self.regex = extraction_data['regex']
		self.match_number_from = extraction_data['match_number_from']
		self.match_number_to = extraction_data['match_number_to']
		if 'filter' in extraction_data:
			self.filter = extraction_data['filter']
		else:
			self.filter = ''

		if 'clean_html_tags' in extraction_data:
			self.clean_html_tags = extraction_data['clean_html_tags']
		else:
			self.clean_html_tags = False