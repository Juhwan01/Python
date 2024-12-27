#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1764                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1764                           #+#        #+#      #+#     #
#    Solved: 2024/12/27 23:25:49 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input =sys.stdin.readline
name_list1=[]
a,b=map(int,input().split())
for i in range(a):
    name=input().rstrip()
    name_list1.append(name)
set1=set(name_list1)
name_list2=[]
for i in range(b):
    name=input().rstrip()
    name_list2.append(name)
set2=set(name_list2)
result=set1&set2
print(len(result))
result=sorted(result)
for name in result:
    print(name)