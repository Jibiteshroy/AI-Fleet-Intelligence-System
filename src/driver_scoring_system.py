data["driver_score"] = 100 \
    - (data["harsh_brake"] * 20) \
    - (data["idle_time"] * 0.5) \
    - (data["speed"] > 100) * 10

data["driver_score"] = data["driver_score"].clip(0,100)