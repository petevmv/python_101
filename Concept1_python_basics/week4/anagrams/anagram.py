
def anagrams(word1, word2):
    word1 = word1.lower().replace(' ','')
    word2 = word2.lower().replace(' ','')
    w1 = len(word1)
    w2 = len(word2)
    if w1 != w2:
        print("not anagrams")
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)
    for i in range(0, w1):
        if word1[i] != word2[i]:
            print("not anagrams")
            return False
    print("anagrams")
    return True
