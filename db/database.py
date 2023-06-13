import pymysql
from pymysql import Error
from .constants import GET_DATABASES_QUERY, CREATE_DATABASE_QUERY, DB_USER, DB_HOST

# MySQL Connection Configuration .. I have set it locally to no pw but you could just add the pw here for your mysql deployment
config = {
    'user': DB_USER,
    'host': DB_HOST
}

def connect_to_database():
    try:
        conn = pymysql.connect(**config)
        if conn.open:
            print('Connected to MySQL server')
            # Check if the database exists
            cursor = conn.cursor()
            cursor.execute(GET_DATABASES_QUERY)
            database_exists = cursor.fetchone()
            if not database_exists:
                # Create the database
                cursor.execute(CREATE_DATABASE_QUERY)
                print('Created new database')
            # Connect to the database
            config['database'] = 'flask_task'
            conn = pymysql.connect(**config)
            if conn.open:
                print('Connected to MySQL database')
                # Check if the database is empty
                cursor = conn.cursor()
                cursor.execute("SHOW TABLES")
                if not cursor.fetchall():
                    # Execute the schema SQL statements
                    with open('db/schema.sql', 'r') as f:
                        sql_statements = f.read()
                        cursor = conn.cursor()
                        statements = sql_statements.split(';')
                        for statement in statements:
                            if statement.strip() != '':
                                cursor.execute(statement)
                                while cursor.nextset():
                                    pass
                        print('Schema SQL statements executed successfully')
            return conn
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')
