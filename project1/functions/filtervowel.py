vowels=['a','e','i','o','u','A','E','I','O','U']
finalVowel = []
i=input('enter a string')
def vowelfilter():
        for letter in i:
                if letter in vowels:
                        finalVowel.append(letter)
        return finalVowel
k=vowelfilter()
print(k)
