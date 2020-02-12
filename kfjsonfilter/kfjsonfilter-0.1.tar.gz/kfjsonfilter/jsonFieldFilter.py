from rest_framework import filters


class JsonFieldFilter(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    view. required params:
        json_field = '<data_json_field_name>'
        json_filters = [{'field': <field_name>, 'lookup': <lookup>}, ...]
        if lookup is a date_range, field value must contain <field_name>[]
        for a single date filter whe can specify any lookup
    """

    def filter_queryset(self, request, queryset, view):
        filters_json = {}
        try:
            if view.json_field:
                pass
        except Exception:
            raise NotImplementedError('You must define json_filed/s')
        try:
            if view.json_filters:
                if type(view.json_filters) != list:
                    raise NotImplementedError('You must define json_filters as list of dicts')
                for el in view.json_filters:
                    if type(el) != dict:
                        raise NotImplementedError('You must define json_filters as list of dicts')
                    if 'field' not in el or 'lookup' not in el:
                        raise NotImplementedError('Each dict must contain field an lookup element')
        except Exception:
            raise NotImplementedError('You must define json_filters')

        for param in request.query_params:
            for el_filter in view.json_filters:
                if param == el_filter.get('field'):
                    if el_filter.get('lookup') == 'date_range':
                        clean_param = param.replace('[]', '')
                        json_field = '{}__{}__{}'.format(view.json_field, clean_param, 'lte')
                        filters_json[json_field] = request.query_params.getlist(param)[1]
                        json_field = '{}__{}__{}'.format(view.json_field, clean_param, 'gte')
                        filters_json[json_field] = request.query_params.getlist(param)[0]
                    else:
                        json_field = '{}__{}__{}'.format(view.json_field, param, el_filter.get('lookup'))
                        filters_json[json_field] = request.query_params.get(param)
        return queryset.filter(**filters_json)


