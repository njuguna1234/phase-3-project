import psycopg2

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "school_manage_system"
DB_USER = "postgres"
DB_PASSWORD = "12345"  # Replace with your actual password

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
