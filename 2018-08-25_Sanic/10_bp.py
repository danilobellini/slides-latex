from sanic import Sanic
import imc10, middle10

app = Sanic(__name__, configure_logging=False)
app.blueprint(imc10.bp)
app.blueprint(middle10.bp)
app.static("img", "sanic.png") # route, file/dir name
app.static("gotta_go_fast.png", "gotta_go_fast.png")
