def solution(S):
    count = 0
    characters = set(S)

    for character in characters:
        char_count = S.count(character)
        if char_count % 2 != 0:
            count += 1

    return count

print(solution("acbcbba"))  #return 1
print(solution("axxaxa"))   #return 2
print(solution("aaaa"))     #return 0