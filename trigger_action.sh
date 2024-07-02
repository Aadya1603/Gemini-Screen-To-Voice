#!/bin/bash

# Replace these variables with your own values
GH_TOKEN=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
REPO_OWNER=Aadya1603
REPO_NAME=Gemini-Screen-To-Voice

curl -X POST \
-H "Accept: application/vnd.github.v3+json" \
-H "Authorization: token $GH_TOKEN" \
https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/dispatches \
-d '{"event_type":"start-application"}'
