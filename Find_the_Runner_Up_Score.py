n = int(input())

scoreList = list(map(int, input().split()))

maxScore = float('-inf')
runnerUpScore = float('-inf')

for score in scoreList:
    if score > maxScore:
        runnerUpScore = maxScore
        maxScore = score
    elif score > runnerUpScore and score != maxScore:
        runnerUpScore = score

print(runnerUpScore)