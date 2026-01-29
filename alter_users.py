import sqlite3

def alter_users_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # Check if 'email' column already exists
    c.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in c.fetchall()]

    if 'email' not in columns:
        print("Adding 'email' column...")
        c.execute("ALTER TABLE users ADD COLUMN email TEXT")
        print("'email' column added successfully.")
    else:
        print("'email' column already exists. No action taken.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    alter_users_table()
