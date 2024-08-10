dict = {"namaste" : "Hello", "Gadhe": "Donkey", "Phool": "Flower", "Sundar" : "Beautiful","gora" : "white"}
word = input("Enter the word you want to search its meaning in english: ")
print(f"Meaning of {word} is {dict.get(word)}")