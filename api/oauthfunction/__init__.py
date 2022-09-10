import logging

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import azure.functions as func
from azure.keyvault.secrets import SecretClient
import json
from azure.identity import ManagedIdentityCredential, DefaultAzureCredential
from os import environ

token_url = "https://api.os.uk/oauth2/token/v1"

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Running oauth function")
        identity = DefaultAzureCredential()
        logging.info('Python HTTP trigger function processed a request.')
        secretClient = SecretClient(vault_url="https://dhirst-kv.vault.azure.net/", credential=identity)
        logging.info("Authenticated")
        project_api_key = secretClient.get_secret('project-api-key').value

        client_secret = secretClient.get_secret('client-secret').value
    except:
        project_api_key = environ.get("project_api_key")
        client_secret = environ.get("client_secret")

    logging.info("Got api key and secret")
    client = BackendApplicationClient(client_id=project_api_key)
    oauth = OAuth2Session(client=client)
    logging.info("Connected to oauth client")
    token = oauth.fetch_token(token_url=token_url, client_id=project_api_key,
                              client_secret=client_secret)
    logging.info('Got token')
    return json.dumps(token)

    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)