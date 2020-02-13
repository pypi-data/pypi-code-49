import os
import pickle

# Map country_code:country_name
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       'country_code_iso_alpha2.pickle'), mode='rb') as pickle_file:
    country_code_iso_alpha2_map = pickle.load(pickle_file)
