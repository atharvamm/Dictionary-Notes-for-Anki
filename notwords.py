'''Imports'''
import requests
import html_to_json
import urllib.request
import html_to_json
import urllib.parse

link_def='https://www.urbandictionary.com/define.php?term='

'''Initialization'''
'''1.If word not in previous state go for not words'''
'''2.If not found in free dictionary then here we will search in urban dictionary'''
def urban_dictionary(worp):
    try:
            link=link_def+urllib.parse.quote(worp)
            # print(worp)
            data=urllib.request.urlopen(link).read().decode('utf-8')
            json_data=html_to_json.convert(data)
            temp1=json_data['html'][0]['head'][0]['meta'][6]['_attributes']['content']
            
            final_urban=temp1+"<br>"
            # print(final_urban)
            return final_urban
    except:
        return "Nothing"

