n=int(input())
arr=list(map(int,input().split()))

if len(arr)>n:
    print(f"You have entered {len(arr)} numbers. expected {n} number/s.")
    
    arr=arr[:n]

main_arr=list(set(arr))
if len(main_arr)<2:
    print(-1)
else:
    main_arr.sort(reverse=True)
    print(main_arr[1])

