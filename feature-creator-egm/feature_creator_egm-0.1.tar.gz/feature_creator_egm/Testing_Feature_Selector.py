from FeatureSelector import FeatureSelector
from feature_creator_egm import SimpleFeatureSelector


""" Testing FeatureSelector
"""
fs = FeatureSelector(0.30,"english")
text = fs.read_file("Test_Text_English.txt")
fs.prepare_word_array(text)


print(text)

print(" ".join(fs.words).join("\n\n"))

word_dict = fs.frequency_dictionary()

print(fs.word_dictionary)

selected_words = fs.feature_selection(0.30)
for word in selected_words:
    print(word)

""" Testing SimpleFeatureSelector
"""
sfs = SimpleFeatureSelector(15,45,'spanish')
text = sfs.read_file("Test_Text_Spanish.txt")
sfs.prepare_word_array(text)
print(" ".join(sfs.words).join("\n\n"))
sfs.frequency_dictionary()
print(sfs.word_dictionary)
selected_words = sfs.feature_selection()
for word in selected_words:
    print(word)
