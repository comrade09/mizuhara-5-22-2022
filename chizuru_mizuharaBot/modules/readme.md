# chizuru_mizuhara  Example plugin format

## Basic: Simple Plugins
```python3

from chizuru_mizuharaBot.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="Hi")
@disableable_dec("Hi")
async def _(message):
    j = "Say Hello There Im chizuru_mizuhara "
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im chizuru_mizuhara 
"""
```

## Basic: Env Vars
```python3
# You can import env like this. If config present auto use config

from chizuru_mizuharaBot.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str
from chizuru_mizuharaBot.conf import get_int_key, get_str_key

HI_STRING = get_str_key("HI_STRING", required=True) # String
MULTI = get_int_key("MULTI", required=True) #Intiger

@register(cmds="Hi")
@disableable_dec("Hi")
async def _(message):
    j = HI_STRING*MULTI
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im chizuru_mizuhara 
"""
```



## Advanced: Pyrogram
```python3
from chizuru_mizuharaBot.pyrogramee.pluginhelpers import admins_only
from chizuru_mizuharaBot import pbot

@pbot.on_message(filters.command("hi") & ~filters.edited & ~filters.bot)
@admins_only
async def hmm(client, message):
    j = "Hello there"
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im chizuru_mizuhara 
"""
```

## Advanced: Telethon
```python3

from chizuru_mizuharaBot.telethon import tbot
from chizuru_mizuharaBot.events import register

@register(pattern="^/hi$")
async def hmm(event):
    j = "Hello there"
    await event.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There Im chizuru_mizuhara 
"""
```
