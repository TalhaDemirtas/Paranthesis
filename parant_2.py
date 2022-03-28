#sieve method
x=input('Enter text = ')
def isValid(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()','').replace('[]','').replace('{}','')
    print(not s)
isValid(x)