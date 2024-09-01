#!/bin/bash

echo "Setting up the application firewall project environment..."

# Update and install necessary packages
sudo pacman -Syu --noconfirm
sudo pacman -S docker docker-compose python python-pip git appwrite prometheus grafana --noconfirm

# Install Python dependencies
python -m venv devanshi
Source devanshi/bin/activate
pip install streamlit pyqt5 xgboost scikit-learn prometheus_client
pip freeze >> requirements.txt

# Set up Docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Set up Appwrite
cd backend/appwrite/setup
bash appwrite-setup.sh

# Set up Prometheus
bash prometheus-setup.sh

# Set up Grafana
bash grafana-setup.sh

# Build Docker images
cd ../../../docker
docker-compose build

echo "Devanshi made the code sucessful."
