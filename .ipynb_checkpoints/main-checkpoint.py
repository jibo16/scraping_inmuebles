import gzip
import os
import pandas as pd
from lxml import etree


url = 'https://www.inmuebles24.com/sitemaps_https.xml'
scraper = cloudscraper.create_scraper()

res = scraper.get(url).text

directory = '/home/jib/Desktop/scraping_inmuebles'
xml_gz_files = [f for f in os.listdir(directory) if f.endswith('.xml.gz')]


def reader_convertor(list_url):
    
    urls_dict = []
    for i in list_url:  
        try:
            with gzip.open(i, 'rb') as f:
                i = f.read()

                tree = etree.fromstring(i)
                namespaces = tree.nsmap.copy()
                
                for url in tree.findall('url', namespaces = namespaces):
                    loc = url.find('loc', namespaces = namespaces).text
                    urls_dict.append({'loc':loc})
        except:
            pass
    print(len(urls_dict))
    return urls_dict

def dataframe_convertor(dict_list:list) -> None:
    df = pd.DataFrame(dict_list).rename(columns={'loc':'urls'})
    df.to_csv('testing.csv')


if __name__ == '__main__':
    xml = reader_convertor(xml_gz_files)
    dataframe_convertor(xml)