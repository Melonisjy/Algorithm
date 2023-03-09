def solution(seoul):
    answer = 0
    for i in seoul:
        if "Kim" == i:
            break
        answer += 1
            
    return "김서방은 %d에 있다" % answer