def solution(n, k):
    answer = 0
    service = 0
    if n >= 10:
        service = n // 10
    else:
        service = 0
    answer += n*12000 + k*2000 - service*2000
    return answer