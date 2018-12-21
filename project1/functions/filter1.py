
vowels = "aeiouAEIOU"
finalVowel = []
def vowelfilter(sentence):
        for letter in sentence:
                if letter in vowels:
                        finalVowel.append(letter)
        return finalVowel
k=vowelfilter('prasad is good boy')
print(k)