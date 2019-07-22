# Reddit Flair Detector

A Reddit Flair Detector web application to detect flairs of India subreddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Detector](https://reddit-flair-detector-sp.herokuapp.com/).

#Url as feature
accuracy from Naive Bayes = 0.6410256410256411
accuracy from Linear SVM = 0.5384615384615384
accuracy from Logistic Regression = 0.48717948717948717

#Title as feature
accuracy from Naive Bayes = 0.6666666666666666
accuracy from Linear SVM = 0.6410256410256411
accuracy from Logistic Regression = 0.5641025641025641

#Title+Url as feature
accuracy from Naive Bayes = 0.6410256410256411
accuracy from Linear SVM = 0.5897435897435898
accuracy from Logistic Regression = 0.5346587647883683

#url_feature.py = this python code uses url as its only feature for prediction
#title_feature.py = this python code uses title as its only feature for prediction
#title+url_feature.py = this python code uses url as well as title as its feature for prediction

#precog.html, precog.css, statistics.html, statistics.css = these 4 are the files which are used to desing the website

#reddit-flair-detector-sp = this is the webapp which is hosted on heroku

#data.txt = this file contains the data used for predictions

#statistics.py = this python code is used for the calculations of the statistics.html page which tells te percentage of num_comments and upvote_ratio of differet types of flaired posts.

### References

1. [How to scrape data from Reddit](http://www.storybench.org/how-to-scrape-reddit-with-python/)
2. [Multi-Class Text Classification Model Comparison and Selection](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
