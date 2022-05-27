from Mizuharabot import pbot
from pyrogram import filters

from animedev import client as AnimeDevClient, exceptions

@pbot.on_message(filters.command('search'))
async def animedev_function(client, message):
    anime_name = message.text.split()
    if len(anime_name) <= 1:
        await message.reply_text('Please enter the anime name.\n\n<b>Example:</b>\n/search Doraemon.')
        return
    try:
        anime = AnimeDevClient.search(' '.join(anime_name[1:]))
    except exceptions.NotFound:
        await message.reply_text('Anime not found.')
        return
    except Exception as e:
        await message.reply_text(f'[ERROR]: {e}\n\nPlease report this at @Shinobu_Support.')
        return
    msg_text = f'''
Anime Title: {anime['AnimeTitle']}
    '''
    buttons = InlineKeyboardMarkup[
        [InlineKeyboardButton('Download', anime['AnimeLink'])],
        [InlineKeyboardButton('Search Query', anime['Search_Query'])]
        ]
    await message.reply_photo(anime['AnimeImg'], caption=msg_text, reply_markup=buttons)
