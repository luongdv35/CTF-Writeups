#Subset Sum Problem
#https://imgs.xkcd.com/comics/np_complete.png
import random
choices = list(set([random.randint(100000,1000000000) for _ in range(30)]))
random.shuffle(choices)
winners = choices[:15]
target = sum(winners)
winners.sort()
flag = "UDCTF{%s}" % ("_".join(map(str,winners)))
#print(flag)
choices.sort()
print(choices)
print(target)

# [19728964, 30673077, 137289540, 195938621, 207242611, 237735979, 298141799, 302597011, 387047012, 405520686, 424852916, 461998372, 463977415, 528505766, 557896298, 603269308, 613528675, 621228168, 654758801, 670668388, 741571487, 753993381, 763314787, 770263388, 806543382, 864409584, 875042623, 875651556, 918697500, 946831967]
# 7627676296
