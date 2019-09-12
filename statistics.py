#! usr/bin/env python3
import praw
import copy
import datetime as dt
import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
#import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import re
from bs4 import BeautifulSoup
#%matplotlib inline

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer

#link = input()
reddit = praw.Reddit(client_id='#', \
                     client_secret='#', \
                     user_agent='#', \
                     username='#', \
                     password='#')
#submission = reddit.submission(url=link)
#print (submission.link_flair_text)
#title = submission.title
#flair = submission.link_flair_text
#print (flair)
arrc = []
arru = []
arrf = []
subreddit = reddit.subreddit('india')
top_subreddit = subreddit.top(limit=400)
for i in top_subreddit:
	#print (submission.comments[0].body)
	arrc.append(i.num_comments)
	arru.append(i.upvote_ratio)
	arrf.append(i.link_flair_text)

AskIndia_comments = 0
AskIndia_upvotes = 0
BuisnessFinance_comments = 0
BuisnessFinance_upvotes = 0
Food_comments = 0
Food_upvotes = 0
Non_Political_comments = 0
Non_Political_upvotes = 0
Photography_comments = 0
Photography_upvotes = 0
Policy_Economy_upvotes = 0
Policy_Economy_comments = 0
Politics_comments = 0
Politics_upvotes = 0
Science_Technology_comments = 0
Science_Technology_upvotes = 0
Sports_comments = 0
Sports_upvotes = 0
Reddiquette_upvotes = 0
Reddiquette_comments = 0
for i in range(0, 400):
	if (arrf[i]=="AskIndia"):
		AskIndia_comments += arrc[i]
		AskIndia_upvotes += arru[i]
	if (arrf[i]=="Buisness/Finance"):
		BuisnessFinance_comments += arrc[i]
		BuisnessFinance_upvotes += arru[i]
	if (arrf[i]=="Food"):
		Food_comments += arrc[i]
		Food_upvotes += arru[i]
	if (arrf[i]=="Non-Political"):
		Non_Political_comments += arrc[i]
		Non_Political_upvotes += arru[i]
	if (arrf[i]=="Photography"):
		Photography_comments += arrc[i]
		Photography_upvotes += arru[i]
	if (arrf[i]=="Policy/Economy"):
		Policy_Economy_comments += arrc[i]
		Policy_Economy_upvotes += arru[i]
	if (arrf[i]=="Politics"):
		Politics_comments += arrc[i]
		Politics_upvotes += arru[i]
	if (arrf[i]=="Science/Technology"):
		Science_Technology_comments += arrc[i]
		Science_Technology_upvotes += arru[i]
	if (arrf[i]=="Sports"):
		Sports_comments += arrc[i]
		Sports_upvotes += arru[i]
	if (arrf[i]=="[R]eddiquette"):
		Reddiquette_comments += arrc[i]
		Reddiquette_upvotes += arru[i]

	print (AskIndia_comments/400, BuisnessFinance_comments/400, Food_comments/400, Non-Political_comments/400, Photography_comments/400,
		Policy_Economy_comments/400, Politics_comments/400, Science_Technology_comments/400, Sports_comments/400, Reddiquette_comments/400)
	print (AskIndia_upvotes/400, BuisnessFinance_upvotes/400, Food_upvotes/400, Non-Political_upvotes/400, Photography_upvotes/400,
		Policy_Economy_upvotes/400, Politics_upvotes/400, Science_Technology_upvotes/400, Sports_upvotes/400, Reddiquette_upvotes/400)
#print (arrc)
#print (arru)
