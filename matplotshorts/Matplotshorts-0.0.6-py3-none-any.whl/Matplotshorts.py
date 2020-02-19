import matplotlib.pyplot as plt

def grid_display(list_of_images, list_of_titles=[], no_of_columns=2, figsize=(10,10)):
	fig = plt.figure(figsize=figsize)
	column = 0
	for i in range(len(list_of_images)):
		column += 1
		#  check for end of column and create a new figure
		if column == no_of_columns+1:
			fig = plt.figure(figsize=figsize)
			column = 1
		fig.add_subplot(1, no_of_columns, column)
		plt.imshow(list_of_images[i])
		plt.axis('off')
		if len(list_of_titles) >= len(list_of_images):
			plt.title(list_of_titles[i])
	plt.show()
    
