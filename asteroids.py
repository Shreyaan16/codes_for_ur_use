asteroids = [-2,-1,1,2]
ans = []
for i in range(len(asteroids)):
    if len(ans) == 0:
        ans.append(asteroids[i])
        max_index = 0
    else:
        if asteroids[i] * ans[max_index] > 0:
            ans.append(asteroids[i])
            if abs(ans[max_index]) < asteroids[i]:
                max_index = len(ans) - 1
        else:
            if abs(asteroids[i]) < abs(ans[max_index]):
                ans = ans[:max_index+1]
            elif abs(asteroids[i]) == abs(ans[max_index]):
                ans = ans[:max_index]
            else:
                ans = []
                ans.append(asteroids[i])
print(ans)
