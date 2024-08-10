with open("poems.txt") as f:
    data = f.read()
    if("twinkle" in data.lower()):
        print("Twinkle found")
    else:
        print("Not Found")