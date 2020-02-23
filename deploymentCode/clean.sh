#!/bin/bash

# Export kube config file
export KUBECONFIG="/var/lib/jenkins/secrets/kubeconfig.yml"

# Stage the application and get the URL for the version 2 of the image
rio rm $(rio ps | awk 'NR>1{print $1}' | tr "\n" " ")

# Deploy the initial appliation back
rio run -p 80:5000/http --scale 1-10 --name devcon kingalt/flask:1.0

echo "{\"name\":\"kingalt/flask:1.0\"}" > metadata.json

