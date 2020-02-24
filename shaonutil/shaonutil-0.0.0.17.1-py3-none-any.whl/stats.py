"""Statistics"""
def counter(li,number):
	num = 0
	for c in li:
		if c == number:
			num += 1
	return num

def occurance_dic(li):
	dic = {}
	for number in li:
		dic[number] = counter(li,number)
	return dic

def mean(li):
	"""Avearage or mean of elements - shaonutil.stats.mean(list of numbers)"""
	return sum(li)/len(li)

def median(li):
	"""Median of elements - shaonutil.stats.median(list of numbers)"""
	n = len(li) 
	li.sort() 

	if n % 2 == 0: 
		median1 = li[n//2] 
		median2 = li[n//2 - 1] 
		median = (median1 + median2)/2
	else: 
		median = li[n//2] 

	return median

def mode(li):
	"""Mode of elements - shaonutil.stats.mode(list of numbers)"""
	n = len(li)
	data = occurance_dic(li)
	mode = [k for k, v in data.items() if v == max(list(data.values()))] 
	  
	if len(mode) == n: 
	    raise ValueError('No mode found !')
	else:
	    return mode


if __name__ == '__main__':
	pass