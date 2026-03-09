def is_odd():
    return lambda a:a%2!=0
        
def is_prime():
    def check(a):
        if a<=1:
            return False
        if a==2:
            return True
        if a%2==0:
            return False
        i=3
        while i*i<=a:
            if a%i==0:
                return False
            i+=2
        return True
    return check    

def is_Palindrome():
    def check(a):
        orig_num=a
        rev_num=0
        while a>0:
            digit=a%10
            rev_num=rev_num*10+digit
            a//=10
        return orig_num == rev_num    
    return check    
t=int(input())
for _ in range(t):
    condition,number=map(int,input().split())
    if condition==1:
        op=is_odd()
        print(True if op(number) else False)
    elif condition==2:
        op=is_prime()
        print(True if op(number) else False)
    elif condition==3:
        op=is_Palindrome()
        print(True if op(number) else False)
               



