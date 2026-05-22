import sqlite3

def init_db():
    # Establishes connection to the local database file specified by the manual
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    
    # Lab 1, 3, 4, 5, 6, 7, 8: Products table layout with different data types
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        category TEXT,
        price INTEGER,
        released INTEGER
    )''')
    
    # Lab 2: Standard users authentication table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )''')
    
    # Lab 5, 6, 8: Target backend credential harvesting table
    cursor.execute('''CREATE TABLE IF NOT EXISTS secret_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )''')
    
    # Seed sample parameters if tables are currently unpopulated
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        # Inserting items into products matrix
        cursor.execute("INSERT INTO products (name, description, category, price, released) VALUES ('Laptop', 'High performance engineering workstation', 'Tech', 1200, 1)")
        cursor.execute("INSERT INTO products (name, description, category, price, released) VALUES ('Hidden Spy Camera', 'Unreleased surveillance node prototype', 'Tech', 150, 0)")
        cursor.execute("INSERT INTO products (name, description, category, price, released) VALUES ('Running Shoes', 'Premium lightweight athletic footwear', 'Sports', 85, 1)")
        
        # Creating default administrator user account
        cursor.execute("INSERT INTO users (username, password) VALUES ('administrator', 'SuperSecureAdminPassword2026')")
        
        # Planting flags inside target extraction schema
        cursor.execute("INSERT INTO secret_users (username, password) VALUES ('admin', 'flag{sql_injection_master_level_8}')")
        cursor.execute("INSERT INTO secret_users (username, password) VALUES ('ceo', 'ultimate_corporate_vault_access')")
        
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()