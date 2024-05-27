import pandas as pd
import matplotlib.pyplot as plt

# Ścieżki do plików CSV
gamePath = 'csv/3Stardew Valley.csv'
gamePathgame = 'csv/3Stardew ValleyGAME.csv'
title = 'Stardew Valley: Comparison of the number of players and price'

# Wczytaj plik CSV z poprawnym separatorem
df = pd.read_csv(gamePath, delimiter=';')

# Konwersja kolumny DateTime na typ datetime z odpowiednim formatem
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%d.%m.%Y %H:%M')

# Usunięcie rekordów z ceną równą 0
df = df[df['Final price'] != '0']

# Konwersja cen na float
df['Final price'] = df['Final price'].str.replace(',', '.').astype(float)

# Dodanie kolumny miesiąc-rok
df['MonthYear'] = df['DateTime'].dt.to_period('M')

# Obliczenie średniej ceny dla każdego miesiąca
average_price_per_month = df.groupby('MonthYear')['Final price'].mean().reset_index()

# Mapowanie nazw miesięcy na liczby
month_map = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

# Wczytaj plik CSV z poprawnym separatorem
df_right = pd.read_csv(gamePathgame, delimiter=',')

# Podziel wartości w kolumnie na rzeczywiste kolumny za pomocą separatora ','
df_right = df_right['gamename,"year","month","avg","gain","peak","avg_peak_perc"'].str.split(',', expand=True)

# Zmień nazwy kolumn na odpowiednie
df_right.columns = ["gamename", "year", "month", "avg", "gain", "peak", "avg_peak_perc"]

# Usuń znaki cudzysłowu (") i spacje z wartości w kolumnie "month"
df_right['month'] = df_right['month'].str.strip('"').str.strip()

# Zamień nazwy miesięcy na liczby
df_right['month'] = df_right['month'].apply(lambda x: month_map[x])

# Stwórz kolumnę "MonthYear" w df_right
df_right['MonthYear'] = df_right['year'] + '-' + df_right['month']

# Usuń kolumny "year" i "month" (jeśli nie są już potrzebne)
df_right.drop(columns=['year', 'month'], inplace=True)

# Usuń wszystkie cudzysłowy (") z wartości w kolumnie "MonthYear"
df_right['MonthYear'] = df_right['MonthYear'].str.replace('"', '')

# Konwersja kolumny 'MonthYear' na typ period
df_right['MonthYear'] = pd.to_datetime(df_right['MonthYear'], format='%Y-%m').dt.to_period('M')

# Konwersja kolumny 'avg' na typ float
df_right['avg'] = df_right['avg'].astype(float)

# Połączenie obu DataFrames na podstawie kolumny 'MonthYear'
merged_df = pd.merge(average_price_per_month, df_right, on='MonthYear', how='inner')

# Ustawienie rozmiaru wykresu
plt.figure(figsize=(12, 8))

# Stworzenie pierwszej osi y dla liczby graczy
fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.set_xlabel('Date')
ax1.set_ylabel('Average Players', color='blue')
ax1.plot(merged_df['MonthYear'].dt.to_timestamp(), merged_df['avg'], label='Average Players', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Tworzenie drugiej osi y dla ceny
ax2 = ax1.twinx()
ax2.set_ylabel('Average Price', color='red')
ax2.plot(merged_df['MonthYear'].dt.to_timestamp(), merged_df['Final price'], label='Average Price', color='red', linestyle='--')
ax2.tick_params(axis='y', labelcolor='red')

# Dodanie tytułu
plt.title(title)

# Obrót etykiet osi X dla lepszej czytelności
plt.xticks(rotation=45)

# Dodanie siatki na wykresie
fig.tight_layout()
plt.grid(True)

# Pokazanie wykresu
plt.show()
