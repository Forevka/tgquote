import asyncio
from io import BytesIO

from aiogram import Bot
from aiogram.types import Message, User

from tgquote import TelegramImageRenderer
from tgquote.filegetters import DefaultFileGetter
from tgquote.renderers import PyppeteerRenderer
from tgquote.debug.server import app
from aiohttp import web

bot = Bot(token="666922879:AAEWkOwKYH-Sz7pBm9fLtXDlDV1fSGiNbwo")
render_engine = PyppeteerRenderer()
quoter = TelegramImageRenderer(
    renderer=render_engine,
    filegetter=DefaultFileGetter(bot),
)


async def main():
    '''
    Bot.set_current(bot)
    img: BytesIO = await quoter.render(
        Message(
            from_user=User(
                first_name="qqqqq",
                id=1,
            ),
            text="",
        )
    )
    with open("1.png", "wb") as f:
        f.write(img.read())
    '''



if __name__ == "__main__":
    web.run_app(app)
    #asyncio.run(main())
