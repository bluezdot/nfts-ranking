
from urllib import request
from bs4 import BeautifulSoup
import json
import ssl
import pandas as pd

def create_dataframe():
    
    """
    Create a null dataframe with columns
    """
    
    df = pd.DataFrame(columns=['Id', 'Title', 'Uri', 'Rank', 'Sale7', 'SaleAll', 'Volumn7', 'VolumnAll'])
    return df

# print(create_dataframe())
def get_project_data(df, site_json, number_of_projects):
    print(df)
    for i in range(number_of_projects):
        project = site_json['projects'][i]
        id = project['id']
        title = project['title']
        uri = project['uri']
        rank = i + 1
        sale7 = project['statistics'][0]['value']
        saleAll = project['statistics'][1]['value']
        volumn7 = project['statistics'][2]['value']
        volumnAll = project['statistics'][3]['value']
        df = pd.concat([df, pd.DataFrame.from_records([{'Id': id, 'Title': title, 'Uri': uri, 'Rank': rank, 'Sale7': sale7, 'SaleAll': saleAll, 'Volumn7': volumn7, 'VolumnAll': volumnAll}])])
    return df
if __name__ == '__main__':
    
    # Create an SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_NONE

    # Configuration
    number_of_projects = 300

    api = f"https://nonfungible.com/api/topProjects?limit={number_of_projects}&orderBy=SUMUSD7D&order=DESC"
    html = request.urlopen(api, context=context).read()
    soup = BeautifulSoup(html,'html.parser')
    site_json=json.loads(html)
    
    df = create_dataframe()
    _df = get_project_data(df, site_json, number_of_projects)
    _df.to_excel('nonfungible.xlsx')
    
    