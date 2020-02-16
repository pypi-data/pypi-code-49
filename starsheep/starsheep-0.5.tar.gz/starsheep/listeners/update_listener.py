# import dinemic
#
#
# class Listener(object, dinemic.DAction):
#     listener_name = None
#     _fields = None
#     _lists = None
#     _dicts = None
#
#     def __init__(self, listener_name, document):
#         if 'on' not in document:
#             raise Exception('Missing "on" in listener ' + listener_name)
#         if 'action' not in document:
#             raise Exception('Missing "action" in listener ' + listener_name)
#         if document['action'] == 'script' and 'script_name' not in document:
#             raise Exception('Missing "script_name" in listener ' + listener_name + ' or wrong listener type')
#         if document['action'] == 'update' and 'update' not in document:
#             raise Exception('Missing "update" in listener ' + listener_name)
#
#     @staticmethod
#     def get_owned(model_name):
#         pass
