
from wxpy import *
bot = Bot()

my_friend = bot.friends().search('wildChicken', sex=MALE)[0]

all = len(bot.friends())
msg = 'My man, I have ' + str(all) + ' friends! What about u?'
my_friend.send(msg)

#embed()
