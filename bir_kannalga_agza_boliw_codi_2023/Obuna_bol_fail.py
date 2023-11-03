from aiogram import Bot, Dispatcher, executor,types

from config import Token_AIP
from aiogram.dispatcher.filters import CommandStart
from keyborts import sub_check
bot =Bot(Token_AIP)
dp = Dispatcher(bot)

CHANNEL = "@my_bots_2023"
#*********************************************************************#
def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False
            
#*********************************************************************#

@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL,user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id,"Salem  botimizga xush kelepsiz")
    else:
        await bot.send_message(message.from_user.id,"Usi kannalrga agza boliwiniz kerek!",reply_markup=sub_cehck)

@dp.message_handler()
async def echo_bot(message: types.Message):
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL,user_id=message.from_user.id)):
        if message.message_id == "MESSAGE":
            await bot.send_message(message.from_user.id, "zor emes")
        else:
            await bot.send_message(message.from_user.id, "bunday informatsaya joq bizde",)
    else:
        await bot.send_message(message.from_user.id,"Usi kannalrga agza boliwiniz kerek!",reply_markup=sub_cehck)

@dp.callback_query_handler(text="Agzan_tekesriw")
async def Agzan_tekesriw(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub(await bot.get_chat_member(chat_id=CHANNEL,user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id,f"Salem botimizga xush kelepsiz {message.from_user.full_name}")
    else:
        await bot.send_message(message.from_user.id,"Usi kannalrga agza boliwiniz kerek! ",reply_markup=sub_cehck)
    




if  __name__ == '__main__':
    executor.start_polling(dispatcher=dp,skip_updates=True)
