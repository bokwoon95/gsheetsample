import xml.etree.ElementTree as ElementTree
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Enter your Spreadsheet ID here
# Spreadsheet ID is found in the google sheet's URL between '/d/' and '/edit#gid'
# e.g. the ID of https://docs.google.com/spreadsheets/d/1_9T4Wik9u6v7tBOORhurPPF4YLCjQMw03kvTdp3I1Gk/edit#gid=0 is 1_9T4Wik9u6v7tBOORhurPPF4YLCjQMw03kvTdp3I1Gk
SPREADSHEET_ID = '1_9T4Wik9u6v7tBOORhurPPF4YLCjQMw03kvTdp3I1Gk'

def authenticate_google_sheets():
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', 'https://www.googleapis.com/auth/spreadsheets')
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    return service


def main():

    # Extract all 'variable' tag items from xml file
    variables = ElementTree.parse('SampleProfile.xml').find('profile').find('variablecollection').findall('variable')

    # Parse variables xml object into a list of lists
    values = []
    for vee in variables:
        name = vee.attrib['name']
        value = vee.find('value').text
        values.append([name, value])
    print(values)

    # Authenticate google sheets
    service = authenticate_google_sheets()

    # Copy parsed xml data into google sheet
    result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range='A:B',
            valueInputOption='RAW',
            body={'values':values}
            ).execute()
    print(result)


if __name__ == '__main__':
    main()
