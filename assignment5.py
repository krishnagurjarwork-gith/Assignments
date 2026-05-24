import requests
import random

print("Assignment 5")
print("1. Weather API")
print("2. Joke API")
print("3. Cat Fact API")
print("4. Rock Paper Scissors Game")

choice = input("Enter choice: ")

if choice == "1":

    city = input("Enter city name: ")

    api_key = "6796f5cda9eb26f67401e0da6d681f5a"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6796f5cda9eb26f67401e0da6d681f5a"

    response = requests.get(url)

    data = response.json()

    print(data)

elif choice == "2":

    url = "https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    data = response.json()

    print(data["setup"])
    print(data["punchline"])

elif choice == "3":

    url = "https://catfact.ninja/fact"

    response = requests.get(url)

    data = response.json()

    print(data["fact"])


elif choice == "4":

    options = ["rock", "paper", "scissors"]

    computer = random.choice(options)

    user = input("Enter rock, paper or scissors: ").lower()

    print("Computer chose:", computer)

    if user == computer:
        print("Match Draw!")

    elif ((user == "rock" and computer == "scissors") or
          (user == "paper" and computer == "rock") or
          (user == "scissors" and computer == "paper")):

        print("You Win!")

    else:
        print("Computer Wins!")


else:
    print("Invalid Choice")