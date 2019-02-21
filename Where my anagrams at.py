def anagrams(word, words):
    res_anagram=[]
    word_dict={i:word.count(i) for i in word}
    for wordy in words:
        if all(True if sym in word_dict and wordy.count(sym) == word_dict[sym] else False for sym in wordy):
            res_anagram.append(wordy)
    return res_anagram

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

