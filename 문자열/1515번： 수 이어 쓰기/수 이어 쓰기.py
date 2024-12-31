#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1515                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1515                           #+#        #+#      #+#     #
#    Solved: 2024/12/29 23:22:52 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
n = input().rstrip()

num = 1
idx = 0
while idx < len(n):
    curr = str(num)
    for c in curr:
        if idx < len(n) and c == n[idx]:
            idx += 1
    num += 1

print(num - 1)