import argparse
import requests
import io
import os
import httplib2
import json

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build


PROJECT_ID = os.getenv('PROJECT_ID')
SCOPES = [
    'https://www.googleapis.com/auth/firebase.remoteconfig',
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/cloud-platform.read-only',
    'https://www.googleapis.com/auth/firebase',
    'https://www.googleapis.com/auth/firebase.readonly'
]

# [START retrieve_access_token]
def _get_access_token():
  """Retrieve a valid access token that can be used to authorize requests.
  :return: Access token.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', SCOPES)
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token
# [END retrieve_access_token]


def _getConfig():
    """Retrieve the current Firebase Config template from server.
    Retrieve the current Firebase Config template from server and store it
    locally.
    """
    headers = {
        'Authorization': 'Bearer ' + _get_access_token()
    }
    credentials = ServiceAccountCredentials.from_json_keyfile_name( 'service-account.json', scopes=SCOPES)
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build("firebase", "v1beta1", http=http)
    projects = service.projects().webApps()
    webapps = projects.list(parent="projects/didi-dito-trevor").execute()
    webapp_id = webapps["apps"][0]["appId"]
    name = "projects/{}/webApps/{}/config".format(PROJECT_ID, webapp_id)
    print("Getting firebase-config for app {}".format(name))
    config = projects.getConfig(name=name).execute()
    with open("firebase-config.json", "w") as file:
        json.dump(config, file)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--action')
  parser.add_argument('--etag')
  parser.add_argument('--version')
  args = parser.parse_args()

  if args.action and args.action == 'getConfig':
    _getConfig()
  else:
    print('''Invalid command. Please use one of the following commands:
python configure.py --action=get
python configure.py --action=publish --etag=<LATEST_ETAG>
python configure.py --action=versions
python configure.py --action=rollback --version=<TEMPLATE_VERSION_NUMBER>''')



if __name__ == '__main__':
  main()
