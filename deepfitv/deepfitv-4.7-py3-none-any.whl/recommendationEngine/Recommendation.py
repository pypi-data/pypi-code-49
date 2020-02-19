#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd #Analysis 
import matplotlib.pyplot as plt #Visulization
import seaborn as sns #Visulization
import numpy as np #Analysis 
from scipy.stats import norm #Analysis 
from sklearn.preprocessing import StandardScaler #Analysis 
from scipy import stats #Analysis 
import warnings 
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')
import gc

import os
import string
color = sns.color_palette()

get_ipython().run_line_magic('matplotlib', 'inline')

from plotly import tools
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go

from sklearn import model_selection, preprocessing, metrics, ensemble, naive_bayes, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD
import lightgbm as lgb

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999


# ## 1. Exploration Data Analysis
# 
# ### 1.1. Data understanding
# 
# 
# First we will import Train data and Test data. The sizes of the two data are as follows:
# 
# It was data from https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29 and crawled reviews from online pharmaceutical review sites.

# In[ ]:


import os


# In[ ]:


df_train = pd.read_csv("drugsComTrain_raw.csv", parse_dates=["date"])
df_test = pd.read_csv("drugsComTest_raw.csv", parse_dates=["date"])


# In[ ]:


print("Train shape :" ,df_train.shape)
print("Test shape :", df_test.shape)


# This is the result of looking at the data through the head () command. There are six variables except for the unique ID that identifies the individual, and review is the key variable.

# In[ ]:


df_train.head()


# These are additional explanations for variables.
# 
# - drugName (categorical): name of drug 
# - condition (categorical): name of condition
# - review (text): patient review 
# - rating (numerical): 10 star patient rating 
# - date (date): date of review entry 
# - usefulCount (numerical): number of users who found review useful
# 
# The structure of the data is that a patient with a unique ID purchases a drug that meets his condition and writes a review and rating for the drug he/she purchased on the date. Afterwards, if the others read that review and find it helpful, they will click usefulCount, which will add 1 for the variable.

# ### 1.2. Data understanding
# 
# First, we will start exploring variables, starting from uniqueID. We compared the unique number of unique IDs and the length of the train data to see if the same customer has written multiple reviews, and there weren't more than one reviews for one customer.

# In[ ]:


print("unique values count of train : " ,len(set(df_train['uniqueID'].values)))
print("length of train : " ,df_train.shape[0])


# DrugName is closely related to condition, so we have analyzed them together. The unique values of the two variables are 3671 and 917, respectively, and there are about 4 drugs for each condition. Let's go ahead and visualize this in more detail.

# In[ ]:


df_all = pd.concat([df_train,df_test])
df_all.head()


# In[ ]:


condition_dn = df_all.groupby(['condition'])['drugName'].nunique().sort_values(ascending=False)
condition_dn[0:20].plot(kind="bar", figsize = (14,6), fontsize = 10,color="green")
plt.xlabel("", fontsize = 20)
plt.ylabel("", fontsize = 20)
plt.title("Top20 : The number of drugs per condition.", fontsize = 20)


# As you can see from the picture above, the number of drugs for top eight conditions is about 100 for each condition. On the other hand, it should be noted that the phrase "3</span> users found this comment helpful" appears in the condition, which seems like an error in the crawling process. I have looked into it to see in more details.

# In[ ]:


df_all[df_all['condition']=='3</span> users found this comment helpful.'].head(3)


# It is expected that for structure of '</ span> users found this comment helpful.' phrase, there will be not only 3, but also 4 as shown above, and other numbers as well. We will remove these data in the future preprocessing.
# 
# The following are the low 20 conditions of 'drugs per condition'. As you can see, the number is all 1. Considering the recommendation system, it is not feasible to recommend with that when there is only one product. Therefore, we will analyze only the conditions that have at least 2 drugs per condition.

# In[ ]:


condition_dn = df_all.groupby(['condition'])['drugName'].nunique().sort_values(ascending=False)

condition_dn[condition_dn.shape[0]-20:condition_dn.shape[0]].plot(kind="bar", figsize = (14,6), fontsize = 10,color="green")
plt.xlabel("", fontsize = 20)
plt.ylabel("", fontsize = 20)
plt.title("Bottom20 : The number of drugs per condition.", fontsize = 20)


# Next, let's have a look at the review. First, noticeable parts are the html strings like \ r \ n, and the parts that express emotions in parentheses such as (very unusual for him) and (a good thing) and words in capital letters like MUCH.

# In[ ]:


df_train['review'][1]


# In addition, there were some words with errors like didn&# 039;t for didn't, and also characters like ...

# In[ ]:


df_train['review'][2]


# We will delete these parts in preprocessing as well.

# Next, we will classify 1 ~ 5 as negative, and 6 ~ 10 as positive, and we will check through 1 ~ 4 grams which corpus best classifies emotions.

# In[ ]:


from collections import defaultdict
df_all_6_10 = df_all[df_all["rating"]>5]
df_all_1_5 = df_all[df_all["rating"]<6]


# In[ ]:


import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stops = set(stopwords.words('english'))


# In[ ]:


df_all["usefulCount"].describe()


# If you look at the distribution of usefulCount, you can see that the difference between minimum and maximum is 1291, which is high. In addition, the deviation is huge, which is 36. The reason for this is that the more drugs people look for, the more people read the review no matter their contents are good or bad, which makes the usefulcount very high. So when we create the model, we will normalize it by conditions, considering people's accessibility.

# ### 1.3 Missing value

# In[ ]:


percent = (df_all.isnull().sum()).sort_values(ascending=False)
percent.plot(kind="bar", figsize = (14,6), fontsize = 10, color='green')
plt.xlabel("Columns", fontsize = 20)
plt.ylabel("", fontsize = 20)
plt.title("Total Missing Value ", fontsize = 20)


# In[ ]:


print("Missing value (%):", 1200/df_all.shape[0] *100)


# We will delete because the percentage is lower than 1%.

# ## 2. Date Preprocessing

# ### 2.1. Missing Values Removal

# In[ ]:


df_train = df_train.dropna(axis=0)
df_test = df_test.dropna(axis=0)


# In[ ]:


df_all = pd.concat([df_train,df_test]).reset_index()
del df_all['index']
percent = (df_all.isnull().sum()).sort_values(ascending=False)
percent.plot(kind="bar", figsize = (14,6), fontsize = 10, color='green')
plt.xlabel("Columns", fontsize = 20)
plt.ylabel("", fontsize = 20)
plt.title("Total Missing Value ", fontsize = 20)


# ### 2.2 Condition Preprocessing

# We will delete the sentences with the form above.

# In[ ]:


all_list = set(df_all.index)
span_list = []
for i,j in enumerate(df_all['condition']):
    if '</span>' in j:
        span_list.append(i)


# In[ ]:


new_idx = all_list.difference(set(span_list))
df_all = df_all.iloc[list(new_idx)].reset_index()
del df_all['index']


# Next, we will delete conditions with only one drug.

# In[ ]:


df_condition = df_all.groupby(['condition'])['drugName'].nunique().sort_values(ascending=False)
df_condition = pd.DataFrame(df_condition).reset_index()
df_condition.tail(20)


# In[ ]:


df_condition_1 = df_condition[df_condition['drugName']==1].reset_index()
df_condition_1['condition'][0:10]


# In[ ]:


all_list = set(df_all.index)
condition_list = []
for i,j in enumerate(df_all['condition']):
    for c in list(df_condition_1['condition']):
        if j == c:
            condition_list.append(i)
            
new_idx = all_list.difference(set(condition_list))
df_all = df_all.iloc[list(new_idx)].reset_index()
del df_all['index']


# ### 2.3 Review Preprocessing

# In[ ]:


from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


# - \r\n : we need to convert html grammer
# - ... , &#039; : deal with not alphabet

# In[ ]:


stops = set(stopwords.words('english'))
#stops


# In[ ]:


not_stop = ["aren't","couldn't","didn't","doesn't","don't","hadn't","hasn't","haven't","isn't","mightn't","mustn't","needn't","no","nor","not","shan't","shouldn't","wasn't","weren't","wouldn't"]
for i in not_stop:
    stops.remove(i)


# In[ ]:


from sklearn import model_selection, preprocessing, metrics, ensemble, naive_bayes, linear_model
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD
import lightgbm as lgb

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
from sklearn import metrics

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation, CuDNNGRU, Conv1D
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers


# In[ ]:


stemmer = SnowballStemmer('english')

def review_to_words(raw_review):
    # 1. Delete HTML 
    review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    # 2. Make a space
    letters_only = re.sub('[^a-zA-Z]', ' ', review_text)
    # 3. lower letters
    words = letters_only.lower().split()
    # 5. Stopwords 
    meaningful_words = [w for w in words if not w in stops]
    # 6. Stemming
    stemming_words = [stemmer.stem(w) for w in meaningful_words]
    # 7. space join words
    return( ' '.join(stemming_words))


# In[ ]:


get_ipython().run_line_magic('time', "df_all['review_clean'] = df_all['review'].apply(review_to_words)")


# ## 3. Model

# ### 3.1. Deep Learning Model Using N-gram

# In[ ]:


# Make a rating
df_all['sentiment'] = df_all["rating"].apply(lambda x: 1 if x > 5 else 0)


# In[ ]:


df_train, df_test = train_test_split(df_all, test_size=0.33, random_state=42) 


# In[ ]:


df_train


# In[ ]:



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

vectorizer = CountVectorizer(analyzer = 'word', 
                             tokenizer = None,
                             preprocessor = None, 
                             stop_words = None, 
                             min_df = 2, 
                             ngram_range=(4, 4),
                             max_features = 20000
                            )
vectorizer


# In[ ]:



pipeline = Pipeline([
    ('vect', vectorizer),
])


# In[ ]:


get_ipython().run_line_magic('time', "train_data_features = pipeline.fit_transform(df_train['review_clean'])")
get_ipython().run_line_magic('time', "test_data_features = pipeline.fit_transform(df_test['review_clean'])")


# In[ ]:


all_features=pipeline.fit_transform(df_all['review_clean'])


# In[ ]:


from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Bidirectional, LSTM, BatchNormalization, Dropout
from tensorflow.python.keras.preprocessing.sequence import pad_sequences


# In[ ]:



# 0. Package
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense
import random

# 1. Dataset
y_train = df_train['sentiment']
y_test = df_test['sentiment']
solution = y_test.copy()

# 2. Model Structure
model = keras.models.Sequential()

model.add(keras.layers.Dense(200, input_shape=(20000,)))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.Dropout(0.5))

model.add(keras.layers.Dense(300))
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.Dropout(0.5))

model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(1, activation='sigmoid'))

# 3. Model compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[ ]:


model.summary()


# In[ ]:


train_data_features


# In[ ]:


y_train


# In[ ]:


# 4. Train model
hist = model.fit(train_data_features, y_train, epochs=10, batch_size=64)

# 5. Traing process
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.set_ylim([0.0, 1.0])
acc_ax.set_ylim([0.0, 1.0])

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show()


# In[ ]:


# 6. Evaluation
loss_and_metrics = model.evaluate(test_data_features, y_test, batch_size=32)
print('loss_and_metrics : ' + str(loss_and_metrics))


# In[ ]:


sub_preds_deep = model.predict(all_features,batch_size=32)


# In[ ]:


df_all['deep_pred'] = sub_preds_deep


# In[ ]:


df_all.to_csv('final.csv')


# In[ ]:



df_all = df_all.groupby(['condition','drugName']).agg({'deep_pred' : ['mean']})
df_all


# In[ ]:


if df_test['condition'] == df['condition']:
     


# In[ ]:


import pandas as pd
df_all_r = pd.read_csv('final.csv')


# In[ ]:


df_all_r


# In[ ]:





# In[ ]:


df_all_r = df_all_r.groupby(['Unnamed: 0','Unnamed: 1']).agg({'deep_pred' : ['mean']})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 4. Result

# Our team set the topic as recommending the right medicine for the patient's condition with reviews and proceeded the project according to the topic with the data exploration, data preprocessing and modeling. In the data exploration section, we looked at the forms of data using visualization techniques and statistical techniques. The next step was to preprocess the data according to the topic we set, such as removing the condition that has only one drug for recommendation. In the process of modeling, we used deep learning model with n-gram.These steps allowed us to calculate the final predicted value and recommend the appropriate drug for each condition according to the order of the value.

# ## 5. Limitations

# In conclusion, these are the limitations we had during the project.
# 
# 1. Sentiment analysis using sentiment word dictionary has low reliability when the number of positive and negative words is small. For example, if there are 0 positive words and 1 negative word, it is classified as negative. Therefore, if the number of sentiment words is 5 or less, we could exclude the observations.
# 2. To ensure the reliability of the predicted values, we normalized usefulCount and multiplied it to the predicted values. However, usefulCount may tend to be higher for older reviews as the number of cumulated site visitors increases. Therefore, we should have also considered time when normalizing usefulCount.
# 
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


import pandas as pd
df_all_r = pd.read_csv('final.csv')


# In[2]:


df_all_r


# In[3]:


df = df_all_r.iloc[2:]


# In[4]:


df.head()


# In[5]:


df.columns = ['condition','drugName','deep_pred']


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df['deep_pred'] = df['deep_pred'].astype(str).astype(float)


# In[9]:


df.dtypes


# In[10]:


df


# In[11]:


df_all = df.groupby(['condition','drugName']).agg({'deep_pred' : ['mean']})


# In[16]:


df = df.reset_index(drop=True)


# In[18]:


user_input = pd.DataFrame(df.iloc[10])


# In[19]:


user_input = user_input.T.reset_index(drop=True)


# In[20]:


user_input


# In[21]:


recommended_drugs = []


# In[22]:


for i in range(len(df)):
    if df['condition'][i] == user_input['condition'][0] and df['deep_pred'][i] >= user_input['deep_pred'][0] :
        recommended_drugs.append(df['drugName'][i])


# In[23]:


recommended_drugs

