import logging

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import azure.functions as func
from azure.keyvault.secrets import SecretClient
import json
from azure.identity import ManagedIdentityCredential, DefaultAzureCredential

token_url = "https://api.os.uk/oauth2/token/v1"

def main(req: func.HttpRequest) -> func.HttpResponse:
    identity = DefaultAzureCredential()
    logging.info('Python HTTP trigger function processed a request.')
    secretClient = SecretClient(vault_url="https://dhirst-kv.vault.azure.net/", credential=identity)
    project_api_key = secretClient.get_secret('project-api-key').value

    client_secret = secretClient.get_secret('client-secret').value
    
    client = BackendApplicationClient(client_id=project_api_key)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=project_api_key,
                              client_secret=client_secret)

    return json.dumps(token)