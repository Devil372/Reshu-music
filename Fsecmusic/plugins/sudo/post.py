from pyrogram import Client, filters
from Fsecmusic import app
from config import OWNER_ID, BOT_USERNAME
from pyrogram.types import Message


@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(OWNER_ID "5460343986"))
async def copy_messages(_, message):

    if message.reply_to_message:
      
        destination_group_id = --1001685012914
 

        
        await message.reply_to_message.copy(destination_group_id)
        await message.reply("ᴘᴏsᴛ sᴜᴄᴄᴇssғᴜʟ ᴅᴏɴᴇ ")
