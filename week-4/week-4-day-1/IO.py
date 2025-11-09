#1
def encrypt(text: str) -> str:
    string = ""
    for ch in text:
        if ch.islower():
            string += chr(122 - ord(ch) + 97)
        elif ch.isupper():
            string += chr(90 - ord(ch) + 65)
        else:
            string += ch
    return string

with open("secret.txt", "w") as file:
    file.write(encrypt("Hi, my name is UD"))

with open("secret.txt", "r") as file:
    print(file.read())

with open("secret.txt", "r") as file:
    print(encrypt(file.read()))

#2
mixed_stories = open("mixed_stories.txt", "r").readlines()

def sort_lines_1(text):
    string = ""
    for index, line in enumerate(text):
        if index % 2 == 0:
            string += line
    return string

def sort_lines_2(text):
    string = ""
    for index, line in enumerate(text):
        if index % 2 == 1:
            string += line
    return string

    

with open("story_1.txt", "w") as file:
    file.write(sort_lines_1(mixed_stories))

with open("story_2.txt", "w") as file:
    file.write(sort_lines_2(mixed_stories))