import pandas as pd
import requests
import json
import pickle
import csv
import unittest

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
        # print "retrieving cached result for " + full_url
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
        pickle.dump(cache_diction, fobj)#turn into json file

        # json.dump()
        fobj.close()
        return response.text

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)
# print pretty(saved_cache[saved_cache.keys()[0]])

week = 1
while week < 14:
    # a = raw_input("please wait over a second to input a number..")
	dest_url = "http://api.sportradar.us/ncaafb-t1/2016/REG/{}/schedule.json?api_key=9yfg5nkfcjneyec967hr9j4r".format(week)
	d = {'format': 'json'}
	result_text = get_with_caching(dest_url, d, saved_cache, cache_fname)
	week += 1


dest_url = "http://api.sportradar.us/ncaafb-t1/2016/REG/{}/schedule.json?api_key=9yfg5nkfcjneyec967hr9j4r".format(week)
d = {'format': 'json'}
result_text = get_with_caching(dest_url, d, saved_cache, cache_fname)


def find_games(x):
    hp = []
    ap = []
    away = []
    for i in range(len(x.keys())):
        for j in range(len(json.loads(x[x.keys()[i]])['games'])):
            if json.loads(x[x.keys()[i]])['games'][j]['home'] == 'MICH':
                        hp.append(json.loads(x[x.keys()[i]])['games'][j]['home_points'])
                        ap.append(json.loads(x[x.keys()[i]])['games'][j]['away_points'])
                        away.append(json.loads(x[x.keys()[i]])['games'][j]['away'])
    return pd.DataFrame({'Home Point':hp,'Away Point':ap,'Away Team':away,'Home Team':'MICH'})

data = find_games(saved_cache)
# data.to_csv('./games.csv', index = False)
# index=false means to cancel the index

class Statistics:
    def __init__(self, competitor, home_points, away_points):
        self.competitor = competitor
        self.home_points = home_points
        self.away_points = away_points
    def CompetitorTeam(self):
        print "This season has %d of games vs. MICH" %len(self.competitor)
        return len(self.competitor)
    def MaxScore(self):
        new_list = filter(lambda i: i == 7, self.home_points)
        print "There are %d of games MICH scored 7" %len(new_list)
        return new_list

hp_lst = list(data["Home Point"])
ap_lst = list(data["Away Point"])
away = list(data["Away Team"])
game_stats = Statistics(away, hp_lst, ap_lst)
game_stats.CompetitorTeam()
game_stats.MaxScore()



# FB Data

access_token = "EAACEdEose0cBAJ0e6EKAPuibGZASJTNQNbFeIlFNy7zKzmxa8MVWt5QzMybCDHoP2wcsCcU873zYQr2DlC7S0pLVEB2n2PswfaHpRKPcUJn3N4M30D9hCL5IA1olZCNVVfENdLKN19BISICuA1zZCXDDvUGne0iNIi2avCH2wZDZD"
###The following code allows us to grade your code with graders' tokens. (It also helps you run the code if your access token has expired.) Please do not change it!
r = requests.get("https://graph.facebook.com/v2.3/me/feed",params={"limit":2, "access_token":access_token})
# print r.status_code
# if r.status_code != 200:
#    access_token = raw_input("Get a Facebook access token v2.3 from https://developers.facebook.com/tools/explorer and enter it here if the one saved in the file doesn't work anymore.  :\n")

# Group "MaizeMarket" to fetch ticket selling information
GROUP_ID = "343214415726175"

## Baseurl for the Facebook API
fb_baseurl = "https://graph.facebook.com/v2.3/{}/feed".format(GROUP_ID)
# Building the Facebook parameters dictionary
fb_params = {}
fb_params["access_token"] = access_token
fb_params["field"] = "message"


collected=[]
cached_fb={}
try:
    f = open("cached_fb.txt", "r")
    cached_fb = json.loads(f.read())
    f.close()
except:
    f = open("cached_fb.txt", "w")
    for i in range (120):
        if i == 0:
            fb_response = requests.get(fb_baseurl, params= fb_params)
        else:
            fb_response = requests.get(newurl)
        cached_fb = json.loads(fb_response.text)
        collected += cached_fb['data']
        newurl = cached_fb['paging']['next']
    cached_fb["data"] = collected
    f.write(json.dumps(cached_fb))
    f.close()

# print pretty(cached_fb)

def filter_message(x):
    raw_massage = []
    for i in x["data"]:
        # print type(i["message"])
        # print i["message"]
        # need to check if the "message" key in a post
        try:
            raw_massage.append(i["message"])
        except:
            pass
    return raw_massage

message_data = filter_message(cached_fb)
# print pretty(message_data)

class Game:
    def __init__(self, fullname, keywords, lst_message):
        self.fullname = fullname
        self.keywords = keywords
        self.lst_message = lst_message

    def filter_one(self):
        filtered_one = []
        for message in self.lst_message:
            if "basketball" not in message and "hockey" not in message:
                # use filter here instead the line above
                filtered_one.append(message)
        return filtered_one
    def filter_two(self):
         a = self.filter_one()
         filtered_two = []
         for word in self.keywords:
             for message in a:
                 if word in message:
                     filtered_two.append(message)
         return filtered_two
    def count(self):
        b = self.filter_two()
        count = len(b)
        return count


Florida = Game("UCF",["UCF","Florida","florida","ucf"],message_data)
WISC = Game("WISC",["Wisconsin","badger","Badger","wisconsin"],message_data)
Indiana = Game("Indiana",["Indiana","IU", "Hoosiers","indiana","iu"],message_data)
Colorado = Game("Colorado",["Colorado","colorado"],message_data)
Illinois = Game("Illinois",["Illinois","illinois"],message_data)
Penn = Game("Penn",["Penn","penn","psu","PSU"],message_data)
Maryland = Game("Maryland",["Maryland","maryland"],message_data)
Hawaii = Game("Hawaii",["Hawaii","hawaii"],message_data)


away = ["UCF", "ILL", "PSU", "IU", "MAR", "HAW", "COL", "WIS"]
df = [Florida.count(), Illinois.count(), Penn.count(), Indiana.count(), Maryland.count(), Hawaii.count(), Colorado.count(), WISC.count()]
df = pd.DataFrame({"Away Team": away, 'Message Count':df})
res = pd.merge(data, df, on = "Away Team")
f = open("./games.csv", "w")
res.to_csv(f, index = False)
f.close

class myTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(type(message_data), type([]), "testing type of message_data")
    def test2(self):
        self.assertEqual(len(away), 8, "testing length of away team")
    def test3(self):
        self.assertEqual(type(Florida.count()), type(8), "testing type of Florida.count()")
    def test4(self):
        self.assertEqual(type(d), type({}), "testing type of d")
    def test5(self):
        self.assertEqual(type(WISC.filter_two()), type([]), "testing type of WISC.filter_two()")
    def test6(self):
        self.assertEqual(type(WISC.filter_one()), type([]), "testing type of WISC.filter_one()")
    def test7(self):
        self.assertEqual(type(res), type(df), "testing type of res is the same as df")
    def test8(self):
        self.assertEqual(type(data), type(df), "testing type of data is the same as df")
    


unittest.main(verbosity=2)




