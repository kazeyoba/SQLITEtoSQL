# Script pour convertir .sqlite vers .sql 
# Author: Timaï SELMI
import sqlite3
import sys

def convert_sqlite_to_sql(sqlite_file, sql_file):
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()

    # Obtenir toutes les informations de la table
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    with open(sql_file, 'w') as f:
        for table_name in tables:
            table_name = table_name[0]

            # Obtenir les colonnes de la table
            cursor.execute(f"PRAGMA table_info('{table_name}');")
            columns = cursor.fetchall()

            column_str = ", ".join([f"{column[1]} {column[2]}" for column in columns])
            f.write(f"CREATE TABLE {table_name} ({column_str});\n")

            # Obtenir les données de la table
            cursor.execute(f"SELECT * FROM {table_name};")
            table_data = cursor.fetchall()

            for data in table_data:
                data_str = ", ".join([f"'{data[i]}'" if isinstance(data[i], str) else str(data[i]) for i in range(len(data))])
                f.write(f"INSERT INTO {table_name} VALUES ({data_str});\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Utilisation : python sqliteTosql.py <fichier SQLite> <fichier SQL>")
        sys.exit(1)

    sqlite_file = sys.argv[1]
    sql_file = sys.argv[2]
    convert_sqlite_to_sql(sqlite_file, sql_file)
