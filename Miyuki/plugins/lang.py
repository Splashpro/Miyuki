###################################
####    From  Yukki Music Bot  ####
###################################

from lang import get_string
from Miyuki.mongo.language import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message
from Miyuki.utils.lang import *
from lang import get_command

LANG = get_command("LANG")

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="English🇬🇧", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="සිංහල🇱🇰", callback_data="languages_si"
            )
        ],
        [
            InlineKeyboardButton(
                text="हिन्दी🇮🇳", callback_data="languages_hi"
            ),
            InlineKeyboardButton(
                text="Italiano🇮🇹", callback_data="languages_it"
            )
        ],
        [
            InlineKeyboardButton(
                text="🧑‍💻 Developer",
                url=f"https://t.me/VenujaST",
            )
        ],
        [
            InlineKeyboardButton(
                text="Close ✖️", callback_data="close_data"
            ),
        ],
    ]
)


@app.on_message(filters.command(LANG))
@language
async def langs_command(client, message: Message, _):
    userid = message.from_user.id if message.from_user else None
    chat_type = message.chat.type
    user = message.from_user.mention
    lang = await get_lang(message.chat.id)
    if chat_type == "private":
      await message.reply_text( "Hello {}, I can speek many languages\n Select your language from bellow !".format(lang),
        reply_markup=keyboard,
     )
    elif chat_type in ["group", "supergroup"]:
        lang = await get_lang(message.chat.id)
        group_id = message.chat.id
        st = await app.get_chat_member(group_id, userid)
        if (
                st.status != "administrator"
                and st.status != "creator"
        ):
         return 
        try:   
            await message.reply_text( "Hello {}, I can speek many languages\n Select your language from bellow !".format(user),
        reply_markup=keyboard,
     )
        except Exception as e:
            return await app.send_message(LOG_GROUP_ID,text= f"{e}")


@app.on_callback_query(filters.regex("languages"))
async def language_markup(_, CallbackQuery):
    langauge = (CallbackQuery.data).split("_")[1]
    user = CallbackQuery.from_user.mention
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer("You're already on same language ")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer("Successfully changed your language.")
    except:
        return await CallbackQuery.answer(
            "Failed to change language or Language under update.")
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Close ✖️", callback_data="close_data"
            ),
        ],
    ]
)

    return await CallbackQuery.message.edit("🌎Language was changed Successfully \n.Changed by {}".format(user),
        reply_markup=keyboard,
        disable_web_page_preview=True,
    ) 

__MODULE__ = "Languages"
__HELP__ = """
Not every group speaks fluent english; some groups would rather have Miyuki respond in their own language.

This is where translations come in; you can change the language of most replies to be in the language of your choice!

**Available languages are:**
- हिन्दी🇮🇳
- English🇬🇧
- සිංහල🇱🇰

**Admin commands:**
- /lang : Set your preferred language.
"""
__helpbtns__ = (
    [
        [
            InlineKeyboardButton(
                text="English🇬🇧", callback_data="languages_en"
            ),
            InlineKeyboardButton(
                text="සිංහල🇱🇰", callback_data="languages_si"
            )
        ],
        [
            InlineKeyboardButton(
                text="हिन्दी🇮🇳", callback_data="languages_hi"
            ),
            InlineKeyboardButton(
                text="Italiano🇮🇹", callback_data="languages_it"
            )
        ],
        [
            InlineKeyboardButton(
                text="🧑‍💻 Developer",
                url=f"https://t.me/VenujaST",
            )
        ],
        [
            InlineKeyboardButton(
                text="Close ✖️", callback_data="close_data"
            ),
        ],
    ]
)