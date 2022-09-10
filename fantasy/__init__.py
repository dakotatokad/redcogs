import json
from fantasy import Path

from redbot.core.bot import Red

from .fantasy import football

def setup(bot: Red)-> None:
  """Load Football cog."""
  cog = football()
  bot.add_cog(cog)
