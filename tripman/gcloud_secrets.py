import os

from google.cloud import secretmanager
from io import StringIO

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", 'tripman')


def get_gcloud_secret(name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{name}/versions/latest"
    response = client.access_secret_version(name=name)
    payload = response.payload.data.decode("UTF-8")
    return StringIO(payload)
