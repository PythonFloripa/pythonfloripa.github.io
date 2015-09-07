#!/bin/bash

set -e


echo "Updating remotes..."
git remote add deploy git@github.com:PythonFloripa/pythonfloripa.github.io.git || echo "Remote deploy already exists:"
git remote -v


echo "Set up deploy key..."
openssl aes-256-cbc -K $encrypted_63aef70bd380_key -iv $encrypted_63aef70bd380_iv \
    -in deploy_key.pem.enc -out deploy_key.pem -d
chmod 600 deploy_key.pem
eval $(ssh-agent)
ssh-add deploy_key.pem


echo "Running mkdocs gh-deploy"
mkdocs gh-deploy --verbose --clean --remote-branch master --remote-name deploy
