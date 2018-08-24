import os
from asyncpgsa import pg
from sanic import  response, Sanic
app = Sanic(__name__)

@app.listener("before_server_start")
async def setup_db(app, loop):
    await pg.init(os.environ["PGSQL_URL"])

@app.route("/")
async def tstamper(request):
    ip = request.remote_addr or request.ip
    query = "SELECT timezone('UTC', CURRENT_TIMESTAMP)"
    now = await pg.fetchval(query)
    return response.json({
        str(ip): now.isoformat(timespec="microseconds")
    })
