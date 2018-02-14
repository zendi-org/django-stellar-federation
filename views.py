import importlib
import logging

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from stellar_federation import NotImplementedException, NotFoundException

logger = logging.getLogger(__name__)


@require_GET
def federation(request):
    # extract parameters
    query = request.GET['q']
    query_type = request.GET['type']

    logger.info('Performing query (q={}, type={})'.format(query, query_type))

    # get callback
    mod_name, func_name = settings.STELLAR_FEDERATION_CALLBACK.rsplit('.', 1)
    mod = importlib.import_module(mod_name)
    callback = getattr(mod, func_name)

    try:
        # query account
        account = callback(request, query, query_type)
        return JsonResponse(account, status=200)
    except NotImplementedException:
        error_details = {'details': 'Query of type {} is not implemented.'.format(query_type)}
    except NotFoundException as ex:
        error_details = {'details': ex.details}
    except Exception as e:
        error_details = {'details': str(e)}

    return JsonResponse(error_details, status=404)
