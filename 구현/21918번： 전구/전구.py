#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 21918                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/21918                          #+#        #+#      #+#     #
#    Solved: 2025/01/02 17:12:05 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
status=list(map(int,input().rstrip().split()))

for _ in range(m):
    num, l, r = map(int,input().rstrip().split())
    if(num==1):
        status[l-1]=r
    elif(num==2):
        for i in range(l-1,r):
            status[i] = 1 if status[i] == 0 else 0
    elif(num==3):
        for i in range(l-1,r):
            status[i]=0
    elif(num==4):
        for i in range(l-1,r):
            status[i]=1

for i in range(n):
        print(status[i],end=" ") 
