import requests
import json
import pickle

cache_fname = "srcached_results.txt"
try:
    fobj = open(cache_fname, 'r')
    saved_cache = pickle.load(fobj)
    fobj.close()
except:
    saved_cache = {}

def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res

def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url

def get_with_caching(base_url, params_diction, cache_diction, cache_fname):
    full_url = requestURL(base_url, params_diction)
    # step 1
    if full_url in cache_diction:
        # step 2
        print "retrieving cached result for " + full_url
        return cache_diction[full_url]
    else:
        # step 3
        a = raw_input("please wait over a second to input a number..")
        response = requests.get(base_url, params=params_diction)
        print "adding cached result for " + full_url
        # add to the cache and save it permanently
        cache_diction[full_url] = response.text
        # cache_diction[full_url] = response.json() # json.loads(response.text)
        fobj = open(cache_fname, "w")
        pickle.dump(cache_diction, fobj)

        # json.dump()
        fobj.close()
        return response.text

# def pretty(obj):
#     return json.dumps(obj, sort_keys=True, indent=2)

# print pretty(saved_cache[saved_cache.keys()[0]])

week = 1

caching_dic={}


while week < 14:
    # a = raw_input("please wait over a second to input a number..")
	dest_url = "http://api.sportradar.us/ncaafb-t1/2016/REG/{}/schedule.json?api_key=9yfg5nkfcjneyec967hr9j4r".format(week)
	d = {'format': 'json'}
	result_text = get_with_caching(dest_url, d, saved_cache, cache_fname)
	week += 1
	
# print json.loads(result_text)

# print result_text
# r = open(cache_fname,"r")
# test = pickle.load(r)

# def pretty(obj):
#    return json.dumps(obj, sort_keys=True, indent=2)
# print pretty(test)

# print type(saved_cache)
# print saved_cache.keys()




# import unittest
# import string
# import requests
# import json
# from pprint import pprint
# import pickle

# cache_fname = "srcached_results.txt"
# try:
#     fobj = open(cache_fname, 'r')
#     saved_cache = pickle.load(fobj)
#     fobj.close()
# except:
#     saved_cache = {}

# week = 1
# #r = requests.get("https://graph.facebook.com/v2.3/me/feed",params={"limit":2})
# baseurl = "http://api.sportradar.us/ncaafb-t1/2016/REG/{}/schedule.json?api_key=9yfg5nkfcjneyec967hr9j4r".format(week)
# url_params = {}
# url_params["fields"] = "games{home, away, home_points, away_points}"

# collected=[]
# sr_data={}
# r = requests.get(baseurl,params=url_params)
# temp = json.loads(r.text)

# for i in temp["games"]["home"]:
# 	if i == "MICH":
# 		collected += (temp["games"]["home"], temp["game"]["away"], temp["game"]["home_points"], temp["game"]["away_points"])
# 	else:
# 		collected += []
# #collected += temp["data"]
# sr_data['data']= collected
# print sr_data["data"]

