import azure.functions as func

bp = func.Blueprint()

@bp.route(route='healtcheck', auth_level=func.AuthLevel.ANONYMOUS)
def healthcheck(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("OK", status_code=200)