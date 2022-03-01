'''For sentences'''
'''1.Get atleast 50 links from different news api_s'''
'''2.Find sites from where you can get sentences'''
'''3.Connect those sentences as one and send it back to where you were called from'''
from gnews import GNews
from newsfetch.news import newspaper
from search_engines import yahoo_news
from search_engines import bing_news
import requests
import time


# '''Get Sentence'''
def sentences(wordorphrase,article_data):
    word=article_data.index(wordorphrase)
    start=article_data.rfind(".",0,word)
    end=article_data.index(".",word)
    # print(article_data[start+1:end+1])
    return article_data[start+1:end+1]


def get_sentences(worp,n=15):
    wordorphrase=worp
    mode = 1
    sentence_list=[]
    link_read=[]
    repeats=0
    while len(sentence_list)<n:
        
        if mode==1:
            
            try:
                google_news = GNews(max_results=75)
                # google_news = GNews(max_results=2)
                temp = google_news.get_news(wordorphrase)
                for i in range(len(temp)):
                    # print(temp[i]['url'])
                    link=temp[i]['url']
                    print("No of sentences collected:",len(sentence_list)," "*10,end='\r')
                    
                    if repeats==15 or len(sentence_list)>=n:
                        repeats=0
                        raise Exception
                    if link in link_read:
                        
                        repeats=repeats+1
                        continue
                    try :
                        requests.get(link,timeout=3)
                        pass
                    except :
                        continue
                    link_read.append(link)
                    news=newspaper(link)
                    article_data=news.article
                    if wordorphrase in article_data:
                        sent=sentences(wordorphrase,article_data)
                        sentence_list.append(str(len(sentence_list)+1)+") "+sent+"<br>")
            except:
             
                mode=2
                
                continue
            mode=2

        elif mode==2:
            
            try:
                url = bing_news.get_search_url(wordorphrase)
                next_page_url=url
                while next_page_url is not None:
                    resp = requests.get(next_page_url)
                    html = resp.text
                    results, next_page_url = bing_news.extract_search_results(html, url)
                    # print(len(results))
                    for result in results:
                        # print(result['url'])
                        print("No of sentences collected:",len(sentence_list)," "*10,end='\r')
                        
                        if repeats==15 or len(sentence_list)>=n:
                            repeats=0
                            raise Exception
                        if result['url'] in link_read:
                            
                            repeats=repeats+1
                            continue
                        try :
                            requests.get(link,timeout=3)
                            pass
                        except :
                            continue
                        link_read.append(result['url'])
                        news=newspaper(result['url'])
                        article_data=news.article
                        if wordorphrase in article_data:
                            try:
                                sent=sentences(wordorphrase, article_data)
                                sentence_list.append(str(len(sentence_list)+1)+") "+sent+"<br>")
                                
                            except:
                                continue
                    time.sleep(10)
            except:
                
                mode=3
                
                continue
            mode=3

        elif mode==3:
            
            try:
                url = yahoo_news.get_search_url(wordorphrase)
                next_page_url=url
                while next_page_url is not None:
                    resp = requests.get(next_page_url)
                    html = resp.text
                    results, next_page_url = yahoo_news.extract_search_results(html, url)
                    # print(len(results))
                    for result in results:
                        # print(result['url'])
                        print("No of sentences collected:",len(sentence_list)," "*10,end='\r')
                        if repeats==10 or len(sentence_list)>=n:
                            repeats=0
                            raise Exception
                        if result['url'] in link_read:
                            repeats=repeats+1
                            continue
                            try :
                                requests.get(link,timeout=3)
                                pass
                            except :
                                continue
                        link_read.append(result['url'])
                        news=newspaper(result['url'])
                        article_data=news.article
                        if wordorphrase in article_data:
                            try:
                                sent=sentences(wordorphrase, article_data)
                                sentence_list.append(str(len(sentence_list)+1)+") "+sent+"<br>")
                            except:
                                continue
                    time.sleep(10)
            except:
                break
            break
        # print("Curr Mode: ",mode," "*15)
        time.sleep(10)
    print(sentence_list)
    return " ".join(sentence_list)
