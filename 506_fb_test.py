#final project testing
import unittest
import string
import requests
import json
from pprint import pprint

#def pretty(obj):
#    return json.dumps(obj, sort_keys=True, indent=2)

access_token = "EAACEdEose0cBAGtUla9F82hrSGYaGQA58c8huaEybTEuT4RqjYJ3mpys5ANMLeDmwsiCknEIa4SXNtn0ZCn5UenJIltsasEmNhGv60wmuQr0srHPTZBhTa9EpiFXRm830KjBZA7mJGxZCjLGR5Ee4RRZCVmZA1LIzSdQ8Gm2DdygZDZD"

###The following code allows us to grade your code with graders' tokens. (It also helps you run the code if your access token has expired.) Please do not change it!
r = requests.get("https://graph.facebook.com/v2.3/me/feed",params={"limit":2, "access_token":access_token})
# print r.status_code
#if r.status_code != 200:
#    access_token = raw_input("Get a Facebook access token v2.3 from https://developers.facebook.com/tools/explorer and enter it here if the one saved in the file doesn't work anymore.  :\n")

# Group "MarketNoire" to fetch ticket selling information
GROUP_ID = "397389103642039"

## Baseurl for the Facebook API

baseurl = "https://graph.facebook.com/v2.3/{}/feed".format(GROUP_ID)

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
url_params["fields"] = "comments{comments{like_count,from,message,created_time},like_count,from,message,created_time},likes,message,created_time,from" 
# Parameter key-value so you can get post message, comments, likes, etc. as described in assignment instructions.
# Write code to make a request to the Facebook API using paging and save data in fb_data here.
collected=[]
sr_data={}

r = requests.get(baseurl,params=url_params)
temp = json.loads(r.text)
collected += temp["data"] # return --[u'created_time', u'message', u'from', u'id', u'updated_time']
fb_data['data']=collected
print fb_data["data"]




