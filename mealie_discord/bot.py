import discord
import logging
from mealie_discord.mealie import Mealie
from discord.ext import commands

logger = logging.getLogger(__name__)


class Bot:
    @staticmethod
    def run(discord_token, mealie_token, mealie_url):
        intents = discord.Intents(messages=True, message_content=True)

        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            logger.info(f"We have logged in as {client.user}")

        @client.event
        async def on_message(message):
            logger.info(f"New message {message}")
            # Don't respond to ourselves
            if message.author == client.user:
                return

            if message.content == "comida":
                logger.info(f"Food request by {client.user}")
                await message.channel.send(
                    Mealie.get_todays_meal_message(mealie_token, mealie_url)
                )

        client.run(discord_token)
