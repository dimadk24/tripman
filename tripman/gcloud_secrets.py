import os
import warnings
from io import StringIO

from environ import Env
from google.api_core.exceptions import PermissionDenied
from google.cloud import secretmanager

env = Env()
DEFAULT_MAIN_BRANCH = 'master'

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
is_deployed = env.bool("DEPLOYED", '')
branch_name = os.getenv('BRANCH_NAME', '').replace('-', '_')
base_settings_name = 'django_settings'
branch_settings_name = f'{base_settings_name}_{branch_name}'
secrets_parent = f'projects/{project_id}'


def get_gcloud_secret(name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"{secrets_parent}/secrets/{name}/versions/latest"
    response = client.access_secret_version(name=name)
    payload = response.payload.data.decode("UTF-8")
    return StringIO(payload)


def read_secrets_to_env():
    if is_deployed:
        try:
            branch_settings = get_gcloud_secret(branch_settings_name)
            env.read_env(branch_settings)
        except PermissionDenied as error:
            if branch_name != DEFAULT_MAIN_BRANCH:
                warnings.warn(
                    "Branch secret doesn't exist or there's no permission:")
                print(error)

        base_secrets = get_gcloud_secret(base_settings_name)

        env.read_env(base_secrets)  # doesn't override branch secrets
