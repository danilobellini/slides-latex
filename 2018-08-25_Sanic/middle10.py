from datetime import datetime, timezone
from email.utils import formatdate
from sanic import response, Blueprint
bp = Blueprint(__name__)

@bp.middleware("request")
async def before_handling(request):
    request["start"] = datetime.now(tz=timezone.utc)

@bp.middleware("response")
async def after_handling(request, response):
    end = datetime.now(tz=timezone.utc)
    response.headers.update({
        "Duration": str(end - request["start"]),
        "Date": formatdate(end.timestamp()),
    })
