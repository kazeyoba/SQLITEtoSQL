# Script pour convertir .sqlite vers .sql 
# Author: Timaï SELMI
import sqlite3
import sys
import os
import argparse


def convert_sqlite_to_sql(sqlite_file, sql_file, user:str = None, password: str = None):
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()

    # Obtenir toutes les informations de la table
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Récupérer le nom du fichier .sql sans son extension
    sql_file_name = os.path.splitext(sql_file)[0]


    # Définir le nom de la base de données
    database_name = sql_file_name
    

    with open(sql_file, 'w') as f:
        
        # Indication pour créer une table
        f.write(f"CREATE DATABASE {database_name};\n")
        
        # Indication pour créer un utilisateur
        if user != None and password != None:
            f.write(f"CREATE USER {user}@'localhost' IDENTIFIED BY '{password}'")
            f.write(f"GRANT SELECT, INSERT, UPDATE, DELETE, ON {database_name}.* TO '{user}'@'localhost'")
        
        # Utilise la table et commence à inscrire des données
        f.write(f"USE {database_name};\n")
        
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
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required = True, help = 'Le nom d'utilisateur à créer')
    parser.add_argument('-p', '--password', required = True, help = 'Le mot de passe à utiliser')

    args = parser.parse_args()
    
    username = args.username
    password = args.password
    
    if len(sys.argv) != 3:
        print("Utilisation : python sqliteTosql.py <fichier SQLite> <fichier SQL>")
        sys.exit(1)
    
    
    sqlite_file = sys.argv[1]
    sql_file = sys.argv[2]
    convert_sqlite_to_sql(sqlite_file, sql_file)
