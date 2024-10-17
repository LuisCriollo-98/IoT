'''
Scrip descrption: Get all data about solar system.

'''

import os
import requests

os.system('clear')

def get_data():
    print("::: SOLAR SYSTEM INFORMATION :::")
    url = "https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"
    print(type(url)) #verificar tipo de dato
    
    try:
        #Request to API
        res = requests.get(url)
        res.raise_for_status()
        
        #Convert answer to JSON (Java Object Notation)

        data = res.json()

        print(data)


    except requests.exceptions.RequestsException as e:
        print(f"API error: {e}")

get_data()
