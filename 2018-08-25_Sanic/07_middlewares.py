from datetime import datetime, timezone
from email.utils import formatdate

from sanic import exceptions, response, Sanic
app = Sanic(__name__)

@app.middleware("request")
async def before_handling(request):
    request["start"] = datetime.now(tz=timezone.utc)
    if request.headers.get("Authorization", "") != "TEST":
        exceptions.abort(401)

@app.middleware("response")
async def after_handling(request, response):
    end = datetime.now(tz=timezone.utc)
    response.headers.update({
        "Duration": str(end - request["start"]),
        "Path": request.path,
        "Date": formatdate(end.timestamp()),
    })

@app.route("/")
@app.route("/another/path")
async def root(request):
    return response.json({"status": "authorized"})
