def isPalindrome(s: str):
n = len(s)
for i in range(n//2):
    if(s[i]!= s[n-1-i]):
        break
return (i== n//2 -1)