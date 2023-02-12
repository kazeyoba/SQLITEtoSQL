# SQLITEtoSQL
Convert sqlite file to sql file for MariaDB or MySQL

## How to use ?
To use this script, you must provide it with the names of the SQLite and SQL files as command line arguments, like this:

`python sqliteTosql.py -i database.sqlite -o database.sql -u USER -p USER_PASSWORD`

**-u** and **-p** : Optional parameters, if used then creates a user who will be allowed to access the database.

I will create an `.sql` file for you.

## Import in MariaDB

**Before to start**: Please check the sql file is syntactically correct. 

Here is a resource for error codes:
https://mariadb.com/kb/en/mariadb-error-codes/

```text
/docker-entrypoint-initdb.d # mysql -u root -p test < app.sql
ERROR 1064 (42000) at line 49: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 's Souls', 79.99, 'img/demons-souls.jpg', 'Jeux-vidéos');
INSERT INTO Produit...' at line 1
/docker-entrypoint-initdb.d #
```

**Import file.sql**

`mysql -u root -p DATABASE_NAME < file.sql`

> **I repeat, in case of error, read the sql file again.**
