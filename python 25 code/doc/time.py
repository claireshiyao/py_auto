# author by claire

import datetime
import time

# cur1 = datetime.datetime.now()
# time.sleep(3)
# cur2 = datetime.datetime.now()
#
# print(cur1)
# print(cur2)
# print(cur2 - cur1)
# 2020-03-25 11:00:42.446134
# 2020-03-25 11:00:45.447113
# 0:00:03.000979

# cur1 = int(time.time())
# time.sleep(3)
# cur2 = int(time.time())
#
# print(cur1)
# print(cur2)
# print(cur2 - cur1)
# 1585105091
# 1585105094
# 3

# now = time.strftime("%Y-%m-%d %H_%M_%S")
now = time.strftime("%Y-%m-%d")
print(now)
# 2020-03-25 11_01_56
# 2020-03-25

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 2020-03-25 11:06:56