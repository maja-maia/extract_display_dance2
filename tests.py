from googleapiclient.discovery import build
from google.oauth2 import service_account
from time import sleep
from tkinter import *
import random
import json
import gspread
from google.oauth2.service_account import Credentials

# {'author_id': 912646231532417025, 'text': 'Welcome to Bulgaria, where the Ukraine war is NATO’s fault\n\nhttps://t.co/tPTequbbv5'}

def get_a_list_of_words():

#Shows basic usage of the Sheets API.
#Prints values from a sample spreadsheet.

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.

    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1DtZKwqfoDeSHb0mGGoeEvh_Kizfs8a42XozEh6ODaxI'
    service = build('sheets', 'v4', credentials=creds)

    #Call the Sheets API
    sheet = service.spreadsheets()
    values = sheet.values()
    content = values.get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:A")
    result = content.execute()


# TESTS WRITING INTO

# connect to your google sheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('keys.json', scopes=scope)
gc = gspread.authorize(credentials)
wks = gc.open("Extract Display Dance").sheet1

# Let's say you have some json values
j = ({'author_id': tweet['author_id'], 'text': tweet.text})
y = json.dumps(j)

result = y
#for key in y:
   # result.append([key,y[key]])

wks.update('A1', result)

# values = [
#     [
#         # Cell values ...
#     ],
#     # Additional rows ...
# ]
# body = {
#     'values': values
# }
# result = service.spreadsheets().values().update(
#     spreadsheetId=spreadsheet_id, range=range_name,
#     valueInputOption=value_input_option, body=body).execute()
# print('{0} cells updated.'.format(result.get('updatedCells')))


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
    myLabel = Label(root, text = 'whatever')
    # shoving the widget into the screen
    myLabel.pack()


    myWord = WordDisplay(myLabel)
    myWord.draw()
    root.mainloop()

if __name__ == '__main__':
    main()