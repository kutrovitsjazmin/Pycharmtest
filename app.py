import pandas as pd

# Az "astronauts.csv.csv" fájl beolvasása
file_path = "astronauts.csv.csv"
df = pd.read_csv(file_path)

# Születési hónapok kinyerése a "Birth Date" oszlopból
df['Birth Month'] = pd.to_datetime(df['Birth Date']).dt.month

# Hónapok számosságának számolása
month_counts = df['Birth Month'].value_counts()
top_three_months = month_counts.head(3)
total_astronauts = len(df)
percentage_top_three = (top_three_months / total_astronauts) * 100
for month, percentage in percentage_top_three.iteritems():
    print(f"{month}: {percentage:.1f}%")