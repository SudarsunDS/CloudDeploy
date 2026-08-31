#!/bin/bash

# ==========================================
# CloudDeploy - IBM Cloud Deployment Script
# ==========================================

APP_NAME="clouddeploy"

REGISTRY_NAMESPACE="YOUR_NAMESPACE"

REGION="us-south"

IMAGE_NAME="$REGISTRY_NAMESPACE/$APP_NAME"

echo "Logging into IBM Cloud..."

ibmcloud login


echo "Selecting IBM Cloud Container Registry region..."

ibmcloud cr region-set $REGION


echo "Logging into Container Registry..."

ibmcloud cr login


echo "Building Docker image..."

docker build -t $IMAGE_NAME:latest .


echo "Pushing image to IBM Cloud Container Registry..."

docker push $IMAGE_NAME:latest


echo "Deploying application to IBM Code Engine..."

ibmcloud ce application create \
    --name $APP_NAME \
    --image $IMAGE_NAME:latest \
    --port 8080 \
    --min-scale 0 \
    --max-scale 5


echo "Deployment completed successfully."
