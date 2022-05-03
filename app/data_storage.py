# data_storage.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()


def load_auth():

    load_dotenv()
    DOCUMENT_ID = os.getenv("GOOGLE_SHEET_ID", default="OOPS")
    SHEET_NAME = os.getenv("SHEET_NAME", default="OOPS")

    # code adapted from https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/gspread.md

    #
    # AUTHORIZATION
    #
    # see: https://gspread.readthedocs.io/en/latest/api.html#gspread.authorize
    # ... and FYI there is also a newer, more high level way to do this (see the docs)

    # an OS-agnostic (Windows-safe) way to reference the "auth/google-credentials.json" filepath:
    CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "../google-credentials.json")

    AUTH_SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
        "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)
    print("CREDS:", type(credentials)) #> <class 'oauth2client.service_account.ServiceAccountCredentials'>

    client = gspread.authorize(credentials)
    print("CLIENT:", type(client)) #> <class 'gspread.client.Client'>

    doc = client.open_by_key(DOCUMENT_ID)
    sheet = doc.worksheet(SHEET_NAME)
    rows = sheet.get_all_records()

    return sheet, rows


def read_sheet():

    sheet, rows = load_auth()

    users_dict = []

    #
    # READ SHEET VALUES
    #
    # see: https://gspread.readthedocs.io/en/latest/api.html#client
    # ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Spreadsheet
    # ...  https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet

    print("---------------------------------")
    print("READING DOCUMENT...")

    for row in rows:
        users_dict.append(row)

    return users_dict


def write_sheet(user_name, user_email, user_country, user_category):

    sheet, rows = load_auth()

    #
    # WRITE VALUES TO SHEET
    #
    # see: https://gspread.readthedocs.io/en/latest/api.html#gspread.models.Worksheet.insert_row

    print("-----------------")
    print("NEW ROW...")

    new_row = {
        "Name": user_name,
        "Email": user_email,
        "Country": user_country,
        "Category": user_category,
    }
    print(new_row)

    print("-----------------")
    print("WRITING VALUES TO DOCUMENT...")

    # the sheet's insert_row() method wants our data to be in this format (see docs):
    new_values = list(new_row.values())

    # the sheet's insert_row() method wants us to pass the row number where this will be inserted (see docs):
    next_row_number = len(rows) + 2 # number of records, plus a header row, plus one

    # actually insert the data:
    response = sheet.insert_row(new_values, next_row_number)

    # see if it worked ok:
    print("RESPONSE:", type(response)) #> dict
    print(response) #> {'spreadsheetId': '____', 'updatedRange': "'Products-2021'!A9:E9", 'updatedRows': 1,
                    # 'updatedColumns': 5, 'updatedCells': 5}


if __name__ == "__main__":

    dict = read_sheet()
    print(dict)
    write_sheet("Krish", "ks1730@georgetown.edu", "in", "general")
