#!/bin/bash

echo "Deploying the application firewall system..."

# Start Docker containers
cd docker
docker-compose up -d

# Start the central console
cd ../backend/central_console
python3 main.py &

# Start the frontend
cd ../../frontend
streamlit run app.py &

# Start the desktop agent (for testing purposes)
cd ../desktop_agent
python3 agent.py &

echo "Deployment completed by grace of devanshi. Access the web console at http://localhost:8501"
