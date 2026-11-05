
s = [input() for _ in range(5)]
ans = 5
# 枚举5行
for i in range(5):
    cnt = s[i].count('.')
    ans = min(ans, cnt)
# 枚举5列
for j in range(5):
    cnt = 0
    for i in range(5):
        if s[i][j] == '.':
            cnt += 1
    ans = min(ans, cnt)

# 主对角线（左上到右下）
cnt = 0
for i in range(5):
    if s[i][i] == '.':
        cnt += 1
ans = min(ans, cnt)

# 副对角线（右上到左下）
cnt = 0
for i in range(5):
    if s[i][4 - i] == '.':
        cnt += 1
ans = min(ans, cnt)

print(ans)
