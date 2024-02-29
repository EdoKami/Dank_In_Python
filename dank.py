import sqlite3
import time
import random
rd = random

#database
conn = sqlite3.connect("dankdata.db")
c = conn.cursor()

class Dank:
    
    def Availablecommands(self):
        print("< /bal >, < /dig >, more comming soon baby!!!!!!!")
        
    def bal(self, name):
        c.execute("SELECT money FROM dank WHERE name=?", (name,))
        balance = c.fetchone()
        c.execute("SELECT moneyinbank FROM dank WHERE name=?", (name,))
        balanceinbank = c.fetchone()
        if balance:
            print(f"User> {name}")
            print(f"Balance: {balance[0]}Rs")
            print(f"Bank Balance: {balanceinbank[0]}Rs")
        else:
            print(f"User {name} not found.")
    def dig(self, name):
        chanc = rd.randint(1, 4)
        
        if chanc == 1:
            soldgold = rd.randint(1, 100000)
            print(f"You strike gold, {name}! You got some gold and sold it for {soldgold}Rs.")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (soldgold, name))
            conn.commit()
        elif chanc == 2:
            print(f"You dug down and found nothing! lololololol!")
        elif chanc == 3:
            worth = rd.randint(1, 100)
            print(f"You dug down and found some coins worth {worth}Rs")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (worth, name))
            conn.commit()
        elif chanc == 4:
            print(f"You dug down and found buried dog poop XD")
        elif chanc == 5:
            print("Some message here")
        elif chanc == 20:
            print(f"Unfortunate turn of events! {name}, your digging attracts unwanted attention from bandits, who demand a share of your findings. Better luck next time.")
