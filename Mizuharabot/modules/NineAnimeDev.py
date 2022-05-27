from Mizuharabot import telethn
from Mizuharabot.events import register

from animedev import client as AnimeDevClient, exceptions

@register(pattern='/search')
async def animedev_function(event):
    await event.reply(str(event.message.message))
    anime_name = event.message.message.split()
    if len(anime_name) <= 1:
        await event.reply('Please enter the anime name.\n\n<b>Example:</b>\n/search Doraemon.')
        return
    try:
        anime = AnimeDevClient.search(' '.join(anime_name[1:]))
    except exceptions.NotFound:
        await event.reply('Anime not found.')
        return
    except Exception as e:
        await event.reply(f'[ERROR]: {e}\n\nPlease report this at @Shinobu_Support.')
        return
    msg_text = f'''
Anime Title: {anime['AnimeTitle']}
    '''
    buttons = [[Button.url('Download Link', anime['AnimeLink'])], [Button.url('Search Query', anime['Search_Query'])]]
    await telethn.send_file(event.chat_id, anime['AnimeImg'], caption=msg_text)
