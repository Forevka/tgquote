import aiohttp
from aiohttp import web
from jinja2 import Environment, FileSystemLoader
import json

from .filegetter import DebufFileGetter
from .. import messagesToHtml
from ..utils import templates_list, js

from pathlib import Path

selfdir = Path(__file__).parent
module = selfdir.parent

loader = FileSystemLoader(module / "templates")
env = Environment(loader=loader, enable_async=True, cache_size=0)

filegetter = DebufFileGetter()

app = web.Application()
routes = web.RouteTableDef()


@routes.get("/")
async def debug(req: web.Request):
    messages = []
    with open(selfdir / "messages.json", encoding="utf-8") as f:
        messages = json.loads(f.read())
    css = open(module / "css/light.css").read()
    css += "body {background-color: grey}"

    rendered = await messagesToHtml(
        messages, env, files=filegetter, templates=templates_list
    )
    html = (
        f"""
  <!!DOCTYPE html>
  <html>
    <head>
      <title>TelegramImage debug</title>
    </head>
    <body>
      <style>
      {css}
      </style>
      {rendered}
    </body>
  </html>
  """
    )
    return web.Response(body=html, content_type="text/html")


app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(debug.app)
