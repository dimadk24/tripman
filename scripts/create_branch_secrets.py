#!/usr/bin/env python3
import os

from google.api_core.exceptions import PermissionDenied
from google.cloud import secretmanager

from tripman.gcloud_secrets import secrets_parent, branch_settings_name, \
    project_id, get_gcloud_secret, branch_name

PROD_DATABASE_URL = os.getenv('PROD_DATABASE_URL')


def create_branch_secrets(payload):
    client = secretmanager.SecretManagerServiceClient()
    try:
        get_gcloud_secret(branch_settings_name)
    except PermissionDenied:
        print(
            f"No secret exists for \"{branch_name}\" branch or don't have "
            f"access, creating...")
        response = client.create_secret(
            request={
                "parent": secrets_parent,
                "secret_id": branch_settings_name,
                "secret": {"replication": {"automatic": {}}},
            }
        )
        print(f'Created new secret {response.name}')
    # Build the resource name of the parent secret.
    parent = client.secret_path(project_id, branch_settings_name)

    # Convert the string payload into a bytes. This step can be omitted if you
    # pass in bytes instead of a str for the payload argument.
    payload = payload.encode("UTF-8")

    # Add the secret version.
    response = client.add_secret_version(
        request={
            "parent": parent,
            "payload": {"data": payload},
        }
    )
    print(f'Added new version with branch secrets to secret {response.name}')


def create_secret_payload():
    return PROD_DATABASE_URL.replace('_prod', f'_{branch_name}')


if __name__ == '__main__':
    create_branch_secrets(create_secret_payload())
