from .base_entity import BaseEntity
import logging
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories

logging.basicConfig(level=logging.INFO)

class ProductBacklog(BaseEntity):

    def do(self,data):
        try:
            self.config(data)

            application_atomic_user_story = application_factories.AtomicUserStoryFactory()
            application_epic = application_factories.EpicFactory()

            logging.info("Product Backlog")
            work_itens = self.tfs.get_work_item_query_by_wiql_epic_user_story_product_backlog_item()
            for work_item in work_itens:
                element = self.tfs.get_work_item(work_item.id, None,None, "All")

                logging.info("Product Backlog: element ID: "+str(work_item.id))
                logging.info("Product Backlog: element Type: "+element.fields['System.WorkItemType'])

                
                if (element.fields['System.WorkItemType'] == "User Story" or element.fields['System.WorkItemType'] =="Product Backlog Item"):
                    
                    logging.info("User Story")
                    relations = element.relations
                    if relations:
                        for relation in relations:
                            if relation.attributes["name"] == "Parent":
                                url = relation.url
                                logging.info("Searching User Story: "+str(element.id))
                                atomic_user_story = application_atomic_user_story.retrive_by_external_uuid(element.id)
                            
                                logging.info("Searching Epic: "+str(url))
                                epic_parent = application_epic.retrive_by_external_url(url)
                                
                                if epic_parent:
                            
                                    logging.info("Assignig Epic in Atomic User Story")
                                    atomic_user_story.epic = epic_parent.id
                                        
                                    logging.info("Updating")
                                    application_atomic_user_story.update (atomic_user_story)
                                    logging.info("Atomic User Story updated: "+str(element.id) + " | "+ str(element.fields["System.Parent"]))
                                else:
                                    logging.error("It is not a EPIC")
                                    
                    else:
                        logging.info("No parent to User Story: "+str(element.id))
                    
                elif element.fields['System.WorkItemType'] == "Epic":
                    relations = element.relations
                    if relations:
                        for relation in relations:
                            if relation.attributes["name"] == "Parent":
                                url = relation.url    
                                logging.info("Add Epic in Epic")
                                logging.info("Searching Epic: "+str(element.id))
                                epic = application_epic.retrive_by_external_uuid(element.id)
                                    
                                logging.info("Searching Epic Parent: "+str(url))
                                    
                                epic_parent = application_epic.retrive_by_external_url(url)
                                if epic_parent:
                                    epic.epic = epic_parent.id
                                    application_epic.update(epic)
                                    logging.info("Updating")
                                    logging.info("Epic updated: "+str(element.id))
                                else:
                                    logging.error("It is not a EPIC")
                    else: 
                        logging.info("No parent to Epic: "+str(element.id))
        
            logging.info("Fim")      
        except Exception as e:
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)