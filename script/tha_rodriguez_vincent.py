#############################################
#=============Read in Libraries=============#
# Read in the necessary libraries.          #
#############################################
import pandas as pd
import numpy as np
import os
from os.path import exists
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import nltk
from nltk.stem import PorterStemmer


# Run the following a single time to download these:
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags


# data storage
data_dir = "/home/architectus/docker/osu/MSIS5193/WK13/named-entity-recognition-tha-0Architectus0/data/"

osu_history_name = 'wiki_osu_history.txt'

file_path = data_dir + osu_history_name

file_exists = exists(file_path)

#===============================
# History of OSU (2 pts.)
#===============================
wiki_url = "https://www.espn.com/college-football/scoreboard"

driver = webdriver.Firefox(executable_path="/home/architectus/docker/osu/MSIS5193/WK9/geckodriver")
driver.get(wiki_url)

paragraphs = driver.find_elements_by_xpath('/html/body/div[3]/div[@id="bodyContent"]/div[@id="mw-content-text"]/div[1]//p[count(preceding-sibling::h2)=1]')

textbank = ""

for para in paragraphs:
    textbank += para.text

# write to data dir
osu_history_file = open(file_path,"w")
osu_history_file.writelines(textbank)
osu_history_file.close() 

driver.quit()

#open text file in read mode
#text_file = open(file_path, "r")

#read whole file to a string
#textbank = text_file.read()

#close file
#text_file.close()

print(textbank)
#===============================
# Extracting and Assessing Entities (8 pts.)
#===============================
pos = pos_tag(word_tokenize(textbank))
print(pos)

fd = nltk.FreqDist(pos)
fd.plot()

tree = ne_chunk(pos)
print(tree)

entity_nouns = []

# NN: noun, singular
# NNS: noun, plural
# NNP: proper noun, singular
# NNPS: proper noun, plural


entityp = []
entityo = []
entityg = []
entitydesc = []

for x in str(tree).split('\n'):
    if 'PERSON' in x:
        print(x)
        entityp.append(x)
    elif 'ORGANIZATION' in x:
        entityo.append(x)
    elif 'GPE' in x or 'GSP' in x:
        entityg.append(x)
    elif '/NN' in x:
        entitydesc.append(x)

entityp
entityo
entityg
entitydesc

entity_nouns = entityp + entityo + entityg

iob_tag = tree2conlltags(tree)

# Overall, what do your findings suggest about OSU? (1 pt.)
"""
OSU likes to talk about itself (not unwarranted in a history of OSU) and name things after people; most likely doners. 
"""