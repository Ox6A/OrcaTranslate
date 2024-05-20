import os
import time
import asyncio
import argostranslate.translate

breakLoop = False

version = "1.0.0"

async def timer(reason):
    global breakLoop
    breakLoop = False
    if reason == "online":
        counter = 1
        while breakLoop == False:
            print(f"Checking online connectivity{('.'*counter)}", end="\r")
            counter += 1
            await asyncio.sleep(1)

def checkOnline():
    global breakLoop
    asyncio.run(timer("online"))
    response = os.system("ping -c 1 8.8.8.8")
    if response == 0:
        breakLoop = True
        return True
    else:
        breakLoop = True
        return False

def translate():
    run = True
    while run:
        try:
            x = input("Enter text to translate, then add a / and language code: e.g en: ")
            if x.lower() == "exit":
                run = False
                break
            x = x.split("/")
            text = x[0]
            if x[1].lower() == "en":
                translatedText = argostranslate.translate.translate(text, "fr", "en")
                print(translatedText + "\n")
            else:
                translatedText = argostranslate.translate.translate(text, "en", "fr")
                print(translatedText + "\n")
        except IndexError as e:
            print(e+"\n")

def main():
    print(f"Welcome to Orca Translate {version}\nThis is an offline language translator that is written in Python.\n")
    time.sleep(1)
    x = checkOnline()
    if x:
        print("You are connected to the internet, you can use the online translator.")
    else:
        print("You are not connected to the internet, you can use the offline translator.")

if __name__ == "__main__":
    main()