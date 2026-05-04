from sklearn.linear_model import LinearRegression

features = ["speed", "rpm", "idle_time"]
target = "fuel_level"

fuel_model = LinearRegression()
fuel_model.fit(data[features], data[target])

data["predicted_fuel"] = fuel_model.predict(data[features])