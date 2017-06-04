from TwitterFollowBot import TwitterBot
import sys
import random
import time

#decale le start du bot
if (len(sys.argv) < 3 or sys.argv[1] != "nowait"):
    time.sleep(random.random()*5+1)

#get arguments et lance bot
my_bot = TwitterBot()
#print(sys.argv[1])

#gestion du cache
#my_bot = TwitterBot()
#my_bot.sync_follows()

#FollowBack
my_bot.auto_follow_followers()

#autoRT something
#my_bot.auto_rt(sys.argv[1], random.randint(1,3))
