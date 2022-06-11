from googleapiclient.discovery import build
from google.oauth2 import service_account
from time import sleep
from tkinter import *
import random



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

    #pprint.pprint(result.get('values', []))
    return result.get('values', [])


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