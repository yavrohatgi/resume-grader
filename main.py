import re
import pdfplumber
import spacy
import json
import sys
import sklearn

# Donload the spacy model buy running the following command : 
# python -m spacy download en_core_web_sm
# Approximately 12mb in size 
nlp = spacy.load("en_core_web_sm") # Load the model

def extract_text_from_pdf(pdf_path):
    text = "" # empty 
    with pdfplumber.open(pdf_path) as pdf: # open pdf file using pdfplumber
        for page in pdf.pages: # iterate through each page
            text += page.extract_text() + "\n" # extract text
    return text.strip()

# sample usage
text = extract_text_from_pdf("resume.pdf")
print(text)