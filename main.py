from dank import Dank
import time
import sqlite3
conn = sqlite3.connect("dankdata.db")
c = conn.cursor()
run = True

#database
c.execute("""CREATE TABLE IF NOT EXISTS dank (
          name text,
          money integer,
          moneyinbank integer
)""")
conn.commit()

print("Welcome to the meme game >:)")
print("Playing for the first time?")
print("1.New Game")
print("2.Continue")
print("3.About the game")
print("4.Exit")
print("")
st =  input("> ")
print("")

if st == "1":
    name = input("enter your name: ")
    c.execute("SELECT name FROM dank")
    names = [row[0] for row in c.fetchall()]
    conn.commit()
    if name in names:
        print("This user already exist!, play continue")
        exit()
    else:
        pass
    starter = [name, 0, 0]
    time.sleep(1)
    c.execute(f"INSERT INTO dank VALUES (?, ?, ?)", starter)
    conn.commit()
    print(f"Hello, {name}\n")
    print("type help for more information\nOr Exit to exit the game\n")
    while run:
        cd = input(f"{name}> ").lower()
        if cd == "help":
                print(f"Current Commands: ", end="")
                print(Dank.Availablecommands(Dank))
        elif cd == "exit":
            exit()
        elif cd == "/bal":
            Dank.bal(self=Dank,name=name)
        elif cd == "/dig":
            Dank.dig(self=Dank,name=name)
        elif cd == "/beg":
            Dank.beg(self=Dank,name=name)
elif st == "2":
    name = input("enter your name: ")
    c.execute("SELECT name FROM dank")
    names = [row[0] for row in c.fetchall()]
    conn.commit()
    if name in names:
        while run:
            cd = input(f"{name}> ").lower()
            if cd == "help":
                print(f"Current Commands: ", end="")
                Dank.Availablecommands(Dank)
            elif cd == "exit":
                exit()
            elif cd == "/bal":
                Dank.bal(self=Dank,name=name)
            elif cd == "/dig":
                Dank.dig(self=Dank,name=name)
            elif cd == "/beg":
                Dank.beg(self=Dank,name=name)
    else:
        print("name not found")
elif st == "3":
    print("This game is still in progress")
    time.sleep(1)
    print("So pls Expect bugs or errors")
    time.sleep(1)
    print("If you ever found errors or bug send me picture of it so i can fix it in the next version")
    time.sleep(1)
    print("Version-0.2")
    time.sleep(4)
elif st == "4":
    exit()
else:
    print("Are you stupid or something?\n")
