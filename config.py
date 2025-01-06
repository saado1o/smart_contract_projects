import os

# Configuration for the database
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),  # Hostname or IP address of the database
    'user': os.getenv('DB_USER', 'root'),  # Database username
    'password': os.getenv('DB_PASSWORD', 'your_password'),  # Database password (from environment variables)
    'database': os.getenv('DB_NAME', 'smart_contract_db')  # Database name
}
