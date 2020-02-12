import pickle
from sklearn.feature_extraction.text import CountVectorizer
import re
import warnings
import pkg_resources
import os

warnings.filterwarnings("ignore")



def pred(question,comments):
    comm = []
    resource_package = 'ICHT_PatientExperience'
    
    for text in comments:
        text = text.strip().lower()
        text = text.strip()
        text = re.sub('[0-9]+', '' ,text)
        comm.append(text)
        
    if question == 1:
        
        resource_path = '/'.join(('models','feature1.pkl'))
        feature_path = pkg_resources.resource_filename(resource_package, resource_path)
            
        resource_path = '/'.join(('models','tfidftransformer1.pkl'))
        tfidftransformer_path = pkg_resources.resource_filename(resource_package, resource_path)
        
        resource_path = '/'.join(('models','Q1TopicNew.pkl'))
        clf1_path = pkg_resources.resource_filename(resource_package, resource_path)
        with open(clf1_path,'rb') as clf1_file:
            clf1 = pickle.load(clf1_file)
            
        resource_path = '/'.join(('models','Q1SentiNew.pkl'))
        clf2_path = pkg_resources.resource_filename(resource_package, resource_path)
        with open(clf2_path,'rb') as clf2_file:
            clf2 = pickle.load(clf2_file)
        
    else:
        resource_path = '/'.join(('models','feature2.pkl'))
        feature_path = pkg_resources.resource_filename(resource_package, resource_path)
            
        resource_path = '/'.join(('models','tfidftransformer2.pkl'))
        tfidftransformer_path = pkg_resources.resource_filename(resource_package, resource_path)

        resource_path = '/'.join(('models','Q2TopicNew.pkl'))
        clf1_path = pkg_resources.resource_filename(resource_package, resource_path)
        with open(clf1_path,'rb') as clf1_file:
            clf1 = pickle.load(clf1_file)
            
        resource_path = '/'.join(('models','Q2SentiNew.pkl'))
        clf2_path = pkg_resources.resource_filename(resource_package, resource_path)
        with open(clf2_path,'rb') as clf2_file:
            clf2 = pickle.load(clf2_file)
    
    loaded_vec = CountVectorizer(decode_error= "replace", vocabulary = pickle.load(open(feature_path, 'rb')))
    tfidftransformer = pickle.load(open(tfidftransformer_path, 'rb')) 
    temp = loaded_vec.transform(comm)
    test_tfidf = tfidftransformer.transform(temp)
    
    
    y_pred1 = clf1.predict(test_tfidf)
    y_pred2 = clf2.predict(test_tfidf)
    
    return y_pred1, y_pred2