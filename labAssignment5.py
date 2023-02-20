import math  #dont need this...

sentence1 = ""

pigLatinPhrase = ""


sentence1 = input ("Enter a phrase to translate into PigLatin: ").lower()
words = sentence1.split()

#if first letter is a vowel
for i, word in enumerate(words): 
    if word[0:] in 'aeiou':
        words[i] = words[i] + "ay"
    else:
        #if sentence has vowel later in word, put consonants along with "ay" at the end
        
        hasVowel = False

        for j, letter in enumerate(word):
            if letter in "aeiou":
                words[i] = word[j:] + word[:j] + "ay"
                hasVowel = True
                break
        if (hasVowel == False):
            words[i] = words[i] + "ay"   

#combine and print piglatin word
pigLatinPhrase = " ".join(words)
print ("Your phrase in PigLatin is:", pigLatinPhrase)