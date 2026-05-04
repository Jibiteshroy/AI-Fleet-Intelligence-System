import pandas as pd

data = pd.read_csv("fleet_telemetry.csv")

# Convert categorical
data = pd.get_dummies(data, columns=["route_type"], drop_first=True)