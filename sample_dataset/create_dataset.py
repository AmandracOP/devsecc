import pandas as pd
import random

# Parameters
num_samples = 10000
applications = ['AppA', 'AppB', 'AppC', 'AppD']
domains = ['domain1.com', 'domain2.net', 'domain3.org', 'domain4.io']
protocols = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'FTP']

data = {
    'application': [random.choice(applications) for _ in range(num_samples)],
    'domain': [random.choice(domains) for _ in range(num_samples)],
    'protocol': [random.choice(protocols) for _ in range(num_samples)],
    'packet_size': [random.randint(40, 1500) for _ in range(num_samples)],
    'is_anomalous': [random.choices([0, 1], weights=[95, 5])[0] for _ in range(num_samples)],
}

df = pd.DataFrame(data)
df.to_csv('dataset.csv', index=False)
