from sanic import Blueprint, exceptions, response
bp = Blueprint(__name__)

@bp.exception(Exception)
def handle_error(request, exception):
    status = getattr(exception, "status_code", 500)
    reason = exceptions.STATUS_CODES.get(exception.status_code,
                                         b"unknown_error")
    snake_reason = b"_".join(reason.lower().split())
    return response.json({"error": snake_reason}, status=status)
