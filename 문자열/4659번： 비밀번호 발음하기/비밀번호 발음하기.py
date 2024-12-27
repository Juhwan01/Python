#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4659                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4659                           #+#        #+#      #+#     #
#    Solved: 2024/12/27 22:01:47 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

def judge(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel in string:
            break
    else:
        return False
    for i in range(len(string)-2):
        a, b, c = string[i], string[i+1], string[i+2]
        if (a in vowels) and (b in vowels) and (c in vowels):
            return False
        if (a not in vowels) and (b not in vowels) and (c not in vowels):
            return False
    for i in range(len(string)-1):
        a, b = string[i], string[i+1]
        if a == b and a != 'e' and a != 'o':
            return False
    return True

while True:
    string = input().rstrip()
    if string == 'end':
        break
    if judge(string):
        print(f'<{string}> is acceptable.')
    else:
        print(f'<{string}> is not acceptable.')
