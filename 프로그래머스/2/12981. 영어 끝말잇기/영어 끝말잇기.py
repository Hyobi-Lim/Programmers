def solution(n, words):
    answer = [0,0]
    for i in range(len(words)):
        if i==0:
            continue
        elif words[i-1][len(words[i-1])-1]!=words[i][0] or words[i] in words[:i]:
            answer[0]=i%n+1
            answer[1]=i//n+1
            break
        else:
            continue
    return answer