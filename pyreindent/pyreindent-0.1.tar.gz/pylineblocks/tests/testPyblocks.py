import pyblocks

def testQuoteStatus(qs):
	mappings = [ ( ("   # fdsfs", None), ('   __comment__', None) ),
	             ( ("   dsds ''' ''' # '''", None), ('   dsds __stringLiteral__ __comment__', None) ),
	             ( ("   dsds ''' ''' # '''", "'''"), ('__stringLiteral__ __stringLiteral__', None) ),
	             ( ("   dsds ''' ''' # '''", '"""'), ('__stringLiteral__', '"""') ) ]
	for (line, curQuote), output in mappings:
		try:
			assert(qs(line, curQuote) == output)
		except AssertionError:
			raise AssertionError(f'testQuoteStatus: quote status function couldnt map {(line, curQuote)} -> {output}')

def testSplitIntoBlocks(sib):
	raise NotImplementedError

testQuoteStatus(pyblocks.quoteStatus)
testSplitIntoBlocks(pyblocks.splitIntoBlocks)
