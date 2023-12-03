import psycopg2

class QueryExecution:
    query_number = 1

def execute_query_and_print(query, cursor):
    cursor.execute(query)
    column_names = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()

    print("\nЗапит #{}:\n".format(QueryExecution.query_number))
    print("\n" + "-" * 50)
    print(" | ".join(map(str, column_names)))
    print("-" * 50)
    for row in results:
        print(" | ".join(map(str, row)))

def main():
    # Підключення до бази даних
    conn = psycopg2.connect(
        host="localhost",
        database="Karman",
        user="user",
        password="user"
    )
    cursor = conn.cursor()

    # Запит для виведення структури та даних з усіх таблиць
    tables_query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    """
    cursor.execute(tables_query)
    tables = cursor.fetchall()

    # Виведення структури та даних з усіх таблиць
    print("\nСТРУКТУРА ТА ДАНІ З ТАБЛИЦЬ:\n")
    for table in tables:
        table_name = table[0]
        print(f"\nТаблиця: {table_name}\n")

        # Запит для виведення структури таблиці
        describe_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';"
        cursor.execute(describe_query)
        table_structure = cursor.fetchall()

        print("-" * 50)
        print(" | ".join(map(lambda x: x[0], table_structure)))
        print("-" * 50)

        # Запит для виведення даних з таблиці
        data_query = f"SELECT * FROM {table_name};"
        cursor.execute(data_query)
        table_data = cursor.fetchall()

        for row in table_data:
            print(" | ".join(map(str, row)))

    # Виконання запитів
    QueryExecution.query_number = 1
    queries = [
        "SELECT * FROM Orendari WHERE Kod_Orendarya IN (SELECT Kod_Orendarya FROM Orenda WHERE Meta_Orendi = 'Warehouse') ORDER BY Nazva_Firmi_Orendarya;",
        "SELECT Nomer_Primischennya, Ploshcha * Vartist_Orendi_za_1m2 AS Zahalna_Orendna_Plata FROM Primischennya;",
        "SELECT Ozdoblennya, SUM(Ploshcha) AS Zahalna_Ploshcha FROM Primischennya GROUP BY Ozdoblennya;",
        "SELECT Nomer_Dogovoru_Orendi, Data_Pochatku_Diyi_Dogovoru + INTERVAL '1 day' * Termin_Diyi_Dogovoru AS Kinceva_Data_Diyi FROM Orenda;",
        "SELECT Meta_Orendi, Ozdoblennya, COUNT(*) AS Kil_kist FROM Orenda INNER JOIN Primischennya ON Orenda.Nomer_Primischennya = Primischennya.Nomer_Primischennya GROUP BY Meta_Orendi, Ozdoblennya;",
        "SELECT * FROM Primischennya WHERE Ozdoblennya = 'Zvichayne';"
    ]

    for query in queries:
        execute_query_and_print(query, cursor)
        QueryExecution.query_number += 1

    # Закриття підключення
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
