#Me Learniing File Handling

f = open("Directory.txt", "a")

def Save():
    global f
    f = open("Directory.txt", "a")
    f.write(f"Name : {UserName}, Number : {Number}. \n")
    f.close()

def PrintLines(x):
    f=open('Directory.txt')
    lines=f.readlines()
    print(lines[x])

def FindUserName(Username):
    f = open('Directory.txt','r')
    line_num = 0
    search_phrase = str(Username)
    for line in f.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
            # print(line_num)
            PrintLines(int(line_num - 1))
            
if __name__ == "__main__":
    # Save()
    # FindUser = input("Enter The Username : ")
    # FindUserName(FindUser)
    x  = int(input("\033[0;34;1mDo You Want to Add an Entry (1) /\033[0;36;1m Look For an Existing One (2) : "))
    if x == 1:
        UserName = input("\033[0;33;2mName: ")
        Number = input("\033[0;32;1mPhone Number: ")
        if len(Number) == 10:
            Save()
        elif len(Number) < 10:
            print("\033[0;31;1mINVALID NUMBER")
            exit()
    elif x == 2:
        FindUser = input("Enter The Username : ")
        FindUserName(FindUser)

    f = open("Directory.txt", "r")
    # print(f.read())

