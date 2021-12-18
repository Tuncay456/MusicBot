from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        '⬇️ The commands and there use is explained here ⬇️\x1f- `/play` To search the song on Youtube and play the first matching result.\x1f- `/song` To download a song from youtube.\x1f- `/play` Reply this in response to a link or any telegram audio file it will be played \x1f- `/skip` to skip current song \x1f- `/end` to stop the streaming of song \x1f- `/pause` to pause the stream \x1f- `/resume` to resume the playback. \x1f- Inline search is also supported.'
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        '⬇️ The commands and there use is explained here ⬇️\x1f- `/play` To search the song on Youtube and play the first matching result.\x1f- `/song` To download a song from youtube.\x1f- `/play` Reply this in response to a link or any telegram audio file it will be played \x1f- `/skip` to skip current song \x1f- `/end` to stop the streaming of song \x1f- `/pause` to pause the stream \x1f- `/resume` to resume the playback. \x1f- Inline search is also supported.'
    )
