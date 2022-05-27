# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if len(word) == len(anagram):
        for i in word:
            if i not in anagram:                
                return False
        return True
    else:
       return False 

print(find_anagram("hello", "check") )
print(find_anagram("below", "elbow"))  


