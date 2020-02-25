from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.forms.forms import ValidationError

from gfk_models.gfk_base.views import GFKCreateView
from .forms import ReviewForm
from .models import Review
from gfk_models.gfk_helpers.functions.common import CommonHelpers


class ReviewCreateView(GFKCreateView):
    @method_decorator(csrf_exempt)
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReviewCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # print('populate_target')
        # self.populate_self(request, *args, **kwargs)

        author = CommonHelpers.get_user__by_request(request)
        tmp_post = request.POST.copy()

        if str(author) != "AnonymousUser":
            tmp_post.update({'author': author.id})
        else:
            tmp_post.update({'author': None})

        request.POST = tmp_post

        try:
            self.target.reviews_manager().add(request.POST.dict())
            return JsonResponse({
                'success': True,
            })

        except ValidationError as ex:
            form = ex.args[1]
            print(form.errors)

            return JsonResponse({
                'success' : False,
                'errors' : [(k, v[0]) for k, v in form.errors.items()],
            })



# @login_required
# def add(request):
#     data_dict = request.POST.copy()
#
#     target_type = ContentType.objects.get(app_label=data_dict['target_app_label'], model=data_dict['target_model'])
#     target = target_type.model_class().objects.get(id=data_dict['target_id'])
#
#     # data_dict['target_id'] = target.id
#     # data_dict['target_content_type'] = target_type.id
#     author = CommonHelpers.get_user__by_request(request)
#     data_dict['author'] = author.id
#
#     review_list = ReviewList.objects.get(_target=target)
#     data_dict['review_list'] = review_list
#
#     try:
#         review = Review.objects.get(review_list=review_list, author=author)
#         update = True
#     except Exception as ex:
#         print(ex)
#         update = False
#         review = Review()
#
#     form = ReviewForm(data_dict, instance=review)
#
#     if form.is_valid():
#         form.save()
#         if update:
#             return JsonResponse({
#                 'success': True,
#                 'create': False
#             })
#         else:
#             return JsonResponse({
#                 'success': True,
#                 'create': True
#             })
#     else:
#         print(form.errors)
#
#     return JsonResponse({
#         'success' : False,
#         'errors' : [(k, v[0]) for k, v in form.errors.items()],
#     })


