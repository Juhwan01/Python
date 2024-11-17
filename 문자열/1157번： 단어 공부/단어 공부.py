#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1157                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1157                           #+#        #+#      #+#     #
#    Solved: 2024/11/17 20:59:31 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n=(list(map(str,input().upper())))
alpha=(list(set(n)))
b=[]
for i in alpha:
    b.append(n.count(i))
if b.count(max(b))>1:
    print("?")
else:
    print(alpha[b.index(max(b))])
