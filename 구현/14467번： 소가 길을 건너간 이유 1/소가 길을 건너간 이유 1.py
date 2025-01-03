#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14467                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14467                          #+#        #+#      #+#     #
#    Solved: 2025/01/02 16:50:04 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
cow_dict={}
cnt=0
n=int(input().rstrip())
for i in range(n):
    cow_num, cow_loc = map(int, input().rstrip().split())
    if cow_num in cow_dict:
        if cow_dict[cow_num] != cow_loc:
            cnt+=1
    cow_dict[cow_num] = cow_loc
print(cnt)