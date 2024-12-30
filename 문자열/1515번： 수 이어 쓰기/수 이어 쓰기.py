#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1515                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: wnghks5432 <boj.kr/u/wnghks5432>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1515                           #+#        #+#      #+#     #
#    Solved: 2024/12/29 23:22:52 by wnghks5432    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = input().rstrip()
numbers = [int(num) for num in n]
i=1
length = len(numbers)
while i<length:
    if(numbers[i]>numbers[i-1]):
        i+=1
        continue
    else:
        j = numbers[i-1]
        while True:
            j+=1
            cnt=0
            if str(numbers[i]) in str(j):
                tmp = str(j).replace(str(numbers[i]),'',1)
                print(tmp)
                for k in range(i+1,length):
                    if  str(numbers[k]) in str(j) and cnt<len(str(j)):
                        tmp=tmp.replace(str(numbers[k]),'',1)
                        print(tmp)
                        cnt+=1
                    else:
                        break
                del numbers[i+1:i+1+cnt]
                numbers[i] = j
                length -= cnt
                i+=1
                break
print(numbers)
print(numbers[-1])                
