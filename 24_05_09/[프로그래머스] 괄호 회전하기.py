def solution(s):
    answer = 0

    ReversedList = []
    ForwardList = []

    StrList = [["{", "[", "("], ["}", "]", ")"]]

    StrDict = \
        {
            "{": "}",
            "[": "]",
            "(": ")"
        }
    '''
    # for i, val in enumerate(s):
    #     if val in StrList[0]:
    #         if not BigRangeStr:
    #             BigRangeStr += 1
    #             answer += 1
    #         ForwardList.append(val)
    #     elif BigRangeStr \
    #             and val in StrList[1]:
    #         if StrDict[ForwardList.pop()] == val:
    #             BigRangeStr -= 1
    #         else:
    #             return 0
    #     else:
    #         ReversedList.append(val)

    # print(ForwardList, ReversedList)

    # if len(ForwardList) != len(ReversedList):
    #     return 0
    # for key, val in zip(ForwardList[::-1], ReversedList):

    #     if StrDict[key] == val:
    #         continue
    #     else:
    #         return 0
    '''

    start = 0
    end = len(s) - 1

    while (True):
        if start > end:
            break
        if s[start] in StrList[0]:
            ForwardList.append(s[start])
            start += 1
            continue

        if ForwardList:
            if StrDict[ForwardList.pop()] != s[start]:
                return 0
            elif not ForwardList:
                answer += 1
            start += 1
            continue

        if s[end] in StrList[1]:
            ReversedList.append(s[end])
            end -= 1
            continue

        if ReversedList:
            if StrDict[s[end]] != ReversedList.pop():
                return 0
            end -= 1
            continue
        
        if s[end] in StrList[0] and StrDict[s[end]] == s[start]:
            answer = 1
            start += 1
            end -= 1
            continue

        return 0

    if ForwardList or ReversedList:
        return 0
    return answer


s = "}(){{}"
print(solution(s))

'''

결국 가장 큰 범위에서 정상적인 구간이 몇개있는지 찾는 문제


'''
