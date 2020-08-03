import praw
print('[+] Logging you in to reddit:')
reddit = praw.Reddit(client_id="uN_KLCjgW68dMQ", client_secret="r61ahO-jqiU43An94Gt5NxgZYOQ", password="2pKxN7kvsVC6QRV", user_agent="Scraping", username="flopyash")
print('[+] Successfully Logged in')
#Example: superlogout.com
a= str(input('Enter Link to crawl(Ex-google.com):'))
def main():

 all = reddit.subreddit("all")
 for i in all.search(a, limit=25):
    print("\n")
    print("  ID: ",i.id)
    print("  Title: ",i.title.encode('ascii', 'ignore'))
    print("  Score: ",i.score)
    print("  URL: ",i.url.encode('ascii', 'ignore'))
    print("  Text: ",i.selftext[:120].encode('ascii', 'ignore'))
    print("  Author: ",i.author)
    print("  URL: ",i.url)
    print("\n")

main()



#dict = {'ID':i.id}
#print(dict)
#import json

#def _write_json(filename, overview):
#        with open(filename, "w", encoding = "utf-8") as results:
#            json.dump(overview, results, indent = 4)

