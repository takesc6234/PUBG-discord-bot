# PUBG-discord-bot
Gives random drop locations with !mapname type command.
Currently map data is stored in lists for easy access, you may add new maps and locations in similar manner.
there is a 1 command per minute per map command cooldown to prevent spamming the function repeatedly. You may increase or decrease this at will, the cooldown by manipulating numbers in: @commands.cooldown(1, 60, commands.BucketType.user) argument where "1" is command call restrictor and "60" is time period in seconds. If you want to adjust total call amounts globally you can substitute "commands.BucketType.-user-" to be commands.BucketType.default in this case the cooldown will be applied all users and all instances where the bot is being used.
