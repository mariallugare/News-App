import urllib.request, json
from .models import Article, Sources

api_key = None
base_url = None



def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    
    
def get_all_news(sources="news-com-au,al-jazeera-english,associated-press,the-washington-post,the-hill,bbc-news,engadget,techcrunch", page_size=30):
    '''
    Function that gets the json response to our url request
    '''
    # get_news_url = '{}/everything?language=en&pageSize={}&sources={}&apiKey={}'.format(base_url,page_size,sources, api_key)
    get_news_url = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=d4f3a1944f534b2b962ebe231208abd2'
    

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results


# def get_source_news(sources, page_size=30):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_news_url = '{}/everything?language=en&pageSize={}&sources={}&apiKey={}'.format(base_url,page_size,sources, api_key)

#     with urllib.request.urlopen(get_news_url) as url:
#         get_news_data = url.read()
#         get_news_response = json.loads(get_news_data)

#         news_results = None

#         if get_news_response['articles']:
#             news_results_list = get_news_response['articles']
#             news_results = process_results(news_results_list)


#     return news_results


def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if urlToImage:
            news_object = Article(author,title,description,url,urlToImage,publishedAt)
            news_results.append(news_object)

    return news_results