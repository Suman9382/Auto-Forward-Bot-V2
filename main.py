import asyncio
import os
from aiohttp import web
from pyrogram import idle
from bot import Bot

async def web_server():
    async def handle(request):
        return web.Response(text="Bot is Running")

    app = web.Application()
    app.add_routes([web.get('/', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 8080)))
    await site.start()

async def main():
    bot = Bot()
    await bot.start()
    await web_server()
    await idle()
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
