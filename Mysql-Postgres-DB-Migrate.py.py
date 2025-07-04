import psycopg2
import pymysql

def migrate_database(mysql_config, postgresql_config):
    """
    Migrates all tables from a MySQL database to a PostgreSQL database.

    Args:
        mysql_config (dict): Dictionary containing MySQL connection details.
        postgresql_config (dict): Dictionary containing PostgreSQL connection details.
    """

    try:
        # Connect to MySQL database
        mysql_conn = pymysql.connect(**mysql_config)
        mysql_cursor = mysql_conn.cursor()
        
        # Connect to PostgreSQL database
        postgresql_conn = psycopg2.connect(**postgresql_config)
        postgresql_cursor = postgresql_conn.cursor()

        # Get a list of all tables in the MySQL database
        mysql_cursor.execute("SHOW TABLES")
        tables = [table[0] for table in mysql_cursor.fetchall()]
     
        # Iterate through each table
        for table_name in tables:
            print(f"Migrating table: {table_name}")

            try:
                #Get column definitions from MySQL
                mysql_cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = mysql_cursor.fetchall()
        
                if not columns:
                    print(f"Warning: NO columns found for table{table_name}")
                    continue

                # for row in rows:
                #     processed_row = [None if value == '000' else value for value in row]

            except Exception as e:
                print(f"Error getting columns for table {table_name}: {e}")
                continue
            
            # columns = [bytes(column) for column in column]
            # column_name = columns[0]
            # sql_query = f"SELECT {column_name} FROM {table_name}"

            # Create column definitions for PostgreSQL
            column_definitions = []
            for column in columns:
                column_name = column[0]
                column_type = column[1] 
                
                # if len (column) > 0:
                #     print(f"Null columns accepted {table_name}") 
                # else: 
                #     None # Handle empty columns.
                
                # Map MySQL data types to PostgreSQL data types
                if column_type == 'date':
                    pg_type = 'DATE'
                elif column_type == 'datetime':
                    pg_type = 'TIMESTAMP'
                elif column_type == 'decimal':
                    pg_type = 'NUMERIC'
                elif column_type == 'json':
                    pg_type = 'JSONB'
                elif column_type == 'blob':
                    pg_type = 'BYTEA'
                elif column_type in ('varchar', 'char'):
                    pg_type = 'VARCHAR(255)'
                elif column_type == 'int':
                    pg_type = 'INTEGER'
                elif column_type == 'float':
                    pg_type = 'FLOAT'
                elif column_type == 'enum':
                    pg_type = 'VARCHAR'
                elif column_type == 'bit':
                    pg_type = 'BOOLEAN'
                elif column_type == 'tinyint':
                    pg_type = 'BOOLEAN'
                elif column_type == 'year':
                    pg_type = 'SMALLINT'
                elif column_type == 'set':
                    pg_type = 'TEXT[]'
                elif column_type == 'decimal':
                    pg_type = 'NUMERIC'
                elif column_type == 'tinyint':
                    pg_type = 'BOOLEAN'
                else:
                    pg_type = 'TEXT'  # Default to text for other types

             


                column_definitions.append(f"{column_name} {pg_type}")

            # Create table in PostgreSQL
            create_table_sql = f"CREATE TABLE {table_name} (" + ",".join(column_definitions) + ")"
            postgresql_cursor.execute(create_table_sql)

            # Insert data into PostgreSQL
            select_sql = f"SELECT * FROM {table_name}"
            mysql_cursor.execute(select_sql)
            rows = mysql_cursor.fetchall()

            for row in rows:
                placeholders = ','.join(['%s'] * len(row))
                insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
                postgresql_cursor.execute(insert_sql, row)

                processed_row = [None if value == '000' else value for value in row]
            postgresql_conn.commit()
            print(f"Data transferred successfully for table: {table_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        mysql_conn.close()
        postgresql_conn.close()

# Example usage:
mysql_config = {
    'host': 'ip_address',
    'user': 'username',
    'password': 'password',
    'database': 'users'
}

postgresql_config = {
    'host': 'ip_address',
    'user': 'username',
    'password': 'password',
    'database': 'users'
}

migrate_database(mysql_config, postgresql_config)
