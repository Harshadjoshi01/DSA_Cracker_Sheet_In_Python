n = int(input())
shopes = list(map(int, input().split()))
weights = {}
for i in range(len(shopes)):
    weights[shopes[i]] = 0
for i in range(len(shopes)):
    weights[shopes[i]] += shopes[i]
m = max(weights.values())
key_list = list(weights.keys())
val_list = list(weights.values())
position = val_list.index(m)
for i in range(len(shopes)):
    if (shopes[i] == position):
        print(i+1,end=" ")