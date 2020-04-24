from hipo_drf_exceptions import handler
from hipo_drf_exceptions.exceptions import InternalServerError


def json_internal_server_error_middleware(get_response):

    def middleware(request):
        json_content_type = "application/json"
        response = get_response(request)

        if str(response.status_code).startswith("5") and request.content_type == json_content_type:
            response = handler(InternalServerError(), {})
        return response

    return middleware
