T = int(input())

for testcase in range(1, T+1):  
    N = int(input())
    text = ''
    for a in range(N):  
        Ci, Ki = input().split()
        text += Ci * int(Ki)
    
    print('#{}'.format(testcase))

    for b in range(0, len(text), 10):
        print(text[b : b+10])  