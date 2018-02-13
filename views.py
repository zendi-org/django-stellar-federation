import importlib
import logging

from django.template import loader
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)


class NotImplementedException(Exception):
    pass


class NotFoundException(Exception):
    pass


@require_GET
def federation(request):
    # extract parameters
    query = request.GET['q']
    query_type = request.GET['type']

    # get callback
    mod_name, func_name = settings.STELLAR_FEDERATION_CALLBACK.rsplit('.', 1)
    mod = importlib.import_module(mod_name)
    callback = getattr(mod, func_name)

    try:
        # query account
        account = callback(query, query_type)
        return JsonResponse(account, status=200)
    except NotImplementedException:
        error_details = {'details': 'Query of type {} is not implemented.'.format(query_type)}
    except NotFoundException:
        error_details = {'details': 'Account was not found. (q={}, type={})'.format(query, query_type)}
    except Exception as e:
        error_details = {'details': str(e)}

    return JsonResponse(error_details, status=404)
