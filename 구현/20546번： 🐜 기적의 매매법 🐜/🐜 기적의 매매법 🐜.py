#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20546                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20546                          #+#        #+#      #+#     #
#    Solved: 2025/01/03 22:39:39 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

account = int(input().rstrip())

junhyun_account=account
junhyun_cnt=0
sungmin_account=account
sungmin_cnt=0

chart_list=list(map(int,input().rstrip().split()))
    

for i in range(14):
    if junhyun_account//chart_list[i]>0:
        junhyun_cnt+= junhyun_account//chart_list[i] 
        junhyun_account-=junhyun_account//chart_list[i]*chart_list[i]

    if(i>2):
        if chart_list[i-3]>chart_list[i-2]>chart_list[i-1]:
            sungmin_cnt+=sungmin_account//chart_list[i]
            sungmin_account-= sungmin_account//chart_list[i]*chart_list[i]
        elif chart_list[i-3]<chart_list[i-2]<chart_list[i-1]:
            sungmin_account+=sungmin_cnt*chart_list[i]
            sungmin_cnt=0

junhyun_account+=junhyun_cnt*chart_list[13]
sungmin_account+=sungmin_cnt*chart_list[13]
if junhyun_account==sungmin_account:
    winner="SAMESAME"
elif junhyun_account>sungmin_account:
    winner="BNP"
else:
    winner="TIMING"
print(winner)
    