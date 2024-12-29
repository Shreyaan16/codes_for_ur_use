s = "level"
ans = ""
start = 0
end = len(s) - 1
while end > start:
    while end > -1 and s[end] != s[start]:
        end -= 1
    flag = True
    max_pre = ""
    for i in range(len(s) - end):
        if s[i] != s[end+i]:
            flag = False
            break
        max_pre += s[i]
    if len(max_pre) > len(ans) and flag == True and end > start:
        ans = max_pre
    end -= 1
print(ans) 
