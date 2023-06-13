from flask import Flask
from api.routes import register_routes
from db.database import connect_to_database


app = Flask(__name__)
# Initialize Swagger


# Connect to the database
conn = connect_to_database()

# Register routes
register_routes(app, conn)

if __name__ == '__main__':
    app.run()
