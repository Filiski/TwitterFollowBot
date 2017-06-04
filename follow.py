from TwitterFollowBot import TwitterBot
import sys
import random
import time

#decale le start du bot
if (len(sys.argv) < 3 or sys.argv[2] != "nowait"):
    time.sleep(random.random()*30+1)

#gestion du cache
my_bot = TwitterBot()
my_bot.sync_follows()

#decale le start du bot
if (len(sys.argv) < 3 or sys.argv[2] != "nowait"):
    time.sleep(random.random()*50+1)

#FollowBackUSer
my_bot.auto_follow_followers_of_user(sys.argv[1])
