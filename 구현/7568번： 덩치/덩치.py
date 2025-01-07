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
    member_list[i]=inform

for i in range(num):
    member=member_list.get(i)

sorted_list1=sorted(member_list.items(), key = lambda x:x[1][0],reverse=True)
sorted_list2=sorted(sorted_list1, key = lambda x:x[1][1],reverse=True)
i=0
while(i<num):
    member1=sorted_list1[i][0]
    member2=sorted_list2[i][0]
    if(member1==member2):
        result_list[member1]=i+1
    else:
        for j in range(num):
            if(member1==sorted_list2[j]):
                result_list[member1]=i+1

    
# for i in range(num):
#     member=result[i][0]
#     result_list[member]=i+1

# for i in range(num):
#     result
# for i in range(num):
#     print(result_list.get(i+1),end=" ")