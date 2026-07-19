def kk(inp1):
    n=len(inp1)
    ans=0
    for start in range(n):
        pos= start  
        curr_len=0
        block_len=2
        
        while True:
            expected=""
            for i in range(block_len):
                expected+=chr(ord('a')+i)
            if pos<=n and inp1[pos:pos+block_len]==expected:
                curr_len+=block_len
                ans=max(ans,curr_len)
                pos+=block_len
                block_len+=1
            else:
                break
        return ans
inp1="ababcabcd"
print(kk(inp1))

def stronger(n,arr):
    ct=0
    for i in range(n):
        left=0
        right=0
        for j in range(i):
            if arr[j]>arr[i]:
                left+=1
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                right+=1
        if left>right:
            ct+=1
    return ct
print(stronger(5,[4,3,5,2,1]))   




from collections import Counter
def get_priority(ch):
    if ch.isdigit():
        return(0,ch)
    if ch.isupper():
        return(1,ch)
    if ch.islower():
        return(2,ch)
def rearrange(n,s):
    freq=Counter(s)
    res=[]
    while freq:
    maxfreq=max(freq.values())
    chars=[]
    for ch in freq:
        if freq[ch]==maxfreq:
            chars.append(ch)
    chars.sort(key=get_priority)
    for ch in chars:
        res+=ch
        freq[ch]-=1
        if freq[ch]==0:
            del freq[ch]
    return "".join(res)
n=10
s="abccaAdA"
print(rearrange(n,s))            
        
