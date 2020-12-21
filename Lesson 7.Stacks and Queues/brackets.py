"""
A string S consisting of N characters is considered to be properly nested 
if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, 
returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", 
the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..200,000];
        string S consists only of the following characters: 
        "(", "{", "[", "]", "}" and/or ")".

"""

# Brackets
def solution(S):
    #returns 1 if S is properly nested and 0 otherwise.

    #S is empty;
    if not S: 
        return 1

    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}

    for element in S:
        #S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        if element in brackets:
            stack.append(element)

        #S has the form "VW" where V and W are properly nested strings. 
        if element in brackets.values():
            
            if stack:
                if element == brackets[stack.pop()]:
                    continue
                else:
                    return 0

            else:
                return 0

    return 0 if stack else 1


S = "{[()()]}" 
print(solution(S))

S = "([)()]" 
print(solution(S))

#https://stackoverflow.com/questions/28951336/codility-brackets-determine-whether-a-given-string-of-parentheses-is-properly

