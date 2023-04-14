from aiogram import types
from data.config import ADMINS

from loader import dp
from utils import photo_link

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    await msg.answer(link)


@dp.message_handler(commands='info')
async def info_handler(msg: types.Message):
    # user = msg.
    username = msg.from_user.username
    full_name = msg.from_user.full_name
    user_id = msg.from_user.id
    chat_lang = msg.from_user.language_code
    await msg.answer(
        "<b>Uer Info:</b>\n"
        "\t <b>Username</b>: @{0}\n"
        "\t <b>ID:</b> {1}\n"
        "\t <b>Full Name:</b> {2}\n"
        "\t <b>Language Code:</b> {3}\n".format(username, user_id, full_name, chat_lang)
    )