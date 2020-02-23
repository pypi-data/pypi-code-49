extraction_fields = [
						'label',
						'regex', 
						'match_number_from', 
						'match_number_to', 
						'filter',
						'clean_html_tags'
					]

class Extraction:

	# Use slots to save memory and prevent invalid values
	__slots__ = extraction_fields

	def __init__(self, extraction_data={}):
		# create attributes for every valid name
		for key, value in extraction_data.items():
			if key in extraction_fields:
				setattr(self, key, value)

	# Create a dictable version of attributes to allow use of slots and vars()
	@property
	def __dict__(self):
		return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}