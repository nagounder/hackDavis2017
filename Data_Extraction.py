#authors: Nandhini Gounder, Nishtha Asija, Iyesha Puri
#January 21-22, 2017
#Program extracts data from the OSISoft API and analyzes annual cost/sq ft. for
#energy expenditures of electricity, chilled water, and steam.
#This analysis provides a window into measuring energy efficiency of a building
#Further analysis would require, usage of building and comparison to similar buildings
#to determine if energy effciency is at par.

import requests
    

def electricity (b):
    print ("Annual Cost of Electricity/Square Foot ($)")   
    for building in b.json()['Items']:
        data = requests.get(building["Links"]["Elements"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
        
        while data.status_code != requests.codes.ok:
            data = requests.get(building["Links"]["Elements"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

        for energy in data.json()['Items']:
            if (energy['Name'] == "Electricity"):
                e = requests.get(energy["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                while e.status_code != requests.codes.ok:
                    e = requests.get(energy["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                
        for info in e.json()['Items']:
            if (info['Name'] == "Annual Cost"):
                cost = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

                while cost.status_code != requests.codes.ok:
                    cost = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                                      
            if (info['Name'] == "Sq Ft."):
                sqft = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

                while sqft.status_code != requests.codes.ok:
                    sqft = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                    
        if (cost.json()['Good'] and sqft.json()['Good'] and sqft.json()['Value'] != 0):
            print (building['Name'], cost.json()['Value']/sqft.json()['Value'])
        else:
            print (building['Name'], 'n/a')
            

def chilledWater (b):
    print ("Annual Cost of Chilled Water/Square Foot ($)")   
    for building in b.json()['Items']:
        data = requests.get(building["Links"]["Elements"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
        
        while data.status_code != requests.codes.ok:
            data = requests.get(building["Links"]["Elements"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

        for energy in data.json()['Items']:
            if (energy['Name'] == "ChilledWater"):
                e = requests.get(energy["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                while e.status_code != requests.codes.ok:
                    e = requests.get(energy["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                
        for info in e.json()['Items']:
            if (info['Name'] == "Annual Cost"):
                cost = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

                while cost.status_code != requests.codes.ok:
                    cost = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                                      
            if (info['Name'] == "Sq Ft."):
                sqft = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

                while sqft.status_code != requests.codes.ok:
                    sqft = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                    
        if (cost.json()['Good'] and sqft.json()['Good'] and sqft.json()['Value'] != 0):
            print (building['Name'], cost.json()['Value']/sqft.json()['Value'])
        else:
            print (building['Name'], 'n/a')


def steam (b):
    print ("Annual Cost of Steam/Square Foot ($)")   
    for building in b.json()['Items']:
        data = requests.get(building["Links"]["Elements"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
        
        while data.status_code != requests.codes.ok:
            data = requests.get(building["Links"]["Elements"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

        for energy in data.json()['Items']:
            if (energy['Name'] == "Steam"):
                e = requests.get(energy["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                while e.status_code != requests.codes.ok:
                    e = requests.get(energy["Links"]["Attributes"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                
        for info in e.json()['Items']:
            if (info['Name'] == "Annual Cost"):
                cost = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

                while cost.status_code != requests.codes.ok:
                    cost = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                                      
            if (info['Name'] == "Sq Ft."):
                sqft = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))

                while sqft.status_code != requests.codes.ok:
                    sqft = requests.get(info["Links"]["Value"], auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
                    
        if (cost.json()['Good'] and sqft.json()['Good'] and sqft.json()['Value'] != 0):
            print (building['Name'], cost.json()['Value']/sqft.json()['Value'])
        else:
            print (building['Name'], 'n/a')

def main ():
    b = requests.get('https://bldg-pi-api.ou.ad3.ucdavis.edu/piwebapi/elements/E0bgZy4oKQ9kiBiZJTW7eugwvgV_Y00J5BGt6DwVwsURwwVVRJTC1BRlxDRUZTXFVDREFWSVNcQlVJTERJTkdT/elements', auth=('ou\pi-api-public', 'M53$dx7,d3fP8'))
    electricity(b)
    chilledWater(b)
    steam(b)
         
main()
