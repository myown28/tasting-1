#~~~ A1 ~~~
from myown.mods import *
import datetime

now = datetime.datetime.now()
m = (now.strftime('%M'))
m = int(m)

clear()
a1 = int(input('m'))
if a1 == m:
    print('yes')
    myt(1.5)
    clear()
else:
    print('no')
    myt(1.5)
    clear()

#~~~ A2 ~~~
from myown.myrandom import myrandom
a = myrandom(5)
