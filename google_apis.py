import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

def create_service(client_secret_file, api_name, api_version, scopes, prefix=''):
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = scopes

    creds = None
    working_dir = os.getcwd()
    token_dir = 'token files' #dont need underscore?
    token_file = f'token_{API_SERVICE_NAME}_{API_VERSION}{prefix}.json'


    ###check if token dir exists first, if not create the folder
    #os.path.join probs just makes it cwd/token_dir
    if not os.path.exists(os.path.join(working_dir, token_dir)):
        os.mkdir(os.path.join(working_dir, token_dir))
    


    ###set credentials

    #first, retrieve existing token (if one exists)
    #after this, creds will either be a valid token, an expired token, or remain as None if file doesnt exist yet
    if os.path.exists(os.path.join(working_dir, token_dir, token_file)):
        creds = Credentials.from_authorized_user_file(os.path.join(working_dir, token_dir, token_file), SCOPES)
    
    #if creds is None, or expired, refresh or create new token
    #after this, creds will always be valid new token no matter what
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            #this flow is the point where users redirected and give permission to the scope, before token is received
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        #update token file with new creds first for storage
        with open(os.path.join(working_dir, token_dir, token_file), 'w') as token:
            token.write(creds.to_json())
    


    ###finally, use token to build and return the service. this gives client access to the APIs
    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=creds, static_discovery=False)
        print(API_SERVICE_NAME, API_VERSION, 'service created successfully') #whats the diff betw this and format strings? 
        return service
    except Exception as e:
        print(e)
        print(f'failed to create service instance for {API_SERVICE_NAME}')
        os.remove(os.path.join(working_dir, token_dir, token_file))
        return None
              
    
