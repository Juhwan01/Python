#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9046                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9046                           #+#        #+#      #+#     #
#    Solved: 2024/11/17 19:34:16 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n=int(input())
cnt=0
result=[]
final_result=[]
for _ in range(n):
    alpha=(list(map(str,input().replace(' ',""))))
    for a in alpha:
        if alpha.count(a)>cnt:
            cnt=alpha.count(a)
            result.clear()
            result.append(a)
        elif alpha.count(a)==cnt:
            if a not in result:
                result.append(a)
    if len(result)>1:
        final_result.append('?')
    else:
        final_result.append(result[0])
    result.clear()
    cnt=0

for i in final_result:
    print(i)

