import time
from sanic import response, Sanic
app = Sanic(__name__)

def slow_func(x):
    time.sleep(1)
    return x[::-1]

@app.route("/")
async def root(request):
    result = slow_func(request.args["input"][0])
    return response.json({"reversed": result})
