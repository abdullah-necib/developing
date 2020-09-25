from bs4 import BeautifulSoup
import re, requests
from collections import deque

req = requests.get('https://www.sainsburys.co.uk/shop/gb/groceries/meat-fish?fromMegaNav=1')
soup = BeautifulSoup(req.text,'html.parser')

product_url = []

def print_list(lst):
    counter =1;
    if type(lst) == list:
        for i in lst:
            print(counter,' >    ', i)
            counter +=1
    else:
        print(lst)
        
def find_urls(url):
    result = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'html.parser')
    ul_department = soup.find('ul',class_='categories departments')
    ul_aisles = soup.find('ul', class_='categories aisles')
    ul_gridView = soup.find('ul',class_='productLister gridView')   
    if ul_aisles:
        ul_department = None
        for li in ul_aisles.find_all('li'):
            a = li.find('a',href = True)
            if a: result.append(a['href'])
        return result        
    if ul_department:
        for li in ul_department.find_all('li'):
            a = li.find('a',href = True)
            if a: result.append(a['href'])
        return result    
    if ul_gridView:        
        while True:                        
            for li in ul_gridView.find_all('li',class_='gridItem'):
                a_product = li.find('a',href= True)
                if a_product : result.append(a_product['href'])                
            next_tag = soup.find('li',class_='next')
            a = next_tag.find('a',href= True)            
            if a:                
                req = requests.get(a['href'])
                soup = BeautifulSoup(req.text,'html.parser')
                ul_gridView = soup.find('ul', class_='productLister gridView')
                #print('a is exist')
            else:
                #print('there is no a')
                break
        return result    
    if soup.body['id']:
        if soup.body['id']=='productDetails':
        #print('we reach here')
            return url
    else: return None

def test(url):
    result = dfs_search(url)
    print('result count: ',len(result))
    print_list(dfs_search(url))
                
            
def dfs_search(url):
    result = []
    visited = set()
    queue = deque()
    queue.append(url)
    while queue:
        current = queue.popleft()
        if current in visited: continue
        visited.add(current)
        lst = find_urls(current)
        if type(lst) == list: queue.extend(lst)
        if type(lst) == str:
            print(lst)
            result.append(lst)
    return result
