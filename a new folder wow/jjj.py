#this actually has the uhh same name as the last file but there's no problem because it's in a folder
import random
alpha = ["ok. die.", "i don't care.", "shut up.", "no", "ok"]
while True:
    print("say something, wow:")
    random_irrellevant_variable = input("> ")
    print(alpha[random.randint(0, len(alpha) - 1)])
