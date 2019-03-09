from sanic import Sanic, response

app = Sanic(__name__)
app.static("/video", "sanic.mp4", stream_large_files=True)
app.static("/video_not_chunked", "sanic.mp4") # Should not be used!

@app.route("/")
def root(request):
    return response.html("""<html><body><video controls>
        <source src="/video"><a href="/video">Video</a>
    </video></body></html>""")
