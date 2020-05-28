# -*- coding: utf-8 -*-
import config.config as config
import telebot
from telebot import types


class product:
 def __init__(self, l=['пустота','залупа','дилдак', 'манда','хурга','медькойн','госткойн','abc','bcd','zalupa','хуйга','манда']):
  self.list=l
  
 def get(self):
  return self.list

 def remove(self, item):
  if item in self.list:
   self.list.remove(item)
  pass
 def add(self, item):
  self.list.append(item)
  pass


def initBot(row_width=config.width_keyboard):
  
  markup_all_commands = types.ReplyKeyboardMarkup(row_width=row_width)
  commands = ['/Магазин', '/Помощь', '/Описание', '/собачья_связь']
  prod = product()
  for comm in commands:
   markup_all_commands.add(comm)
  

  print("Start bot '"+config.nameShop+"' '"+config.token+"'")
  bot=telebot.TeleBot(config.token)# as bot:
  
  @bot.message_handler(commands=['getmyID','debuginfo'])
  def debug_handler(message):
   bot.reply_to(message, str(message) )


  @bot.message_handler(commands=['Помощь','help','help'])
  def help_handler(message):
   bot.reply_to(message, config.helpMessage % message.from_user.first_name, reply_markup=markup_all_commands)

  @bot.message_handler(commands=['собачья_связь','связь','админ'])
  def help_handler(message):
   bot.reply_to(message, config.ownerUserName, reply_markup=markup_all_commands)
  @bot.message_handler(commands=['Описание','движ'])
  def about_handler(message):
   bot.reply_to(message, "Да хуй знает... тестик это", reply_markup=markup_all_commands)

  @bot.message_handler(commands=['Магазин'])
  def shop_handler(message):
   products = prod.get()
   local_commands = types.ReplyKeyboardMarkup(row_width=row_width)
   for l in products:
    local_commands.add("купить "+l)
   if len(products) != 0:
    bot.reply_to(message, "Хуле надо? можешь сделать запрос на товар 'нихуя' командой /купить *tovar*", 
	reply_markup=local_commands)
   else:
    bot.reply_to(message, "Все раскупили брОтишь.", 
	reply_markup=local_commands)

  @bot.message_handler(func=lambda m: True)
  def echo_all(message):
        products = prod.get()
        com=message.text.split(' ')
        if "купить" in com[0] and com[1] in products:  
         bot.reply_to(message, '... обработачка по ебалу... готово. вы купили: %s' % com[1],reply_markup=markup_all_commands)
         prod.remove(com[1])

        elif "купить" in com[0]:
         bot.reply_to(message, '... закончилось ...: %s' % com[1],reply_markup=markup_all_commands)
        else:
         bot.reply_to(message, 'Команда: %s хуй пойми что это крч' % message.text)

  @bot.message_handler(commands=['start'])
  def weolcome_handler(message): # 
   bot.reply_to(message, config.welcomeMessage % (config.nameShop,message.from_user.first_name), reply_markup=markup_all_commands)



  @bot.message_handler(content_types=['document', "sticker", "pinned_message", "photo", "audio"])
  def handle_files_stickers(message):
  # bot.reply_to(message, "FILE? " + str(message)) 
   pass

  bot.polling()
initBot()
