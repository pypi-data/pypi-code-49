from django.views.generic import list, detail
from django.views import generic
from django.contrib.contenttypes.models import ContentType
from helpers.functions.common import CommonHelpers

class GFKBaseViewMixin(object):
    target_model = None
    target_request_attr = None
    target_retrieve_attr = None

    def get_target_from_dict(self, dict):
        # print(dict)
        if 'target_id' in dict and dict['target_id'] != "" \
            and 'target_content_type' in dict and dict['target_content_type'] != "":
            self.target = CommonHelpers.get_target(dict['target_content_type'], dict['target_id'])
            return True
        return False

    def get_target(self):
        '''
        If

        target_model
        target_request_attr
        target_retrieve_attr

        we looking for them in kwargs

        because we can attache views in such way:

        url(r'^foo/(?P<foo_slug>[\w\-]+)/qna/(?P<bar_id>[\d]+)-(?P<bar_slug>[\w\-]+)/',
                include('bar.urls'),
                {
                    'target_model': models.Question
                    'target_request_attr': 'foo_slug'
                    'target_retrieve_attr':'slug'
                }
            ),

        :return: Target connected thru GenericForeignKey
        '''
        try:
            target_model = self.get__kwargs['target_model']
        except:
            target_model = self.target_model

        try:
            target_request_attr = self.get__kwargs['target_request_attr']
        except:
            target_request_attr = self.target_request_attr

        try:
            target_retrieve_attr = self.get__kwargs['target_retrieve_attr']
        except:
            target_retrieve_attr = self.target_retrieve_attr

        try:
            kwargs = {}
            kwargs[target_retrieve_attr] = self.get__kwargs[target_request_attr]

            self.target = target_model.objects.get(*[], **kwargs)

            return self.target
        except:
            return None

    def dispatch(self, request, *args, **kwargs):
        self.populate_self(request, *args, **kwargs)
        return super(GFKBaseViewMixin, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        '''

        self.get__kwargs - должен быть добавлен в дочернем классе
                * target_content_type
                * target_id

        :return:
        '''
        queryset = self.model.objects.all()

        if hasattr(self, 'target'):
            queryset = queryset.filter(_target=self.target)

        self.queryset = queryset

        return super(GFKBaseViewMixin, self).get_queryset()

    def populate_context(self, **kwargs):
        if hasattr(self, 'target'):
            kwargs['target'] = self.target

        if hasattr(self, 'parent_urls_namespace'):
            kwargs['parent_urls_namespace'] = self.parent_urls_namespace

        return kwargs

    def get_context_data(self, **kwargs):
        kwargs = self.populate_context(**kwargs)
        return super(GFKBaseViewMixin, self).get_context_data(**kwargs)

    def populate_self(self, request, *args, **kwargs):
        self.get__kwargs = kwargs
        self.get__args = args

        if not hasattr(self, 'target'):
            self.get_target_from_dict(request.GET)

        if not hasattr(self, 'target'):
            self.get_target_from_dict(request.POST)

        if not hasattr(self, 'target'):
            self.get_target()

        if 'parent_urls_namespace' in kwargs:
            self.parent_urls_namespace = kwargs['parent_urls_namespace']

        if hasattr(self, 'target'):
            kwargs['target'] = self.target
            kwargs['target_id'] = self.target.id
            kwargs['target_content_type'] = ContentType.objects.get_for_model(self.target).id

        post_dict = request.POST.copy()
        post_dict.update(kwargs)
        request.POST = post_dict


class GFKListView(GFKBaseViewMixin, list.ListView):
    pass


class GFKDetailView(GFKBaseViewMixin, detail.DetailView):
    pass


class GFKCreateView(GFKBaseViewMixin, generic.CreateView):
    pass


class GFKUpdateView(GFKBaseViewMixin, generic.CreateView):
    pass



