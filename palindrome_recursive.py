string = " "
def check_palindrome(string , start , end):
    if start > end or string[start] != string[end]:
        return 0
    else:
        check_palindrome(string , start + 1 , end - 1)
    return 1
ans = check_palindrome(string , 0 , len(string) - 1)
print(ans)
