#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2024/12/29 22:43:48 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        dic[word] = dic.get(word, 0) + 1

dic = sorted(dic.items(), key = lambda x : x[0])
dic = sorted(dic, key = lambda x : len(x[0]), reverse = True)
dic = sorted(dic, key = lambda x : x[1], reverse = True)

for i in dic:
    print(i[0])
