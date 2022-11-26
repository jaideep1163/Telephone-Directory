import sqlite3

# Conn
conn = sqlite3.connect("TelephoneStorage.db")

# Create the Cursor
c = conn.cursor()

def InsertValues():
    Name = str(input("\033[1;36;1mEnter The Name: "))
    Number = input("\033[1;34;1mEnter The Number: ")

    Stored = [(Name), (Number)]
    c.executemany("INSERT INTO CringeShit VALUES (?,?)", (Stored,))

def Search():
    Name = str(input("\033[1;36;1mEnter The Name: "))
    cursor = c.execute(f"SELECT * FROM CringeShit Where username=?", (Name,))
    results = cursor.fetchall()
    print(results)

if __name__ == "__main__":
    UserInp = int(input("Enter if U Want to Add An Entry Or Search For An Entry (1/2): "))
    if UserInp == 1:
        InsertValues()
    elif UserInp ==2:
        Search()
# Commit
conn.commit()

# Close the Conn
conn.close()