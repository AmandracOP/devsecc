import pandas as pd
import random

def generate_data(num_rows=1000):
    data = {
        'app_name': [random.choice(['AppA', 'AppB', 'AppC']) for _ in range(num_rows)],
        'domain': [random.choice(['example.com', 'test.com', 'sample.org']) for _ in range(num_rows)],
        'protocol': [random.choice(['TCP', 'UDP', 'ICMP']) for _ in range(num_rows)],
        'packet_size': [random.randint(64, 1500) for _ in range(num_rows)],
        'is_anomalous': [random.choice([0, 1]) for _ in range(num_rows)],
    }
    df = pd.DataFrame(data)
    df.to_csv('dataset.csv', index=False)

if __name__ == "__main__":
    generate_data()
