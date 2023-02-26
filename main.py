import os
from mealie_discord.bot import Bot
import logging

logger = logging.getLogger(__name__)

discord_token = os.getenv("DISCORD_TOKEN")
mealie_token = os.getenv("MEALIE_TOKEN")
mealie_url = os.getenv("MEALIE_URL")

logger.info("Starting bot")
Bot.run(discord_token, mealie_token, mealie_url)
