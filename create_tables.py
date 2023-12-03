import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    host="localhost",
    database="Karman",
    user="user",
    password="user"
)
cursor = conn.cursor()

# Створення таблиць
create_tables_query = """
CREATE TABLE IF NOT EXISTS Orendari (
    Kod_Orendarya SERIAL PRIMARY KEY,
    Nazva_Firmi_Orendarya VARCHAR(255),
    Kerivnik VARCHAR(255),
    Telefon VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Primischennya (
    Nomer_Primischennya SERIAL PRIMARY KEY,
    Ploshcha NUMERIC,
    Vartist_Orendi_za_1m2 NUMERIC,
    Poverkh INT,
    Nomer_Poverkhova BOOLEAN,
    Ozdoblennya VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS Orenda (
    Nomer_Dogovoru_Orendi SERIAL PRIMARY KEY,
    Data_Pochatku_Diyi_Dogovoru DATE,
    Termin_Diyi_Dogovoru INT,
    Meta_Orendi VARCHAR(20),
    Kod_Orendarya INT,
    Nomer_Primischennya INT,
    FOREIGN KEY (Kod_Orendarya) REFERENCES Orendari (Kod_Orendarya),
    FOREIGN KEY (Nomer_Primischennya) REFERENCES Primischennya (Nomer_Primischennya)
);
"""
cursor.execute(create_tables_query)

# Збереження змін
conn.commit()

# Закриття підключення
cursor.close()
conn.close()
