import time ,math
from urllib.request import urlopen
import requests
import re



class InstaVideoDownloader : 
    def __init__(self, cookies, headers) :
        self.cookies = cookies
        self.headers = headers
    def scrape_mediaid(self, contents) :
        index_ = contents.index('"media_id":')
        l = len('"media_id":')
        media_id = str()
        for char in contents[index_+l + 1:] : 
            try : 
                int(char)
                media_id += char
            except  : 
                break
        return media_id

    def get_mediaid(self, link) :
        session = requests.session()
        self.validate_web_url(link)
        r  = session.get(link, headers=self.headers, cookies=self.cookies)
        contents = str(r.content)
        #media_id = [i for i in contents[index_ + l] if type(int(str(i))) == "<class 'int'>" else : break]  
        media_id = self.scrape_mediaid(contents=contents)
        return media_id
    def get_link(self, links) : 
        for link in links  :
            if type(link) == type(tuple()) :
                for l in link : 
                    if ('.mp4?' in l) and ('efg' in l) : 
                        return l
    
    def validate_web_url(self,url):
        try:
            urlopen(url)
            return True
        except :
            content = eval(url)
            content = content['?params']
            print(content, 'not valid url')
            exit(0)
    def get_info(self, link) : 
        session = requests.session()
        media_id = self.get_mediaid(link=link)
        url = f"https://i.instagram.com:443/api/v1/media/{media_id}/info/"
        r = session.get(url=url, headers=self.headers, cookies=self.cookies)
        contents = str(r.content)
        link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        links = re.findall(link_regex, contents)
        links = self.get_link(links=links)
        session.close()
        link = links.replace('\\\\u0026', '&')
        return link
    def get_raw(self, url) :
        session = requests.session()
        r = session.get(url=url, headers=self.headers)
        contents = r.content
        with open(f'IG_video_{str(math.floor(time.time()))}.mp4', 'wb') as f : 
            f.write(contents)
            f.close()
        print('video downloaded')