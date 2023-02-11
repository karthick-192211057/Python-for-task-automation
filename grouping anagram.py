def anagram(l1):
    dictionary = {}
    for word in l1:
        sortedword=''.join(sorted(word))
        print(sortedword)
        if sortedword not in dictionary:
            dictionary[sortedword]=[word]
        else:
            dictionary[sortedword]+=[word]
    return [dictionary[i] for i in dictionary]
l1=['pop','bat','tab','opp']
print(anagram(l1))
