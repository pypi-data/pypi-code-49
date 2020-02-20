from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

from .input_validator import input_validator

@input_validator(dict)
def get_text_blocks(textract_response):
	"""
	Get all text blocks in a Textract response.
	|
	| Argument: dict (JSON-parsed Textract Response)
	|
	| Output: list[string]
	"""
	text_block_list = []

	if "Blocks" not in textract_response:
		logger.error("textract_util.parser.get_text_blocks: invalid input") 
		return text_block_list
	
	for block in textract_response["Blocks"]:
		if block.get("BlockType", "") == "LINE":
			if "Text" in block: 
				text_block_list.append(block["Text"])

	return text_block_list

@input_validator(dict)
def get_text(textract_response):
	"""
	Get text in a Textract response.
	|
	| Argument: dict (JSON-parsed Textract Response)
	|
	| Output: string
	"""
	return " ".join(get_text_blocks(textract_response))

@input_validator(dict)
def get_text_blocks_by_row(textract_response):
	"""
	Get text blocks by row in in a Textract response.
	|
	| Argument: dict (JSON-parsed Textract Response)
	|
	| Output: list[list[string]]
	"""
	text_block_list_by_row = []
	if "Blocks" not in textract_response:
		logger.error("textract_util.parser.get_text_blocks_by_row: invalid input") 
		return text_block_list_by_row

	cur_left, cur_row = 0, []
	for block in textract_response["Blocks"]:
		block_left = block.get("Geometry", {}).get("BoundingBox", {}).get("Left", None)
		block_type = block.get("BlockType", "")
		block_text = block.get("Text", "")
		if block_left is None: continue
		elif block_left < cur_left:
			text_block_list_by_row.append(cur_row)
			cur_left, cur_row = block_left, [block_text]
		else:
			cur_left = block_left
			cur_row.append(block_text)

	if cur_row: text_block_list_by_row.append(cur_row)

	return [list(filter(lambda x: x!= "", row)) for row in text_block_list_by_row]

@input_validator(dict)
def get_text_by_row(textract_response):
	"""
	Get text by row in in a Textract response.
	|
	| Argument: dict (JSON-parsed Textract Response)
	|
	| Output: list[string]
	"""
	return [" ".join(row) for row in get_text_blocks_by_row(textract_response)]







	