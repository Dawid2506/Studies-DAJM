import pandas as pd

# Wczytaj plik CSV z poprawnym separatorem i usuń cudzysłowy z nazw kolumn
df = pd.read_csv('csv/1gtav.csv', delimiter=';')

# Usuń cudzysłowy z nazw kolumn
df.columns = df.columns.str.replace('"', '')

# Wyświetl pierwszy wiersz danych, aby upewnić się, że dane są poprawnie wczytane
print(df.head())

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

# Wybierz kolumny zawierające dane dotyczące gry
game_data_columns = ['gamename', 'year', 'month', 'avg', 'gain', 'peak', 'avg_peak_perc']

# Usuń puste kolumny (mogą pojawić się, jeśli dane nie są idealnie wyrównane)
df = df.dropna(axis=1, how='all')

# Podziel DataFrame na dwie części: lewą (oryginalne dane) i prawą (dane gry)
df_left = df.iloc[:, :3]  # lewa część (3 kolumny: DateTime, Final price, Historical low)
df_right = df.iloc[:, 3:]  # prawa część (dane gry)

# Usuń cudzysłowy z nazw kolumn w prawej części
df_right.columns = df_right.columns.str.replace('"', '')

# Zamień nazwy miesięcy na liczby w kolumnie 'month'
df_right['month'] = df_right['month'].map(month_map)

# Scal obie części DataFrame
df_combined = pd.concat([df_left, df_right], axis=1)

# Wyświetl zmodyfikowany DataFrame
print(df_combined.head())