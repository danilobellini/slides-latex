import asyncio
from sanic import response, Sanic
app = Sanic(__name__)

async def slow_func(x):
    await asyncio.sleep(1)
    return x[::-1]

@app.route("/")
async def root(request):
    result = await slow_func(request.args["input"][0])
    return response.json({"reversed": result})
