import praw
import requests
import json
import requests.auth

creds = []
with open('creds.key', 'r') as f: # wow much secure
    creds = f.read().splitlines()

# Request a token with post @reddit.com
headers = {"User-Agent": "u/mserob test"}
post_data = {"grant_type": "password", "username": creds[0], "password": creds[1]}
client_auth = requests.auth.HTTPBasicAuth(creds[2], creds[3])
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
r = response.json()

# Retrieve links of all fan art hosted on imgur
urls = list()
headers = {"Authorization": "bearer " + r['access_token'], "User-Agent": "u/mserob test"}
payload = {
	"limit": 100,
	"q": "flair:art site:imgur.com",
	"sort": "new",
	"t": "month",
	"restrict_sr": 1
	}
response = requests.get("https://oauth.reddit.com/r/rwby/search", headers=headers, params=payload)
j = response.json()
a = j["data"]["children"]
for i in a:
	urls.append(i["data"]["url"])
	print("geto")

payload = {
	"limit": 100,
	"sort": "new",
	"t": "month",
	}
response = requests.get("https://oauth.reddit.com/user/velvetbot/comments", headers=headers, params=payload)
j = response.json()
a = j["data"]["children"]
af = j["data"]["after"]
for i in a:
	t = i["data"]["body"]
	if(t.find('[Imgur](') > 0):
		urls.append(t[t.find('[Imgur](')+8:t.find(')',t.find('[Imgur]('))])
		print("velvet")
#import pickle
#with open('data.pickle', 'wb') as fi:
#	pickle.dump(urls, fi, pickle.HIGHEST_PROTOCOL)
#with open('data.txt', 'w') as fo:
#	for item in urls:
#		fo.write("{}\n".format(item))

#Download all imgur links
from imgurdl import ImgurDL
id = ImgurDL()
id.use_default_directory = False
id.output_dir = "RWBY"
for u in urls:
	if id.is_album(u):
		id.token_list.add((id.parse_token(u), "album"))
	else:
		id.token_list.add((id.parse_token(u), "image"))
id.extract_urls(id.token_list)
id.save_images()