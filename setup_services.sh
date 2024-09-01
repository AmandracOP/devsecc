#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to install Docker if it's not installed
install_docker() {
    if ! [ -x "$(command -v docker)" ]; then
        echo "Docker not found. Installing Docker..."
        curl -fsSL https://get.docker.com -o get-docker.sh
        sh get-docker.sh
        rm get-docker.sh
    else
        echo "Docker is already installed."
    fi
}

# Function to set up Grafana
setup_grafana() {
    echo "Setting up Grafana..."
    docker run -d --name=grafana -p 3000:3000 grafana/grafana

    # Wait for Grafana to start
    sleep 15

    # Set up Prometheus as a data source (this assumes Prometheus is running on localhost:9090)
    echo "Adding Prometheus as a data source to Grafana..."
    curl -X POST -H "Content-Type: application/json" -d '{
      "name": "Prometheus",
      "type": "prometheus",
      "url": "http://localhost:9090",
      "access": "proxy",
      "basicAuth": false
    }' http://admin:admin@localhost:3000/api/datasources
}

# Function to set up Appwrite
setup_appwrite() {
    echo "Setting up Appwrite..."
    docker run -d --name=appwrite -p 80:80 -p 443:443 appwrite/appwrite

    # Wait for Appwrite to start
    sleep 15

    echo "Appwrite is set up. Please complete the setup via the web UI at http://localhost."
}

# Function to update config.py with Grafana and Appwrite information
update_config() {
    echo "Updating config.py with service information..."
    
    GRAFANA_URL="http://localhost:3000"
    APPWRITE_URL="http://localhost/v1"
    APPWRITE_PROJECT_ID="66d39066000c552c0cb0"  # Replace with actual project ID
    APPWRITE_API_KEY="a19f336a167150b64e3ad38d7e7cd0a4e0f07f59f694d90d9739bf1d3d7a001f54e896d25e7dc66656d9aec27859193c488439fbe1310bc0b1268b688ea95091bb8328b7d0b24851ef8c952aa410bf37a57f6f110dd087b49c7c19c220d5ebbef367b566175df88106db622033ca539395b2c9ece4c0cb3d405bba2f562345a0"        # Replace with actual API key

    cat <<EOF > config.py
# Configuration file for the project

GRAFANA_URL = "$GRAFANA_URL"
APPWRITE_URL = "$APPWRITE_URL"
APPWRITE_PROJECT_ID = "$APPWRITE_PROJECT_ID"
APPWRITE_API_KEY = "$APPWRITE_API_KEY"

# Other configuration settings...
EOF

    echo "config.py updated successfully."
}

# Function to display usage instructions
display_usage() {
    echo "Usage: ./setup_services.sh"
    echo "This script installs Docker (if not already installed), sets up Grafana and Appwrite, and updates config.py with the necessary configurations."
}

# Main script execution
install_docker
setup_grafana
setup_appwrite
update_config

echo "Setup complete. Please verify the configuration and services."
