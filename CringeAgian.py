import sqlite3

# Conn
conn = sqlite3.connect("TelephoneStorage.db")

# Create the Cursor
c = conn.cursor()

c.execute("""CREATE TABLE CringeShit (
username text,
PhoneNumber text
)""")

# Commit
conn.commit()

# Close the Conn

conn.close()