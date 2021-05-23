#pip install flask
#pip install beautifulsoup4
#pip install lxml
#pip install requests
#pip install nltk
#pip install sklearn
#pip install nltk
#pip install joblib
#pip install pbs

from flask import Flask, render_template, request
from scrapers import *
from ourML import *
import random

app = Flask(__name__)

all_articles = []

@app.route('/', methods=['GET', 'POST'])
def home():
    
    all_articles = []
    result_1 = ""
    #result_2 = ""
    confidence_1 = 0.0
    ##confidence_2 = 0.0

    if request.method == 'POST':

        user_input = request.form['claim']

        if 'http' in user_input :
            url = user_input
            claim = title_scraper(url)
            body = body_scraper(url)
            body = preprocessing(body)
            statement1 = our_model_1(body)
            #statement2 = our_model_2(body)

        else:
            claim = user_input
        
        all_articles = related_article_scraper( claim )
        result_1 =  statement1.split(" ")[0]
        confidence_1 = round( float(statement1.split(" ")[1]), 5)

        #result_2 =  statement2.split(" ")[0]
        #confidence_2 = round(confidence_1 - float(statement2.split(" ")[1]), 5)
        
        return render_template('index.html', articles = all_articles, claim = claim, result_1 = result_1, confidence_1 = confidence_1)

    else:
        claim = ""
        return render_template('index.html', articles = all_articles, claim = claim, result_1 = result_1, confidence_1 = confidence_1)

@app.route('/faq')
def faq():
    return render_template('faq.html')



if __name__ == "__main__":
    app.run(debug=True)

