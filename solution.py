def golf():
    if input()=='0':print(0)
    else:
        r=5526
        for t in map(int, input().split()):
            if abs(t)==abs(r) and t>r or abs(t)<abs(r):r=t
        print(r)