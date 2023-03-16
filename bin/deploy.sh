#!/usr/bin/env bash
# Usage: bin/deploy.sh
# Usage: bin/deploy.sh --tag=name
# Usage: bin/deploy.sh --tag=name --no-traffic
# Description: Deploy the app to Google Cloud Run

gcloud run deploy tripman --source . --region us-central1 --allow-unauthenticated "$@"
