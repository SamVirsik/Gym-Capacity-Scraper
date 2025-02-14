import pandas as pd
import matplotlib.pyplot as plt

filename = "RSF_Data.csv" 
data = pd.read_csv(filename, header=None, names=["datetime", "value"])

data["datetime"] = pd.to_datetime(data["datetime"])

day_to_filter = "2025-01-31"  
filtered_data = data[data["datetime"].dt.date == pd.to_datetime(day_to_filter).date()]

filtered_data["hour"] = filtered_data["datetime"].dt.hour

hourly_avg = filtered_data.groupby("hour")["value"].mean().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))

plt.scatter(
    filtered_data["datetime"].dt.hour + filtered_data["datetime"].dt.minute / 60,  
    filtered_data["value"],
    label="Original Values",
    color="blue",
)

plt.plot(
    hourly_avg["hour"],
    hourly_avg["value"],
    marker="o",
    #linestyle="--",
    label="Hourly Averages",
    color="orange",
)

plt.title(f"Data for {day_to_filter}", fontsize=16)
plt.xlabel("Time of Day (Hours)", fontsize=14)
plt.ylabel("Value", fontsize=14)
plt.xticks(range(0, 24))  # Ensure x-axis ticks are at each hour
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()