from random import randint

#define some global variables
dungeons = "Dungeons"
an = "and"
dragons = "Dragons"
vowels = ['a', 'e', 'i', 'o', 'u']

#Let's start by randoising the vowels in the strings.
def replaceVowels(word):
    w = list(word)
    for index, char in enumerate(w):
        if isVowel(char):
            w[index] = randomiseVowel()
    return ''.join(w)

#Helper method
def isVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    return False

def randomiseVowel():
    return vowels[randint(0, len(vowels)-1)]


def startItUp():
    for x in range(0, 100):
        print (replaceVowels(dungeons))
        print (replaceVowels(an))
        print (replaceVowels(dragons))

startItUp()
