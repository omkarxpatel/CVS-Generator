# this entire file is not used to generate
# the contents of this file are just used to set up the discord bot
# go to cogs/gen.py

import os
import discord
import aiohttp
from colorama import Fore
from pkgutil import iter_modules
import traceback
from discord.ext import commands, tasks


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='-',
                         intents=discord.Intents.all(),
                         activity=discord.Activity(
                             type=discord.ActivityType.watching,
                             name="JcPenny"),
                         owner_ids=[994657968933060708, 760904134688899132])
        self.initial_extensions = [
            m.name for m in iter_modules(['cogs'], prefix='cogs.')
        ]

    async def setup_hook(self):
        self.background_task.start()
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions:
            try:
                await self.load_extension(ext)
                print(f"{Fore.GREEN} {ext} loaded {Fore.RESET}")
            except:
                print(f"{Fore.RED} {ext} not loaded {Fore.RESET}")
                print(traceback.print_exc(limit=None, file=None, chain=True))

    @tasks.loop(minutes=10)
    async def background_task(self):
        print('Running background task...')

    async def close(self):
        await super().close()
        # await self.session.close()

    async def on_ready(self):
        print(Fore.MAGENTA + "========[ " + bot.user.name +
              " is Online! ]========" + Fore.RESET)
        print(Fore.RED + "========[ Discord Version: " + discord.__version__ +
              " ]=======")


bot = MyBot()
my_secret = os.environ['TOKEN']
bot.run(my_secret)