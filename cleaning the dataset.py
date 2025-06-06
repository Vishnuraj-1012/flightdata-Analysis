import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("flightdata.csv")

for col in ['dep_time', 'dep_delay', 'arr_time', 'arr_delay', 'air_time', 'avgdelay']:
    if col in df.columns:
        df[col] = df[col].fillna(0)

if 'tailnum' in df.columns:
    df['tailnum'] = df['tailnum'].fillna('UNKNOWN')

# Showing how many missing values remain
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save the fully cleaned file
df.to_csv("cleaned_flight_data.csv", index=False)
print("\ncleaned_flight_data.csv saved.")
