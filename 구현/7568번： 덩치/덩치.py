#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7568                           #+#        #+#      #+#     #
#    Solved: 2025/01/04 00:03:33 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

member_list={}
result_list={}

num = int(input().rstrip())
for i in range(num):
    inform=list(map(int,input().rstrip().split()))
    member_list[i+1]=inform

sorted_list=sorted(member_list.items(), key = lambda x:x[1][0],reverse=True)
result=sorted(sorted_list, key = lambda x:x[1][1],reverse=True)
print(result)

for i in range(num):
    member=result[i][0]
    result_list[member]=i+1

for i in range(num):
    print(result_list.get(i+1),end=" ")