# ---------------- Web Scraping Imports ------------------------
from bs4 import BeautifulSoup
import requests

def related_article_scraper(claim):
    all_articles = []
    q_param = claim.replace(" ","%20")

    url = f'https://news.google.com/search?q={q_param}&hl=en-IN&gl=US&ceid=US%3Aen'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    pub = []
    for article in soup.find_all('a', class_='wEwyrc AVN2gc uQIVzc Sksgp'):
        pub.append(article.text)

    i = 0
    for article in  soup.find_all('a'):
        if len(article.text) > 30:
            title = article.text
            #link = requests.get('https://news.google.com/' + article['href'].split('/',1)[1]).url
            link = 'https://news.google.com/' + article['href'].split('/',1)[1]

            new_article = {'pub' : pub[i] ,'title' : title ,'url' : link ,'stance' : ' UNKNOWN '}

            all_articles.append(new_article)
            i+=1

        if i>9:
            break
        
    return all_articles

def title_scraper(url):
    r = requests.get(url).text

    soup = BeautifulSoup(r, 'lxml')

    claim = soup.find('title').text
        
    return claim

def body_scraper(url):
    if 'reuters' in url:
        body = reuter_scraper(url)
    if 'usatoday' in url:
        body = usatoday_scraper(url)
    if 'cnn' in url:
        body = cnn_scraper(url)
    if 'nytimes' in url:
        body = nytimes_scraper(url)
    if 'nypost' in url:
        body = nypost_scraper(url)
    if 'foxnews' in url:
        body = foxnews_scraper(url)
    
    return body

def reuter_scraper(url):

    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = ""

    for para in soup.find_all('p'):
            if(len(para.text) > 30 and "Reporting by" not in para.text and "Thomson Reuters" not in para.text  and "All quotes delayed a" not in para.text):
                    body = body + para.text


    body = title + body

    return body

def usatoday_scraper(url):
    # url = "https://www.usatoday.com/story/news/politics/2020/11/02/trump-fire-fauci-after-election/6120265002/"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('title').text
    body = " "

    for article in soup.find_all('p', class_='gnt_ar_b_p'):
        body = body + article.text
    body = title + body

    return body

def cnn_scraper(url):
    # url = "https://edition.cnn.com/2020/11/02/uk/why-wasnt-uk-public-told-about-prince-william-intl-gbr/index.html"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = " "

    for article in soup.find_all('p', class_='zn-body__paragraph speakable'):
        body = body + article.text
    body = title + body

    for article in soup.find_all('div', class_='zn-body__paragraph speakable'):
        body = body + article.text

    for article in soup.find_all('div', class_='zn-body__paragraph'):
        body = body + article.text


    return body

def nytimes_scraper(url):
    # url = "https://www.nytimes.com/2020/11/02/us/politics/Pennsylvania-presidential-election.html?action=click&module=Top%20Stories&pgtype=Homepage"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = " "

    for article in soup.find_all('p', class_='css-158dogj evys1bk0'):
        body = body +" "+ article.text
    body = title + body

    return body


def huffingtonpost_scraper(url):
    # url = "https://www.usatoday.com/story/news/politics/2020/11/02/trump-fire-fauci-after-election/6120265002/"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = " "
    print(title)
    for article in soup.find_all('p'):
        body = body + article.text
    body = title + body

    return body

def foxnews_scraper(url):
    # url = "https://www.foxnews.com/entertainment/celebrities-leave-america-trump-re-elected"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = " "

    for article in soup.find_all('p', class_="speakable"):
        body = body + article.text

    for article in soup.find_all('p'):
        body = body + article.text
        if "published" in article.text and "broadcast" in article.text and"rewritten" in article.text and "redistributed" in article.text:
            break

    body = title + body
    print(body)
    return body

def Politico(url):
    # url = "https://www.politico.com/news/2020/11/02/trump-suburban-house-gop-down-433898"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h2').text
    body = " "

    for article in soup.find_all('p', class_="story-text__paragraph"):
        body = body + article.text

    body = title + body

    return body


def NPR(url):
    # url = "https://www.npr.org/2020/11/03/930688481/bail-for-kyle-rittenhouse-accused-kenosha-shooter-set-at-2-million"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = " "

    for article in soup.find_all('p'):
        body = body + article.text

    body = title + body

    return body

def nypost_scraper(url):
    # url = "https://nypost.com/2020/11/03/the-daniel-jones-doubts-grow-after-blown-giants-chance/"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'lxml')

    title = soup.find('h1').text
    body = " "

    for article in soup.find_all("p"):
        body = body + article.text
        if "Read Next" in article.text:
            break

    body = title + body

    return body