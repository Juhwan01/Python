#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10798                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10798                          #+#        #+#      #+#     #
#    Solved: 2024/11/17 20:14:15 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
result=[]
final_result=""
for i in range(5):
    sub_result = (list(map(str, input())))
    result.append(sub_result)

for i in range(15):
    for j in range(5):
        if i <len(result[j]):
            final_result += result[j][i]
print(final_result)