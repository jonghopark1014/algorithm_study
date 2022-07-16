A, B = map(int, input().split())

xyz = {1:'가위', 2:'바위', 3:'보'}

if xyz[A] == ' 가위' and xyz[B] == '보':  
    print('A')
elif xyz[A] == '바위' and xyz[B] == '가위':  
    print('A')
elif xyz[A] == '보' and xyz[B] == '바위':  
    print('A')
else:  
    print('B')