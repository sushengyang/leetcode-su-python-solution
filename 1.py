

def findallanagrams(s,p):
    hash={}
    for c in p:
        hash[c] = hash.get(c,0)+ 1
    left = right = 0
    cnt = len(p)
    res= []
    while right < len(s):
        if hash[s[right]] >=1:
            cnt  -= 1   # window length - 1
        hash[s[right]] -= 1  # hash value - 1
        right+=1   # move right
        if cnt ==0:  # util window length = 0 , p disappears
            res.append(left)  #
        if right -left ==len(p):
            if hash[s[left]] >=0:
                cnt +=1
            hash[s[left]] +=1
            left +=1
    return res

print findallanagrams("abab", "ab")

