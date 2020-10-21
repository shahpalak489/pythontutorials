from collections import Counter 

def isAnagram(s, t):
    if len(s) == len(t):
        print("anagram is possible")
        print(Counter(s))
        print(Counter(t))
        if Counter(s) == Counter(t):
            print("it is a anagram")
        else:
            print("length is same but not anagram")
    else:
        print("length is different")

isAnagram('akh', 'lap')
# {'p':1, 'a':1,}

# akhil
# akh