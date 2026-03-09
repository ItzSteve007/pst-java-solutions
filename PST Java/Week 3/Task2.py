def splitnum(n,list1):
    word_list=[]
    for i in range(len(word)-n+1):
        s=word[i:n+i]
        word_list.append(s)
    word_list.sort()   
    print(word_list)   
    return f"the smallest is {word_list[0]} and the largest is {word_list[-1]}"
word=input()
n=int(input())

result=splitnum(n,word)
print(result)

