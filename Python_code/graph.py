import pandas as pd
import matplotlib.pyplot as plt

# Data for freight modes
data = {
    "Iteration": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "freight_i": [1800, 0, 1710, 1620, 1710, 1800, 1440, 1620, 1530, 1800, 1620],
    "freight_n": [0, 1800, 90, 180, 90, 0, 360, 180, 270, 0, 180],
}

df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df["Iteration"], df["freight_i"], label="Integrated ", alpha=0.7, color="blue")
plt.bar(df["Iteration"], df["freight_n"], label="Non-integrated", alpha=0.7, bottom=df["freight_i"], color="green")

plt.xlabel("Iteration")
plt.ylabel("Passenger Kilometers Traveled (pkm)")
plt.title("Freight Modes Comparison (Integrated vs Non-integrated)")
plt.legend()
plt.xticks(df["Iteration"])
plt.tight_layout()

# Show the graph
plt.show()
