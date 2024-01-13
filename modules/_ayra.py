# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from . import LOG_CHANNEL, Button, asst, ayra_cmd, eor, get_string

REPOMSG = """
◈ **Lucifer X UserBot** ◈\n
◈ Repo - [Click Here](https://github.com/jonesroot/Lucifer-UserBot)
◈ Support - @GokilSupport
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/jonesroot/Lucifer-UserBot"),
    ],
    [Button.url("Support Group", "t.me/GokilSupport")],
]

AYSTRING = """🎇 **Thanks for Deploying Lucifer-UserBot**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ayra_cmd(pattern="Repo$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        rs.chat_id,
        AYSTRING,
        file="https://telegra.ph//file/26e162bf339e4807c1286.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
