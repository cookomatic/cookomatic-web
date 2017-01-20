#!/usr/bin/env bash

echo -e "\n## Installing App Engine Python SDK"

if [ ! -d "${GAE_PYTHONPATH}" ]; then
    python ./ci/fetch_gae_sdk.py $(dirname "${GAE_PYTHONPATH}");
fi

# If the SDK is not already cached, download it and unpack it
if [ ! -d ${HOME}/google-cloud-sdk/bin ]; then
    rm -rf ${HOME}/google-cloud-sdk;
    export CLOUDSDK_CORE_DISABLE_PROMPTS=1;
    curl https://sdk.cloud.google.com | bash;
fi

echo -e "\n## Authenticating to Google Cloud Platform"
# Decrypt the credentials we added to the repo using the key we added with the Travis command line tool
openssl aes-256-cbc -K $encrypted_781b2254b6c6_key -iv $encrypted_781b2254b6c6_iv -in client-secret.json.enc -out client-secret.json -d

# Here we use the decrypted service account credentials to authenticate the command line tool
gcloud auth activate-service-account --key-file ./ci/client-secret.json

echo -e "\n## Installing Python dependencies"
pip install -r requirements.txt
pip install -r requirements.txt -t lib/
