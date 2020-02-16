from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def main():
   
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret_514215414527-hhhruimjvtvtjpru4c8uai2o5uc4ujsa.apps.googleusercontent.com.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    
    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me',labelIds = ['INBOX'], maxResults = 20, q = 'reject').execute()
    messages = results.get('messages', [])

    userInfo = service.users().getProfile(userId='me').execute()
    print(userInfo)
    

    if not messages:
        print ("No messages found.")
    else:
        print ("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print (msg['snippet'])
            print(len(msg))

if __name__ == '__main__':
    main()
