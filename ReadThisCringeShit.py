import sqlite3

# Conn
conn = sqlite3.connect("TelephoneStorage.db")

# Create the Cursor
c = conn.cursor()

c.execute("SELECT rowid, * FROM CringeShit")

items = c.fetchall()

for item in items:
    print("\033[1;36;1m")
    print(item)

# Commit
conn.commit()

# Close the Conn
conn.close()