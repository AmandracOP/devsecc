from flask import Flask, request, jsonify
from models import session, FirewallPolicy, NetworkLog, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Function to create a default user
def create_default_user():
    default_username = "devanshi"
    default_password = "devanshi"

    # Check if the default user already exists
    user = session.query(User).filter_by(username=default_username).first()
    if not user:
        # Create the default user if it doesn't exist
        new_user = User(username=default_username, password=default_password)
        session.add(new_user)
        session.commit()

# User authentication (simplified)
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = session.query(User).filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# Get firewall policies
@app.route('/firewall/policies', methods=['GET'])
def get_policies():
    policies = session.query(FirewallPolicy).all()
    return jsonify([{
        'id': policy.id,
        'app_name': policy.app_name,
        'domain': policy.domain,
        'protocol': policy.protocol,
        'action': policy.action
    } for policy in policies])

# Add or update firewall policy
@app.route('/firewall/policy', methods=['POST'])
def add_policy():
    data = request.json
    policy = FirewallPolicy(
        app_name=data['app_name'],
        domain=data['domain'],
        protocol=data['protocol'],
        action=data['action']
    )
    session.add(policy)
    session.commit()
    return jsonify({'message': 'Policy added/updated successfully'}), 201

# Monitor network traffic logs
@app.route('/network/logs', methods=['GET'])
def get_logs():
    logs = session.query(NetworkLog).all()
    return jsonify([{
        'id': log.id,
        'app_name': log.app_name,
        'domain': log.domain,
        'protocol': log.protocol,
        'packet_size': log.packet_size,
        'is_anomalous': log.is_anomalous
    } for log in logs])

# Handle network anomaly detection (dummy implementation)
@app.route('/network/anomaly', methods=['POST'])
def detect_anomaly():
    data = request.json
    # Here, you would apply the AI/ML model to detect anomalies
    is_anomalous = False  # Placeholder result
    log = NetworkLog(
        app_name=data['app_name'],
        domain=data['domain'],
        protocol=data['protocol'],
        packet_size=data['packet_size'],
        is_anomalous=is_anomalous
    )
    session.add(log)
    session.commit()
    return jsonify({'message': 'Anomaly detection completed', 'is_anomalous': is_anomalous})

if __name__ == '__main__':
    create_default_user()  # Ensure the default user is created
    app.run(debug=True, host='0.0.0.0', port=5000)
