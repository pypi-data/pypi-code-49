import requests
import json
from pprint import pprint

class Task():
    def __init__(self,name, projectId):
        self.name = name
        self.projectId = projectId

class User():
    
    def __init__ (self, id = None):
        self.id = id

    def __str__(self):
        return self.id

class Clockify():

    def __init__(self,api_key):
        self.base_url = 'https://api.clockify.me/api/' 
        self.api_key = api_key
        self.header =  {'X-Api-Key': self.api_key }

    def get_all_workspaces(self):
        url = self.base_url+'workspaces/'
        return self.__request_get(url)
    
    def get_user (self, id):
        url = self.base_url + 'users/'+str(id)
        r = self.__request_get(url)
        return r.json()

    def get_all_projects (self, workspace_id):
        
        url = self.base_url+'workspaces/'+workspace_id+'/projects/'
        r = self.__request_get(url)
        return r.json()

    def get_all_workspace_users(self, workspace_id):
        url = self.base_url+'workspaces/'+workspace_id+'/users/'
        return self.__request_get(url)
    
    def get_all_time_entry_user(self,workspace_id, user_id):
        url = self.base_url+'v1/workspaces/'+workspace_id+'/user/'+user_id+'/time-entries'
        r = self.__request_get(url)
        time_entries = []
        time_entries.append(r.json())
        hasTimeEntry = True
        page = 1
        
        while (hasTimeEntry):
            urlx = url + "/?page="+str(page)
            r = self.__request_get(urlx)
            if r.status_code == 200:
                if len(r.json()) > 0:
                    time_entries.append(r.json())
                    page = page + 1
                elif len(r.json()) < 50 or len(r.json()) == 0:
                    hasTimeEntry = False
                    page = 1
             
        time_x = []
        for time_entry in time_entries:
            for TE in time_entry:
                time_x.append (TE)
        return time_x
        
    def add_new_task(self, workspace_id, project_id, task_name, assigneeId = None):
        
        url = self.base_url+'workspaces/'+workspace_id+'/projects/'+project_id+'/tasks/'
        
        task = None

        if (assigneeId == None):
            task =  {'name': task_name, 'projectId': project_id }   
        else:
            task =  {'name': task_name, 'projectId': project_id, 'assigneeId': assigneeId}   
    
        return self.__request_post(url, task)
    
    def __get_task(self, url):
        all_tasks = []
        has = True
        page = 0
        urlx = url
        while (has):
            pprint (urlx)
            r = self.__request_get(urlx)
            if r.status_code == 200:
                pprint ("ok")
                tasks = r.json()
                pprint (len(tasks))
                if (len(tasks) > 0):
                    for task in tasks:
                        all_tasks.append(task)
                        pprint (task['id'])
                    page = page + 1  
                
                if (len(tasks) < 50):
                    has = False
            else:
                has = False
            urlx = url + "/?page="+str(page)
        return all_tasks

    def get_task_done(self, workspace_id, project_id):
        url = self.base_url+'workspaces/'+workspace_id+'/projects/'+project_id+'/tasks/'
        return self.__get_task(url)

    def get_task_active (self, workspace_id, project_id):
        url = self.base_url+'workspaces/'+workspace_id+'/projects/'+project_id+'/tasks/?is-active=True'
        return self.__get_task(url)
        
        
    def create_new_project(self, workspace_id, project_name):
        url = self.base_url+'workspaces/'+workspace_id+'/projects/'
        data = {
                'name': project_name,
                "clientId": "",
                "isPublic": "false",
                "estimate": {
                    "estimate": "3600",
                    "type": "AUTO" 
                    },
                "color": "#f44336",
                "billable": "false"
            }

        return self.__request_post(url, data)

    def create_new_workspace(self, name):
        
        url = self.base_url+'workspaces/'
        data = {'name': name}
        return self.__request_post(url, data)
    
    def add_new_user(self,workspace_id, email):
        url = self.base_url+'workspaces/'+workspace_id+'/users'
        emails = []
        emails.append(email)
        data = {'emails': emails}
        return self.__request_post(url, data)

    def __request_get(self,url):
        return requests.get(url, headers=self.header)
    
    def __request_post(self,url,payload):
        return requests.post(url, headers=self.header,json=payload)
