import praw
from datetime import datetime

print('[+] Logging you in to reddit:')

#Authenticating with reddit using username, password & storing in a variable.
reddit = praw.Reddit(client_id="uN_KLCjgW68dMQ", client_secret="r61ahO-jqiU43An94Gt5NxgZYOQ", password="2pKxN7kvsVC6QRV", user_agent="Scraping", username="flopyash")
print('[+] Successfully Logged in')

#Example: superlogout.com
a= str(input('Enter Link to crawl(Ex-google.com):'))
def main():
 # red is a variable searching through all the subchannels.
 red = reddit.subreddit("all")
 for i in red.search(a, limit=25):
    print("\n")
    print("  Comment ID: ",i.id)
    print("  Post Title: ",i.title.encode('ascii', 'ignore')) 
    print("  Post Score: ",i.score)
    #print("  URL: ",i.url.encode('ascii', 'ignore')) 
    print("  Text: ",i.selftext[:200].encode('ascii', 'ignore'))
    print("  Author: ",i.author) # include
    print(" URL: ",i.url)
    print("  Time: ",str(datetime.fromtimestamp(i.created_utc))) # include
    print("\n")

main()



#dict = {'ID':i.id}
#print(dict)
#import json

#def _write_json(filename, overview):
#        with open(filename, "w", encoding = "utf-8") as results:
#            json.dump(overview, results, indent = 4)

