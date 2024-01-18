# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from pyLuci import *
from pyLuci import _ayra_cache
from pyLuci._misc import owner_and_sudos
from pyLuci._misc._assistant import asst_cmd, callback, in_pattern
from pyLuci.fns.helper import *
from pyLuci.fns.tools import get_stored_file
from telethon import Button, custom

from modules import ATRA_COL, InlinePlugin
from strings import get_languages, get_string

OWNER_NAME = ayra_bot.full_name
OWNER_ID = ayra_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Ada yang salah`")


def get_back_button(name):
    return [Button.inline("Kembali", data=f"{name}")]
