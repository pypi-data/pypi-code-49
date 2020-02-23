# import the necessary packages
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import PyPDF2
import re

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head',  'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# we use this method to get text from the web page
# it take one parameter as URL of web page
def get_text(url):
    print (url) 
    try:
        req  = requests.get(url, timeout=5)
    except: 
        return "TIMEOUT ERROR" 
    data = req.text
    soup = BeautifulSoup(data, "html.parser")
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    
    return "".join(t.strip() for t in visible_texts)

# this method convert an url to string 
# take one parameter as URL and return a text
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for scrip in soup(["scrip", "style", "aside"]):
        scrip.extract()
    
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

# this method convert an pdf to text
# it take one parameter as path of a document
def pdf_to_text(path):
    text = ' '
    
    with open(path, mode='rb') as file:
        reader_pdf = PyPDF2.PdfFileReader(file)
    
        # loop over all document page by page and extract text on page
        # add extracted text to text
        for page in reader_pdf.pages:
            text = " ".join(re.split(r'[\n\t]+', page.extractText()))
    return text 