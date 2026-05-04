import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

data = pd.DataFrame({
    "vehicle_id": np.random.randint(100, 200, n),
    "timestamp": pd.date_range(start="2025-01-01", periods=n, freq="H"),
    "speed": np.random.randint(0, 120, n),
    "rpm": np.random.randint(700, 4000, n),
    "engine_temp": np.random.randint(70, 120, n),
    "fuel_level": np.random.randint(10, 100, n),
    "idle_time": np.random.randint(0, 60, n),
    "harsh_brake": np.random.choice([0, 1], n, p=[0.8, 0.2]),
    "distance": np.random.randint(1, 300, n),
    "driver_id": np.random.randint(1, 20, n),
    "route_type": np.random.choice(["city", "highway"], n)
})

# Failure logic
data["failure"] = (
    (data["engine_temp"] > 100) &
    (data["rpm"] > 3000)
).astype(int)

data.to_csv("fleet_telemetry.csv", index=False)

print("Dataset created successfully!")