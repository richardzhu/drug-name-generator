#!/bin/bash

# rsync this folder to tinyhack instance
# !! make sure rsync is installed on destination machine
rsync -Pavz --exclude='.git*' --filter="dir-merge,-n /.gitignore" ./ richardzhu@$(gcloud compute instances list --filter="name=tinyhack" --format "get(networkInterfaces[0].accessConfigs[0].natIP)"):~/drug-name-generator

