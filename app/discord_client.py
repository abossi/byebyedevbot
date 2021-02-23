import discord
from app.core.config import Config


class DiscordClient():
    def __init__(self, bot_secret_key):
        # needed to detect join server
        default_intents = discord.Intents.default()
        default_intents.members = True

        self._client = discord.Client(intents=default_intents)
        self._bot_secret_key = bot_secret_key

        @self._client.event
        async def on_ready():
            print('Bot is ready')

        @self._client.event
        async def on_member_join(member):
            print("member join")
            welcome_channel = self._client.get_channel(int(Config().get("welcome.location")))
            await welcome_channel.send(Config().get("welcome.message").format(name=member.display_name))

    def run(self):
        self._client.run(self._bot_secret_key)
