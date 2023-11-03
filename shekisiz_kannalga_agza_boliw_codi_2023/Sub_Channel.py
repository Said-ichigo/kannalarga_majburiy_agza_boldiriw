from aiogram import Bot, Dispatcher, executor,types
from Config import Token_AIP,CHANNELS,NOT_FOUN_CHANNELS
from aiogram.dispatcher.filters import CommandStart
from Keyborts import sub_check
bot =Bot(Token_AIP)
dp = Dispatcher(bot)


#*********************************************************************#
async def check_subs_2023(channels,user_id):
    for channel in channels:
        chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True
            
#*********************************************************************#

@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    if await check_subs_2023(CHANNELS, message.from_user.id):
        await bot.send_message(message.from_user.id,"Hello")
    else:
        await bot.send_message(message.from_user.id,NOT_FOUN_CHANNELS,reply_markup=sub_check)

@dp.callback_query_handler(text="Agzan_tekesriw")
async def Agzan_tekesriw(message: types.Message):  
    await bot.delete_message(message.from_user.id, message.message.message_id)
    if await check_subs_2023(CHANNELS, message.from_user.id):
        await bot.send_message(message.from_user.id,"Hello")
    else:
        await bot.send_message(message.from_user.id,"Iltimas usi kannalraga agza bolin :}",reply_markup=sub_check)
    

if  __name__ == '__main__':
    executor.start_polling(dispatcher=dp,skip_updates=True)