def solution(n):
    answer = ''
    a = "수"
    b = "박"
    if n % 2 == 0:
        answer = (a+b)*(n//2)
    else:
        answer = (a+b)*(n//2) + a
    return answer