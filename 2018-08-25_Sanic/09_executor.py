import time
from sanic import response, Sanic
app = Sanic(__name__)

def slow_func(x):
    time.sleep(1)
    return x[::-1]

@app.route("/")
async def root(request):
    def slow_runner():
        return slow_func(request.args["input"][0])
    future = app.loop.run_in_executor(None, slow_runner)
    result = await future
    return response.json({"reversed": result})
