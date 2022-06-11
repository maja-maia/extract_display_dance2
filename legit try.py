import tweepy
import time
import json


##################
# Authentication #
##################
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALn0cwEAAAAAglFN63i84ia9ZmYjuTqpPpTz8As%3DXcg9XBg2fDc6vu9b5oWnU4FOKNOD3TKzH9EVDdKXSs4uwe7WtZ"

client = tweepy.Client(bearer_token= BEARER_TOKEN,wait_on_rate_limit=True)

#####################
# Search for Tweets #
#####################

# https://docs.tweepy.org/en/stable/client.html#tweepy.Client.search_recent_tweets
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query

# - means NOT
search_query = "war -is:retweet lang:en" # SEARCHING FOR WORD 'python' + not retweets + in English
for n in [1,2,3,4,5,6,7,8,9]:
    cursor = tweepy.Paginator(
    method=client.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics'],
).flatten(limit=2)
tweets = []
for tweet in cursor:
    #print(tweet.text+'\n') # NOTICE THAT WE ARE PRINTING ONLY TEXT
    print('\n\n-----NEXT TWEET------\n\n')
    #tweets.append({'author_id': tweet['author_id'], 'text': tweet.text})
    j = ({'author_id': tweet['author_id'], 'text': tweet.text})
    #z = [x for x in a ]
    with open('tweets.json', 'w') as out:json.dump(j,out)
    #files.download('tweets.json')
    print(j)
    time.sleep(15) # Sleep for 15 seconds

    import json
    import gspread
    from google.oauth2.service_account import Credentials

    # connect to your google sheet
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file('extract-display-dance-4a3ec1e27340.json', scopes=scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("Extract Display Dance").sheet1

    # Let's say you have some json values
    j = ({'text': tweet.text, 'author_id': tweet['author_id']})
    y = json.dumps(j)

    result = y
    # for key in y:
    # result.append([key,y[key]])

    row = list(j.values())
    wks.insert_row(row)
    print("The row has been added")

    from googleapiclient.discovery import build
    from google.oauth2 import service_account
    from time import sleep
    from tkinter import *
    import random


    def get_a_list_of_words():

        # Shows basic usage of the Sheets API.
        # Prints values from a sample spreadsheet.

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        SERVICE_ACCOUNT_FILE = 'extract-display-dance-4a3ec1e27340.json'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        creds = None
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # The ID of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = '1tsY0r9Xa4oUeRhGIpxxaxpKPZoJCInrQaVVgCD0PdaU'
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        values = sheet.values()
        content = values.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:A")
        result2 = content.execute()

        # pprint.pprint(result.get('values', []))
        return result2.get('values', [])


    def pick_a_word(list_of_words):

        # get some sort of random word function
        return random.choice(list_of_words)


    class WordDisplay:
        def __init__(self, myLabel):
            self.myLabel = myLabel

        def draw(self):
            column_contents = get_a_list_of_words()
            wordyword = pick_a_word(column_contents)
            self.myLabel.config(text=wordyword)

            self.myLabel.after(3000, self.draw)


    def main():
        root = Tk()
        # creating a Label widget
        myLabel = Label(root, text='whatever')
        # shoving the widget into the screen
        myLabel.pack()

        myWord = WordDisplay(myLabel)
        myWord.draw()
        root.mainloop()


    if __name__ == '__main__':
        main()