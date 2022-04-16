import telebot
import time

bot = telebot.TeleBot('5371389783:AAEUy2EQYnkl7mfZHrNBS8o7fH1N762yPBg')

@bot.message_handler(commands = ['start'])
def start_message(message):
   bot.reply_to(message, 'welcome to @HackiOfficialBot \nChannel : @HackiOfficial \nBy : @HackiProduction')

@bot.message_handler(commands = ['salom'])
def salom_message(message1):
    bot.reply_to(message1, 'salomla')

@bot.message_handler(commands=['myid'])
def myid(message):
    user = bot.get_me()
    userid = user.id

@bot.message_handler(content_types = ['text'])
def send_message(message):
  if message.text.lower() == 'help':
  	 bot.send_message(message.chat.id, '1.Developer\n2.Official\n3.Production')
  elif message.text.lower() == 'developer':
     bot.send_message(message.chat.id, 't.me/Hacki_official')
     time.sleep(3)
     bot.send_message(message.chat.id, '@Hacki_official')
  elif message.text.lower() == 'official':
  	 bot.send_message(message.chat.id, 't.me/HackiOfficial')
  	 time.sleep(3)
  	 bot.send_message(message.chat.id, '@HackiOfficial')
  elif message.text.lower() == 'production':
     bot.send_message(message.chat.id, 't.me/HackiProduction')
     time.sleep(3)
     bot.send_message(message.chat.id, '@HackiProduction')
  elif message.text.lower() == 'gl.admin':
     bot.reply_to(message, 'Gl.Admin : ꧁☆An๏nץmͥ๏uͣsͫ ☆꧂ \nLink : @Hacki_Official\nid : 1921829817')
  elif message.text.lower() == 'myinformations':
  	 #bot.send_message(message.chat.id, 'ID : ')  	 
     bot.send_message(message.chat.id, message.from_user.id)
     time.sleep(5)
     #bot.send_message(message.chat.id, 'Username: ')
     bot.send_message(message.chat.id, message.from_user.first_name)
  if message.text.lower() == 'mute':
     bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)  
     bot.send_message(message.chat.id, " successfully, muted the user")
       
  elif message.text.lower() == 'unmute':
     bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)  
     bot.send_message(message.chat.id, "successfully, unmuted the user")            

  elif message.text.lower() == 'admin panel':
  	 bot.send_message(message.chat.id, 'ping code')
  elif message.text.lower() == '9089':
  	 bot.send_message(message.chat.id, 'ping code is true!')
  	 time.sleep(5)
  	 bot.send_message(message.chat.id, '1.My Dokuments')
  	 time.sleep(2)
  	 bot.send_message(message.chat.id, '2.My Ideas')
  	 time.sleep(2)
  	 bot.send_message(message.chat.id, '3.My Production')
  	 time.sleep(2)
  	 bot.send_message(message.chat.id, '4.My Official Channel')
  #else: 
  	#bot.send_message(message.chat.id, 'Syntax Error!')
  if message.text.lower() == 'my dokuments':
    bot.send_message(message.chat.id, 'send admin ping code')
  elif message.text.lower() == '****':
    bot.send_message(message.chat.id, 'Scanning.....')
    time.sleep(5)
    bot.send_message(message.chat.id, 'Admin ping code is True!')
  #if message.text.lower() == 'why error?':
  #else: 
     #while True:
         #bot.send_message(message.chat.id, 'Syntax Error!')
         #message.from_user.id     	

bot.polling(none_stop = True)
