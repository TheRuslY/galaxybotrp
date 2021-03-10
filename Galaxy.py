import discord

matbl = ["бля", "сука", "блять", "хуй", "иди нахуй", "пососи,", "пидор", "пиздец", "еблан", "ебать", "говно", "говноед",
         "пиздабол"]

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if msg in matbl:
        await message.channel.send('Материться - плохо')
    if message.content.startswith('!правила'):
        await message.channel.send('Правила приняли ислам')
    if message.content.startswith('!сервера'):
        await message.channel.send('Сервера приняли ислам')


client.run("Nzg2NDM3NzkzNTgwNDQ5ODIy.YEaeIg.HN6BZxLkouXMT7MEcXacxXluI0s", bot=False)
