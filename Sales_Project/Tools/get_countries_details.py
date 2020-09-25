import requests
from bs4 import BeautifulSoup as bs
from datetime import  datetime
from Tools import writeCSV
import json

countriesFile = 'countries_details.csv'
countriesURL = 'https://countrycode.org/'

def getCities(cityURL):
    page = requests.get(cityURL)
    # print(cityURL)
    soup = bs(page.content, 'html.parser')
    table = soup.find('div', id='collapseCityCodes').find('tbody').findAll('tr')
    temp_dict = {}
    for tr in table:
        tds = tr.findAll('td')
        temp_dict[tds[0].getText()] = tds[1].getText()
    page.close()
    return temp_dict



def GetCountry(countriesURL):
    start = datetime.now()
    page = requests.get(countriesURL)
    soup = bs(page.content, 'html.parser')
    table = soup.find('table',class_='table table-hover table-striped main-table').tbody.findAll('tr')
    cnt = 0
    for tr in table:
        temp_dict = {"index":"cnt{0:0>3}".format(cnt)}
        tds = tr.findAll("td")
        temp_dict["href"] = tds[0].a["href"]
        temp_dict["country"] = tds[0].a.getText()
        temp_dict["country_code"] = tds[1].getText()
        splt = tds[2].getText().split("/")
        temp_dict["iso2"] = splt[0].replace(" ","")
        temp_dict["iso3"] = splt[1].replace(" ", "")
        temp_dict["popuation"]= tds[3].getText()
        temp_dict["area"] = tds[4].getText()
        temp_dict["gdp"] = tds[5].getText()
        temp_dict["cities"] = getCities(countriesURL[:-1]+temp_dict["href"])
        writer = writeCSV.WriteToCSV(fileName='countries.csv')
        writer.Write(json.dumps(temp_dict, indent=4))
        print(temp_dict)
        cnt +=1
    page.close()
    end = datetime.now()
    print('Job accomplished in ', end - start)


GetCountry(countriesURL)
