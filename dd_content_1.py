import requests
from bs4 import BeautifulSoup
import csv
import random

from urllib import request
import json
import datetime

def get_random_quote():
    #URL = "http://quotes.toscrape.com/page/2/"
    URL = "http://quotes.toscrape.com/"
    page = requests.get(URL)
    #print(page.text)

    soup = BeautifulSoup(page.content,"html.parser")
    results = soup.find_all("div", class_="col-md-8")
    #print(results)
    #results = results.find_all(class_="quote")
    #print(type(results))

    quotes_to_mail = []
    for job_element in results:
        #print(job_element)
        quote_elem = job_element.find_all(class_="quote")
        i=1
        for quotes in quote_elem:
            #print(i)
            quote = quotes.text.split("\n")[1]
            auth = quotes.text.split("\n")[2]
            quotes_to_mail.append({"quote":quote,"author":auth})
        #print(quotes_to_mail)
    return random.choice(quotes_to_mail)
"""          
            with open('quotes_authors.csv',mode='w') as csv_file:
                writer = csv.writer(csv_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([quote,auth])
            i+=1

        #author_elem = job_element.find_all(class_="author")
        #print(quote_elem,author_elem)
"""



def get_weather_forecast(coords={'lat':	39.0437567,'lon': -77.4874416}):
    try:
        api_key = "df02d44356c0ce23e8f27e5d011418ee"
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric'
        print (url)
        data = json.load(request.urlopen(url))
        data = json.dumps(data, indent=2)
        #print(data)
        print(data["city"]["name"])

        forecast = {'city': data['city']['name'],  # city name
                    'country': data['city']['country'],  # country name
                    'periods': list()}  # list to hold forecast data for future periods

        for period in data['list'][0:9]:  # populate list with next 9 forecast periods
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}.png'})
            #print(forecast['city'])

        return forecast
        

    except Exception as e:
        print(e)



def get_twitter_trends():
    pass

#def get_wiki_article():
#    pass




if __name__ == '__main__':
    #quote = get_random_quote()
    #print(quote["quote"])
    #print(quote["author"])
    #print(f' - Random quote is {quote["quote"]} - {quote["author"]}')

    #forecast=get_weather_forecast()
    #print(forecast['periods'])