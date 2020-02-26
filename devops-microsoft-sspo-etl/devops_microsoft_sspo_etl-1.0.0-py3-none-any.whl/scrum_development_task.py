from .user_story_abastract import UserStoryAbstract

from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
from pprint import pprint
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class ScrumDevelopmentTask(UserStoryAbstract):

    def do(self,data):
        try:
            logging.info("Task")
            self.config(data)
            
            self.application_scrum_intented_development_task = application_factories.ScrumIntentedDevelopmentTaskFactory()
            self.application_sprint_backlog = application_factories.SprintBacklogFactory()

            # Buscando os projetos do TFS
            work_itens = self.tfs.get_work_item_query_by_wiql_task()

            logging.info("Buscando Task")
            for work_item in work_itens:
                element = self.tfs.get_work_item(work_item.id, None,None, "All")
                
                if element.fields['System.WorkItemType'] == "Task":   
                    state = str(self.check_value(element,'System.State'))
                    
                    if state == "New" or state =="To Do":
                        self.__create_intended_task(element)
                    else:
                        self.__create_performed_task(element)
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)    

    def __create_scrum_development_task(self, element, scrum_development_task):
        try:
            application_sprint = application_factories.SprintFactory()
            application_atomic_user_story = application_factories.AtomicUserStoryFactory()
            
            self.set_name_description(element, scrum_development_task)
            logging.info('Scrum development Task: Name and Description: '+scrum_development_task.name)
            
            project_name = self.retrive_project_name(element)

            logging.info('Scrum development: Project Name: '+str(project_name))
            logging.info('Scrum development: Sprint')

            project_name = project_name.strip()

            sprint_name = self.check_value(element,"System.IterationLevel2") 
            
            logging.info('Scrum development: Sprint: '+str(sprint_name))

            if sprint_name is None:
                sprint_name = "limbo"
                logging.warning("LIMBO")
            else:
                sprint_name = sprint_name.strip()

            logging.info('Scrum development: Sprint Backlog')
            sprint_backlog = self.application_sprint_backlog.retrive_by_name_and_project_name(sprint_name,project_name)
            
            if sprint_backlog is not None:
                scrum_development_task.sprint_backlogs = [sprint_backlog]
            else:
                logging.error('Scrum development: Sprint Backlog: None')
            
            logging.info('Scrum development: retrive Sprint')
            sprints = application_sprint.retrive_by_name_and_project_name(sprint_name,project_name)
            if sprints is not None:
                scrum_development_task.sprints = [sprints]
            else:
                logging.error('Scrum development: retrive Sprint: NONE')
            
            relations = element.relations
            if relations is not None and relations is not 'None':
                for relation in relations:
                    relation_name = relation.attributes["name"] 
                    url = relation.url
                    
                    if relation_name == "Parent":
                        logging.info('Scrum development: Atomic User Story')
                        logging.info('Scrum development: Atomic User Story: '+ url)
                        atomic_user_story = application_atomic_user_story.retrive_by_external_url(url)
                        
                        if atomic_user_story:
                            scrum_development_task.atomic_user_story = atomic_user_story.id
                    
            logging.info('Scrum development: Created')
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)   
        

    def __create_intended_task(self, element):
        try:
            logging.info('Intented Task: Creating Intended Task')
            
            application_development_task_type = application_factories.DevelopmentTaskTypeFactory()
            application_priority = application_factories.PriorityFactory()
            
            scrum_intented_development_task = model_factories.ScrumIntentedDevelopmentTaskFactory()
            logging.info('Intented Task: Calling scrum development task function')
            self.__create_scrum_development_task(element, scrum_intented_development_task)
            
            logging.info('Intented Task: Dates')
            created_data = self.check_value(element,'System.CreatedDate')
            if created_data is not None and created_data is not 'None':
                scrum_intented_development_task.created_date = self.validate_date_format(str(created_data)) 
            
            project_name = self.retrive_project_name(element)
            product_backlog = self.retrive_product_backlog(project_name)

            # Product Backlog 
            logging.info('Intented Task: Product Backlog')
            if product_backlog is not None:
                scrum_intented_development_task.product_backlog = product_backlog.id
            else:
                logging.error('Intented Task: Product Backlog: None')
            
            logging.info('Intented Task: Retrive team member')
            self.retrive_team_members(element, scrum_intented_development_task)
            
            story_points = self.check_value(element,'Microsoft.VSTS.Scheduling.StoryPoints')
            logging.info('Intented Task: Story Point: '+str(story_points))

            if story_points is not None: 
                scrum_intented_development_task.story_points  = story_points

            activity  = self.check_value(element,'Microsoft.VSTS.Common.Activity')
            logging.info('Intented Task: Activity: '+str(activity))

            if activity is not None and activity is not 'None':
                logging.info('Intented Task: Type Activity')
                type_activity = application_development_task_type.retrive_by_name(activity.lower())
                scrum_intented_development_task.type_activity = type_activity.id
            
            priority = self.check_value(element,'Microsoft.VSTS.Common.Priority')
            
            logging.info('Intented Task: Priority: '+str(priority))
            if priority is not None and priority is not 'None':    
                Priority = model_factories.PriorityFactory()
                level = None
                if priority == 1:
                    level = Priority.normal
                elif priority == 2 or priority == 3:
                    level = Priority.medium
                else:
                    level = Priority.high
                
                logging.info('Intented Task: searching priority')
                priority = application_priority.retrive_by_name(level)
                scrum_intented_development_task.priority = priority.id
            
            logging.info('Persisting intented task')
            self.application_scrum_intented_development_task.create(scrum_intented_development_task)
            logging.info('Intented Task persited')
            
            return scrum_intented_development_task
    
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  
        
        
    def __create_performed_task(self, element):

        try:
        
            logging.info('Performed Task: Creating Performed Task')
            
            application_sprint = application_factories.SprintBacklog()

            application_atomic_user_story = application_factories.AtomicUserStoryFactory()

            #criando a intented development task
            scrum_intented_development_task = self.__create_intended_task(element)
            logging.info('Performed Task:Intented Task created')

            application_performed_development_task = application_factories.ScrumPerformedDevelopmentTaskFactory()
            
            scrum_peformed_development_task = model_factories.ScrumPerformedDevelopmentTaskFactory()
            
            logging.info('Performed Task:Performed Task assigned with Intented')
            scrum_peformed_development_task.caused_by = scrum_intented_development_task.id

            self.__create_scrum_development_task(element, scrum_peformed_development_task)
            
            logging.info("Performed Task: Team Member")
            self.retrive_team_members(element, scrum_peformed_development_task)

            #create peformed
            logging.info('Performed Task:Persiting performed task')
            application_performed_development_task.create(scrum_peformed_development_task)

        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)   

    