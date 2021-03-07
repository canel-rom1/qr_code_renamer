#!/usr/bin/env python3

from __future__ import print_function
import connect
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
SPREADSHEETS_SCOPE = ['https://www.googleapis.com/auth/spreadsheets']


def get_google_service(service, scopes, version):
    """Return a googleapiclient.discovery.Resource class
    Connect to my drive
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens,
    # and is created automatically when the authorization flow
    # completes for the first time.
    token = "%s.pickle" % (service)
    if os.path.exists(token):
        with open(token, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save  the credentials for the next run
        with open(token, 'wb') as token:
            pickle.dump(creds, token)
    service = build(service, version, credentials=creds)
    return service
