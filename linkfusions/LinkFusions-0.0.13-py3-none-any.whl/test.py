# import json
# import os
#
# import LinkFusions as lf
#
#
# # token = lf.LinkFusions.auth(
# #     email='admin@localhost.com', password='greatness2011',
# #     client_id='GPj7I9FxcybyHCEeZ50UQ84LMmjhTOU0MzlIIhjh',
# #     client_secret='RrAcveMhXdQC7rPMTqqzuLbe05zRtEVIM6HmV3U8DxlXTnJW3QPDQBZAymAh6TBmV9O1ie9U21xxrfhGVbBL5CuPQm5YaSxyImxcJIIBKOkAg28dlQZKWsnR2Mgb5MAb'
# # ).get('access_token')
#
# token = '6G7oZhqusCZCzCjdOcKRjyANcY8Ra5'
#
# fusion = lf.LinkFusions(token)
# # # fusion.Campaign.trigger(id=19, contacts=[1292], groups=[18])
# fusion.Campaign.create(name='Campaign Name', company='Company Name')