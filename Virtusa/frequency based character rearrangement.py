from collections import Counter

def get_priority(ch):
    if ch.isdigit():
        return (0, ch)
    if ch.isupper():
        return (1, ch)
    if ch.islower():
        return (2, ch)

def rearrange(n, s):
    freq = Counter(s)
    res = []

    while freq:
        maxfreq = max(freq.values())
        chars = []

        for ch in freq:
            if freq[ch] == maxfreq:
                chars.append(ch)

        chars.sort(key=get_priority)

        for ch in chars:
            res.append(ch)
            freq[ch] -= 1

        for ch in chars:
            if freq[ch] == 0:
                del freq[ch]

    return "".join(res)

n = 10
s = "abccaAdA"
print(rearrange(n, s))
