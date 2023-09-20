from pyrogram import Client
from pyrogram.enums import ChatType

from constants import emoji_alphabet


def add_emoji_alphabet(font_name, api_id, api_hash, session_name):
    with Client(session_name, api_id, api_hash) as client:
        dialogs = client.get_dialogs()
        stickers_chat_id = None
        for dialog in dialogs:
            chat = dialog.chat
            if chat.type == ChatType.BOT and chat.username == "Stickers":
                stickers_chat_id = chat.id
                break
        client.send_message(stickers_chat_id, "/start")
        client.send_message(stickers_chat_id, "/newemojipack")
        client.send_message(stickers_chat_id, "Статичные эмодзи")
        client.send_message(stickers_chat_id, font_name)
        for letter in emoji_alphabet.keys():
            client.send_document(stickers_chat_id, f"{font_name}/letter_{letter}.png")
            client.send_message(stickers_chat_id, emoji_alphabet[letter])
        client.send_message(stickers_chat_id, "/publish")
        client.send_message(stickers_chat_id, "/skip")
        client.send_message(stickers_chat_id, font_name)
