import time
from random import randint


# module specified in the config file
for i in range(1, 85):
    print('')

n = ' '
for i in range(1,1000):
    count = randint(1,100)

    while count>0:
        n += " "
        count -= 1
    if i % 10 == 0:
        print(n + "🎉🎂🎈Happy Birthday Shayla🎂🎉🎈!" )
    elif i % 9 == 0:
        print(n + "🎂🎉🎈🍫💖🎊🍰")
    elif i % 5 == 0:
        print(n + "🎊🎉🎂 17! 🎉🎂🎊")
    elif i % 8 == 0:
        print(n + "🎉✨🎶🎉🎊")
    elif i % 7 == 0:
        print(n + "🍫🎁🪅🎇🌟")
    elif i % 6 == 0:
        print(n + "🎂🎉🎈Happy Birthday Shayla!💖🎊🍰")
    else:
        print(n + "🔸🎉🎂🎈🍫💖🎊🍰🎁🪅🎇🌟🎶✨")
    time.sleep(.5)

