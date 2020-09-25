#create robots.txt reader to check the possibility

from urllib import robotparser

robot = robotparser.RobotFileParser()
robot.set_url('http://www.apress.com')
robot.read()
print(robot.can_fetch('http://hajba.hu/category/software-­development/java-software-development/','*'))
print('Done.................')


#find all occurance of <img> from the page
from urllib.request import urlopen, urljoin
import re
def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_image_locations(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE)
    return img_regex.findall(page)

if __name__ == '__main__':
    target_url = 'http://www.apress.com/'
    apress = download_page(target_url)
    image_locations = extract_image_locations(apress)
    for src in image_locations:
        print(urljoin(target_url, src))
