import requests

class ModelManager:
    def  __init__(self, secret_key, base_url):
        self.base_url = base_url
        self.project_data = {}
        self.secret_key = secret_key
    
    def _get_headers(self, **kwargs):
        '''Returns headers for request
        '''
        headers = {'Authorization': 'secret-key {0}'.format(self.secret_key)}

        return headers


class Usecase(ModelManager):
  
    def post_usecase(self, usecase_data):
        '''Post Usecase
        '''
        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/" % self.base_url
        image_p = usecase_data['image']
        banner_p = usecase_data['banner']
        
        #for usecase_data
        data = {
            "name": usecase_data['name'],
            "author": usecase_data['author'],
            "description": usecase_data['description'],
            "source": usecase_data['source'],
            "contributor": usecase_data['contributor'],  
        }

        #for images
        files={
             "image":open(image_p, 'rb'),
             "banner":open(banner_p, 'rb')
        }
    
        r = requests.post(url,
                    data=data, files=files, headers=kwargs['headers'])

        if r.status_code == 201:
            print("Post usecase succeed with status code %s" % r.status_code)
        else:
            print("Post usecase failed with status code %s" % r.status_code)
            
        return self

    def patch_usecase(self, usecase_data, usecase_id):
        '''Update Usecase
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)
        image_p = usecase_data['image']
        banner_p = usecase_data['banner']
        
        #for usecase_data
        data = {
            # "name": usecase_data['name'],
            "author": usecase_data['author'],
            "description": usecase_data['description'],
            "source": usecase_data['source'],
            "contributor": usecase_data['contributor'],  
        }

        #for images
        files={
             "image":open(image_p, 'rb'),
             "banner":open(banner_p, 'rb')
        }
        r = requests.patch(url,
                    data=data, files=files, headers=kwargs['headers'])

        if r.status_code == 200:
            print("Update usecase succeed with status code %s" % r.status_code)
        else:
            print("Update usecase failed with status code %s" % r.status_code)
        return self

    def delete_usecase(self, usecase_id):
        '''Delete Usecase
        '''

        kwargs = {
            'headers': self._get_headers()
        }
       
        url = "%s/api/projects/%s/" % (self.base_url, usecase_id)
        
        r = requests.delete(url, headers=kwargs['headers'])

        if r.status_code == 204:
            print("Delete usecase succeed with status code %s" % r.status_code)
        else:
            print("Delete usecase failed with status code %s" % r.status_code)
            
        return self


class Model(ModelManager):

    def post_model(self, model_data):
        '''Post Model
        '''
        url = "%s/api/models/" % self.base_url

        kwargs = {
            'headers': self._get_headers()
        }

        #for model_data
        data = {
            "project": model_data['project'],
            "transformerType": model_data['transformerType'],
            "target_column": model_data['target_column'],
            "note": model_data['note'],
            "model_area": model_data['model_area'],
            "model_dependencies": model_data['model_dependencies'],
            "model_usage": model_data['model_usage'],
            "model_audjustment": model_data['model_audjustment'],
            "model_developer": model_data['model_developer'],
            "model_approver": model_data['model_approver'],
            "model_maintenance": model_data['model_maintenance'],
            "documentation_code": model_data['documentation_code'],
            "implementation_plateform": model_data['implementation_plateform'],
            "production": model_data['production'],
            "current_date": model_data['current_date'],
            "model_file_path" : model_data['model_file_path'],
            "scoring_file_path" : model_data['scoring_file_path'],
        }

        training_dataset = model_data['training_dataset']
        pred_dataset = model_data['pred_dataset']
        actual_dataset = model_data['actual_dataset']
        test_dataset = model_data['test_dataset']

        files={
                "training_dataset": open(training_dataset, 'rb'),
                "test_dataset": open(test_dataset, 'rb'),
                "pred_dataset": open(pred_dataset, 'rb'),
                "actual_dataset": open(actual_dataset, 'rb'),
                }

    
        model = requests.post(url,
                        data=data, files=files, headers=kwargs['headers'])
        

        if model.status_code == 201:
            print("Post model succeed with status code %s" % model.status_code)
        else:
            print("Post model failed with status code %s" % model.status_code)
        
        return self
    
    def delete_model(self, model_id):

        '''Delete Model
        '''

        kwargs = {
            'headers': self._get_headers()
        }
        
        url = "%s/api/models/%s/" % (self.base_url, model_id)
        
        model = requests.delete(url, headers=kwargs['headers'])

        if model.status_code == 204:
            print("Delete model succeed with status code %s" % model.status_code)
        else:
            print("Delete model failed with status code %s" % model.status_code)
            
        return self

    def patch_model(self, model_data, model_id):

        '''Update Model
        '''

        url = "%s/api/models/%s/" % (self.base_url, model_id)

        kwargs = {
            'headers': self._get_headers()
        }

        #for model_data
        data = {
            "transformerType": model_data['transformerType'],
            "target_column": model_data['target_column'],
            "note": model_data['note'],
            "model_area": model_data['model_area'],
            "model_dependencies": model_data['model_dependencies'],
            "model_usage": model_data['model_usage'],
            "model_audjustment": model_data['model_audjustment'],
            "model_developer": model_data['model_developer'],
            "model_approver": model_data['model_approver'],
            "model_maintenance": model_data['model_maintenance'],
            "documentation_code": model_data['documentation_code'],
            "implementation_plateform": model_data['implementation_plateform'],
            "production": model_data['production'],
            "current_date": model_data['current_date'],
            "model_file_path" : model_data['model_file_path'],
            "scoring_file_path" : model_data['scoring_file_path'],
        }

        training_dataset = model_data['training_dataset']
        pred_dataset = model_data['pred_dataset']
        actual_dataset = model_data['actual_dataset']
        test_dataset = model_data['test_dataset']

        files={
                "training_dataset": open(training_dataset, 'rb'),
                "test_dataset": open(test_dataset, 'rb'),
                "pred_dataset": open(pred_dataset, 'rb'),
                "actual_dataset": open(actual_dataset, 'rb'),
                }

    
        model = requests.patch(url,
                        data=data, files=files, headers=kwargs['headers'])

        if model.status_code == 200:
            print("Update model succeed with status code %s" % model.status_code)
        else:
            print("Update model failed with status code %s" % model.status_code)
        return self