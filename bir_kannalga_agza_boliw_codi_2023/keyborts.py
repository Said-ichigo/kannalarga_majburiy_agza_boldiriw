from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

sub_cehck=InlineKeyboardMarkup(
    inline_keyboard=[
        [
           InlineKeyboardButton(text="Kannalga agza bolin!",url="https://t.me/my_bots_2023"),   
        ],
        [
           InlineKeyboardButton(text="Kannalga agza bolin!",url="https://t.me/aio_flag"),  
        ],
        [
           InlineKeyboardButton(text="Kannalga agza bolgandi tekseriw?",callback_data="Agzan_tekesriw") 
        ]
    ]
)