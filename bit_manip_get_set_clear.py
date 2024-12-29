num = 129909780 
original = num
i = 17
ans = []
while num > 1:
    ans.append(num  % 2)
    num = num // 2
ans.append(num)
start = 0
end = len(ans) - 1
ith_bit = ans[i-1]
if ans[i-1] == 1:
    set_ith_bit = original
else:
    set_ith_bit = original + 2**(i-1)
if ans[i-1] == 0:
    clear_ith_bit = original
else:
    clear_ith_bit = original - 2**(i-1)
print(ith_bit , set_ith_bit , clear_ith_bit)
