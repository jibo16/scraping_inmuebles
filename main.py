import gzip
import os
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup as bs

def reading(files):
    for i in files:

        with gzip.open(i, 'rb') as f:
            file_content = f.read()

        tree = etree.fromstring(file_content)
        namespaces = tree.nsmap.copy()
        recipies_dict = [] 
        for url in tree.findall('url', namespaces = namespaces):
            loc = url.find('loc', namespaces = namespaces).text
            recipies_dict.append({'loc':loc})
    return recipies_dict


def to_pandas(js):
    df = pd.DataFrame(js)
    df.to_csv('final')
    return df

directory = '/home/jib/Desktop/scraping_inmuebles'
xml_gz_files = [f for f in os.listdir(directory) if f.endswith('.xml.gz')]

d = reading(xml_gz_files)

to_pandas(d)
        
