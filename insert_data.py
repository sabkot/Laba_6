import psycopg2
from datetime import date

# Підключення до бази даних
conn = psycopg2.connect(
    host="localhost",
    database="Karman",
    user="user",
    password="user"
)
cursor = conn.cursor()

# Вставка даних
insert_data_query = """
-- Вставка даних для 5 орендарів
INSERT INTO Orendari (Nazva_Firmi_Orendarya, Kerivnik, Telefon) VALUES
    ('Firm1', 'Director1', '123-456-7890'),
    ('Firm2', 'Director2', '987-654-3210'),
    ('Firm3', 'Director3', '111-222-3333'),
    ('Firm4', 'Director4', '444-555-6666'),
    ('Firm5', 'Director5', '777-888-9999');

-- Вставка даних для 11 приміщень
INSERT INTO Primischennya (Ploshcha, Vartist_Orendi_za_1m2, Poverkh, Nomer_Poverkhova, Ozdoblennya) VALUES
    (100, 10, 1, TRUE, 'Zvichayne'),
    (150, 15, 2, FALSE, 'Polipshene'),
    (200, 20, 3, TRUE, 'Zvichayne'),
    (120, 12, 2, FALSE, 'Polipshene'),
    (180, 18, 1, TRUE, 'Yevro'),
    (90, 9, 3, FALSE, 'Zvichayne'),
    (130, 13, 2, TRUE, 'Polipshene'),
    (160, 16, 1, FALSE, 'Zvichayne'),
    (110, 11, 3, TRUE, 'Polipshene'),
    (140, 14, 2, FALSE, 'Yevro'),
    (170, 17, 1, TRUE, 'Yevro');

-- Вставка даних для 11 договорів оренди
INSERT INTO Orenda (Data_Pochatku_Diyi_Dogovoru, Termin_Diyi_Dogovoru, Meta_Orendi, Kod_Orendarya, Nomer_Primischennya) VALUES
    ('2023-01-01', 365, 'Office', 1, 1),
    ('2023-02-01', 730, 'Warehouse', 2, 2),
    ('2023-03-01', 365, 'Retail', 3, 3),
    ('2023-04-01', 730, 'Warehouse', 4, 4),
    ('2023-05-01', 365, 'Office', 5, 5),
    ('2023-06-01', 730, 'Retail', 1, 6),
    ('2023-07-01', 365, 'Warehouse', 2, 7),
    ('2023-08-01', 730, 'Office', 3, 8),
    ('2023-09-01', 365, 'Retail', 4, 9),
    ('2023-10-01', 730, 'Warehouse', 5, 10),
    ('2023-11-01', 365, 'Office', 1, 11);
"""

cursor.execute(insert_data_query)

# Збереження змін
conn.commit()

# Закриття підключення
cursor.close()
conn.close()
