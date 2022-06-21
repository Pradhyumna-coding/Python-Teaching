vowels = ["a", "e", "i", "o", "u"]

def getNoVowels(text):
    noVovels = 0
    for letter in text:
        for vowel in vowels:
            if letter == vowel:
                noVovels+=1
    return noVovels

text = input("Enter the word")

noVowels = getNoVowels(text)

print("The number of vowels are " + str(noVowels))
