# Flight Cancellation Analysis - Objective 4
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
data = pd.read_csv("cleaned_flight_data.csv")

# simulate cancellation info (10% cancelled)
np.random.seed(0)
data['cancelled'] = np.random.choice([0, 1], size=len(data), p=[0.9, 0.1])

cancelled = data[data['cancelled'] == 1]

# Bar Chart: Cancellations by Airline
airline_cancel = cancelled['carrier'].value_counts()
plt.bar(airline_cancel.index, airline_cancel.values)
plt.title("Cancelled Flights by Airline")
plt.xlabel("Airline")
plt.ylabel("Cancellations")
plt.show()

# Pie Chart: Cancellations by Airport
airport_cancel = cancelled['origin'].value_counts()
plt.pie(airport_cancel.values, labels=airport_cancel.index, autopct='%1.1f%%')
plt.title("Cancellations by Airport")
plt.show()
