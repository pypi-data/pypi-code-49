from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

from gfk_models.gfk_base.models import GFKModel
from gfk_models.gfk_base.views import GFKCreateView
from gfk_models.gfk_helpers.functions.common import CommonHelpers


class LikeCreateView(GFKCreateView):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        kwargs['target_model'] = GFKModel.get_ct_model_static(kwargs['target_ct'])
        kwargs['target_request_attr'] = 'target_id'
        kwargs['target_retrieve_attr'] = 'id'

        return super(LikeCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        author = CommonHelpers.get_user__by_request(request)

        if request.POST.get('v') == 'like':
            response = self.target.like(author)

        elif request.POST.get('v') == 'dislike':
            response = self.target.dislike(author)

        return JsonResponse({
            'likes': {
                'count': response.count,
                'sum': response.sum,
            }
        })
