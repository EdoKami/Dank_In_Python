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
print("3.Exit")
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
        if cd.lower == "help":
            print(f"Current Commands: {Dank.Availablecommands}\n")
        elif cd == "exit":
            exit()
        elif cd == "/bal":
            Dank.bal(name=name)
elif st == "2":
    name = input("enter your name: ")
    c.execute("SELECT name FROM dank")
    names = [row[0] for row in c.fetchall()]
    conn.commit()
    if name in names:
        while run:
            cd = input(f"{name}> ").lower()
            if cd == "help":
                print(f"Current Commands: {Dank.Availablecommands}\n")
            elif cd == "exit":
                exit()
            elif cd == "/bal":
                Dank.bal(self=Dank,name=name)
            elif cd == "/dig":
                Dank.dig(self=Dank,name=name)
    else:
        print("name not found")
elif st == "3":
    pass
else:
    print("Are you stupid or something?\n")
