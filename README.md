# rwby-spider
A spider to download all images from the r/RWBY subreddit flaired as fanart

# Details
Uses Leonardicus' [imgurdl.py](https://github.com/leonardicus/imgurdl) to download imgur links from the rwby subreddit.  
Also piggybacks on the Velvet Bot for non-imgur submissions. Apologizes for letting the faunus do all my dirty work :S .


# Usage

1. Make sure praw is installed in your python 3.2+ environment.

2. Apply for a script app by going to the [reddit app section](https://www.reddit.com/prefs/apps). Record the Application ID and secret.  
\*NOTE: You can read more about [creating bots](https://github.com/reddit/reddit/wiki/OAuth2) and the [reddit API](http://www.reddit.com/dev/api) if you wish.

3. Create a file named "creds.key" with the following four lines:  
	- Username  
	- Password  
	- Application ID  
	- Secret

4. Run **RwbySpider.py**. Random debug stuff will spew out but everything should be downloaded to /RWBY/

# Todo

[ ] Run on double-click
[ ] Do not create new folders for albums
[ ] Create folders to sort by post date (easier to group)
[ ] My own imgur downloader so I don't have to use Leonardicus' work