from random import randint

dungeons = "Dungeons"
an = "and"
dragons = "Dragons"
vowels = ['a', 'e', 'i', 'o', 'u']

def replaceVowels(word):
    for index, char in enumerate(word):
        if isVowel(char):
            print char
        #pick random vowel
        #replace random vowel
        #return word
        # print s + '\n'
        # print i

def isVowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    return False

replaceVowels(dungeons)
