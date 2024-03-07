import sqlite3
import time
import random
from FunctionsByRS import Func
rd = random

#database
conn = sqlite3.connect("dankdata.db")
c = conn.cursor()

class Dank:
    
    @staticmethod
    def question():
        dankquestions = {
            "question1": {
                "question": "Who is prime minister of India currently in 2024?",
                "answer": "narendra modi"
            },
            "question2": {
                "question": "What is 2 + 2 - 3 * 4 + 232 + 24 * 3 - 2432 - 32 + 4 - 32 = ?",
                "answer": "-2196"
            },
            "question3": {
                "question": "What is the value of π (pi) to two decimal places?",
                "answer": "3.14"
            },
            "question4": {
                "question": "Who is often credited with the discovery of the Pythagorean theorem?",
                "answer": "pythagoras"
            },
            "question5": {
                "question": "What is the capital of Australia?",
                "answer": "canberra"
            },
            "question6": {
                "question": "In which year did the Apollo 11 mission successfully land humans on the moon?",
                "answer": "1969"
            },
            "question7": {
                "question": "How many sides does a heptagon have?",
                "answer": "7"
            },
            "question8": {
                "question": "Who wrote Dank.Availablecommandsfamous play 'Romeo and Juliet'?",
                "answer": "william shakespeare"
            },
            "question9": {
                "question": "What is the chemical symbol for gold?",
                "answer": "Au"
            },
            "question10": {
                "question": "What is the largest planet in our solar system?",
                "answer": "jupiter"
            },
            "question11": {
                "question": "What is the square root of 144?",
                "answer": "12"
            },
            "question12": {
                "question": "Who painted the famous artwork 'Starry Night'?",
                "answer": "vincent van gogh"
            }
        }
        return dankquestions
    
    @staticmethod
    def askQuestionandgiveanswer():
        q = Dank.question()
        r = random.choice(list(q.values()))
        return r

    def Availablecommands(self):
        return "< /bal >, < /dig >, < /beg > more comming soon baby!!!!!!!"
        
    def bal(self, name):
        c.execute("SELECT money FROM dank WHERE name=?", (name,))
        balance = c.fetchone()
        c.execute("SELECT moneyinbank FROM dank WHERE name=?", (name,))
        balanceinbank = c.fetchone()
        if balance:
            print(f"User: {name}")
            print(f"Balance: {balance[0]}Rs")
            print(f"Bank Balance: {balanceinbank[0]}Rs")
        else:
            print(f"User {name} not found.")
    def dig(self, name):
        chanc = rd.randint(1, 10)
        
        if chanc == 1:
            soldgold = rd.randint(1, 10000)
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
            piggybankmoney = rd.randint(1,150)
            print(f"You Digged down and found kid's piggybank, you found {piggybankmoney}Rs ")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (piggybankmoney, name))
            conn.commit()
        elif chanc == 6:
            print(f"You Digged down and Fell into lava pool")
            time.sleep(2)
            deathmessage = f"{name} tries to swim in lava."
            for i in deathmessage:
                print(i, end="")
                time.sleep(0.2)
            print(":|\n")
        elif chanc == 7:
            notez = rd.randint(0,50)
            if notez >= 3:
                l = rd.randint(6083, 56951)
                print(f"You found a single gold coin worth {l}Rs ")
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (l, name))
                conn.commit()
            else:
                oo = rd.randint(80000,10000000)
                print(f"You Digged down and found a diamond worth {oo}")
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (oo, name))
                conn.commit()
        elif chanc == 8:
            print("You Digged down and found a diamond but then creeper came and blowed you up!\n")
        elif chanc == 9:
            print(f"you digged and found cockroaches!!!!!!!\n")
        elif chanc == 10:
            print(f"Unfortunate turn of events! {name}, your digging attracts unwanted attention from bandits, who demand a share of your findings. Better luck next time.\n")
    def beg(self, name):
        chance = rd.randint(1, 5)
        if chance == 1:
            lm = rd.randint(1, 150)
            print(f"Dank> Ohh you poor~~ soul! here take some {lm}Rs")
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (lm, name))
            conn.commit()
        elif chance == 2:
            lesgo = rd.randint(1, 50)
            print("Dank> ", end="")
            Func.animate_text(text="Bruh! i don't have cash", delay=0.1)
            time.sleep(1)
            print(f"{name}> ", end="")
            Func.animate_text(text="Here's my PayPal qr code scan and give online :D",delay=0.1)
            print(f"Dank> ", end="")
            Func.animate_text(text=f"Are You Serious Right now Bruh?, nvm here's {lesgo}Rs", delay=0.1)
            c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (lesgo, name))
            conn.commit()
        elif chance == 3:
            print("Dank> ", end="")
            Func.animate_text(text="Why?", delay=0.1)
            time.sleep(1)
            print(f"{name}> ", end="")
            Func.animate_text(text="Because i am poor?", delay=0.1)
            time.sleep(2.5)
            print("Dank> ", end="")
            Func.animate_text(text="Then give me money i am poor", delay=0.1)
            time.sleep(2.5)
            print(f"{name}> ", end="")
            Func.animate_text(text=":|, Nvm..", delay=0.1)
        elif chance == 4:
            ht = "Head", "Tails"
            dk = rd.choices(ht)
            print("Dank> ", end="")
            Func.animate_text(text="Imma flip coin if it's a head you will give me money\n if it's a tail then i will take money", delay=0.1)
            time.sleep(3.5)
            Func.animate_text("Coin Flips!!!!", 0.1)
            time.sleep(0.5)
            if dk == "Head":
                Func.animate_text("Head", 0.1)
                print("Dank> ", end="")
                Func.animate_text("It's a head i won money!!", 0.1)
                time.sleep(2.5)
                print(f"{name}> ", end="")
                Func.animate_text("Wait wai wait!!!!!!!!!, again pls :-c", 0.1)
                time.sleep(2.5)
                print("Dank> ", end="")
                Func.animate_text("Fine", 0.1)
                dk = rd.choices(ht)
                time.sleep(2.5)
                if dk == "Head":
                    d = "150"
                    Func.animate_text("Head", 0.1)
                    print("Dank> ", end="")
                    Func.animate_text("I won again hahaha gimme my money", 0.1)
                    time.sleep(2.5)
                    print(f"{name}> ", end="")
                    Func.animate_text("Aw Man!!!!!!", 0.1)
                    c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                    conn.commit()
                else:
                    Func.animate_text("Tails", 0.1)
                    print("Dank> ", end="")
                    Func.animate_text("I won again hahaha gimme my money", 0.1)
                    time.sleep(2.5)
                    print(f"{name}> ", end="")
                    Func.animate_text("wait.... what!!!!!! you fooled me!!!!!!!!", 0.1)
                    c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                    conn.commit()
            else:
                d = "150"
                Func.animate_text("Tails", 0.1)
                print("Dank> ", end="")
                Func.animate_text("I am Still getting the money", 0.1)
                print(f"{name}> ", end="")
                Func.animate_text("How?, wait.... wth!!!!!!!!", 0.1)
                c.execute("UPDATE dank SET money = money - ? WHERE name = ?", (d, name))
                conn.commit()
                print(f"{d}Rs Deducted from the pocket")
        else:
            print("Dank> Ok only if you answer my question correctly")
            time.sleep(2.5)
            print(f"{name}> Ok!")
            time.sleep(1)
            question_data = Dank.askQuestionandgiveanswer()
            question = question_data['question']
            correct_answer = question_data['answer']
            print(f"Dank> {question}")
            user_answer = input(f"{name}> ")
            if user_answer.lower() == correct_answer.lower():
                prize = rd.randint(0, 500)
                print("Dank> Correct answer")
                print(f"Dank> Here is your {prize}")
                c.execute("UPDATE dank SET money = money + ? WHERE name = ?", (prize, name))
                conn.commit()
            else:
                print("Dank> Wrong Answer!!!!")
