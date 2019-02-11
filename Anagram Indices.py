import collections

def anagram_indices(word, s):
    result = []
    freq = collections.Counter(word)
    for char in s[:len(word)]:
        freq[char] -=1
        if freq[char] == 0:
            del freq[char]
    if len(freq)==0:
        result.append(0)
    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]
        freq[start_char]+=1
        freq[end_char] -=1
        if freq[start_char] == 0:
            del freq[start_char]
        if freq[end_char] == 0:
            del freq[end_char]
        if len(freq)==0:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)
    return result

print anagram_indices("korf","geekforgeeks")