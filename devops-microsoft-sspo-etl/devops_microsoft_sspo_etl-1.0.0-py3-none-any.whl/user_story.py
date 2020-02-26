from .user_story_abastract import UserStoryAbstract
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import logging
logging.basicConfig(level=logging.INFO)
import re  

class UserStory(UserStoryAbstract):

    def do(self,data):
        try:
            self.application_epic = application_factories.EpicFactory()
            self.application_atomic_user_story = application_factories.AtomicUserStoryFactory()
            
            self.config(data)
            logging.info("User Story")
            logging.info("User Story: Retrive information from TFS")
            work_itens = self.tfs.get_work_item_query_by_wiql_epic_user_story_product_backlog_item()

            for work_item in work_itens:

                element = self.tfs.get_work_item(work_item.id, None,None, "All")

                if element.fields['System.WorkItemType'] == "User Story" or element.fields['System.WorkItemType'] =="Product Backlog Item":
                    logging.info("User Story: Create User Story")
                    self.__create_atomic_user_story(element)    
               
                elif element.fields['System.WorkItemType'] == "Epic":
                    logging.info("User Story: Epic")
                    self.__create_epic(element)
                    
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)              
    
    def __create_user_story(self, element,seon_element,seon_type_element, application_service):
        try:
            logging.info("User Story: add name and description")
            self.set_name_description(element, seon_element)
            
            logging.info("User Story: add dates")
            #recuperando as datas    
            self.retrive_dates(element, seon_element)

            story_points = self.check_value(element,'Microsoft.VSTS.Scheduling.StoryPoints')
            logging.info('User Story: Story Point: '+str(story_points))

            if story_points is not None: 
                seon_element.story_points  = story_points

            logging.info("User Story: project name")
            #Adicionando o EPIC o backlog
            project_name = self.retrive_project_name(element)
            
            logging.info("User Story: retrive Product Backlog: "+project_name)
            product_backlog = self.retrive_product_backlog(project_name)

            # Product Backlog 
            logging.info("User Story: add Product Backlog :"+str(product_backlog.id))
            
            seon_element.product_backlog = product_backlog.id

            logging.info("User Story: Retrive Team Members")
            self.retrive_team_members(element, seon_element)

            logging.info("User Story: create Seon Element")
            application_service.create (seon_element)
            
            logging.info("User Story: Create reference")
            
            #application reference
            application_reference = model_factories.ApplicationReferenceFactory(
                                                    name = seon_element.name,
                                                    description = seon_element.description,
                                                    application = self.application.id,
                                                    external_id = element.id,
                                                    external_url = element.url,
                                                    external_type_entity = self.WORK_ITEM,
                                                    internal_uuid = seon_element.uuid,
                                                    entity_name = seon_element.__tablename__
                                                )

            self.application_application_reference.create(application_reference)
                                        
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)              
        
        
    def __create_atomic_user_story(self, element):
        
        logging.info("User Story: Create Atomic User Story")
        
        atomic_user_story = model_factories.AtomicUserStoryFactory()

        self.__create_user_story(element,atomic_user_story, "atomic_user_story", self.application_atomic_user_story)

    def __create_epic (self, element):
        
        logging.info("User Story: Create Epics")
        
        epic = model_factories.EpicFactory()

        self.__create_user_story(element, epic, "epic", self.application_epic)
        