from Monu.core.bot import MonuBot
from Monu.core.dir import dirr
from Monu.core.git import git
from Monu.core.userbot import Userbot
from Monu.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

dbb()

heroku()

sudo()

# Clients
app = MonuBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
