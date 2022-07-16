N = int(input())
score = list(map(int, input().split()))
score.sort()

for i in range(N):  
    if i == N//2:  
        print(score[i])
