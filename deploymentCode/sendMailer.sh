#!/bin/bash

# Export the kube config file
export KUBECONFIG="$(k3d get-kubeconfig --name=masters)"

# Sendgrid credentails
mailReceiver=""
mailSender=""
mailSubject="New Version of the Image"
#mailApiKey=""
mailApiKey=""
mailApiUser=""

# Stage the application and get the URL for the version 2 of the image
rio stage --image kingalt/flask:1.1 devcon version2

sleep 2

TEST_URL=$(rio ps | grep version2 | awk '{print $3}')

mailBody="Use this ${TEST_URL} URL to verify new changes"

# Sendgrid api to send email
curl -d "to=$mailReceiver&fromname=$mailSender&subject=$mailSubject&text=$mailBody&from=$mailSender&api_user=$mailApiUser&api_key=$mailApiKey" https://api.sendgrid.com/api/mail.send.json
