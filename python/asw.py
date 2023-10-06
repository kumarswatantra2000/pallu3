#convert to roman to deci,mal number
def romanToDecimal(s):

    roman = {'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
    res = 0
    for i in range(len(s)) :
        if i+1 < len(s) and roman[s[i]] < roman[s[i+1]] :
            res -= roman[s[i]]
        else :

            res += roman[s[i]]
        return res
print(romanToDecimal("mi"))