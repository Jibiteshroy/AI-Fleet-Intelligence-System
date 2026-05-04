import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression

# -----------------------------------------
# PHASE 1: DATASET GENERATOR
# -----------------------------------------
np.random.seed(42)
n = 5000

print("Initializing telemetry data generation...")
data = pd.DataFrame({
    "vehicle_id": np.random.randint(100, 200, n),
    "timestamp": pd.date_range(start="2025-01-01", periods=n, freq="h"), # Changed 'H' to 'h' for deprecation warning
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

# Physics-based failure logic
data["failure"] = ((data["engine_temp"] > 100) & (data["rpm"] > 3000)).astype(int)

# -----------------------------------------
# PHASE 2: AI INTELLIGENCE LAYER
# -----------------------------------------
print("Processing intelligence models...")

# Prepare categorical data
data_processed = pd.get_dummies(data, columns=["route_type"], drop_first=True)

# A. Predictive Maintenance Model (Random Forest)
X = data_processed.drop(columns=["failure", "timestamp"])
y = data_processed["failure"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)
data["failure_prob"] = rf_model.predict_proba(X)[:, 1]

# B. Fuel Efficiency Model (Linear Regression)
features = ["speed", "rpm", "idle_time"]
target = "fuel_level"
fuel_model = LinearRegression()
fuel_model.fit(data_processed[features], data_processed[target])
data["predicted_fuel"] = fuel_model.predict(data_processed[features])

# C. Driver Scoring System
data["driver_score"] = 100 \
    - (data["harsh_brake"] * 20) \
    - (data["idle_time"] * 0.5) \
    - (data["speed"] > 100) * 10
data["driver_score"] = data["driver_score"].clip(0, 100)

# -----------------------------------------
# EXPORT
# -----------------------------------------
output_file = "fleet_output.csv"
data.to_csv(output_file, index=False)
print(f"Success! {output_file} is ready for Power BI.")