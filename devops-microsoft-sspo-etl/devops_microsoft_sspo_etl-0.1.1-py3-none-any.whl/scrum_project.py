
from tfs.tfs import TFS
from .abstract_command import Abstract_Command
from pprint import pprint

from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories

import logging
logging.basicConfig(level=logging.INFO)

class ScrumProject(Abstract_Command):
    
    def do(self,data):
        try:
            logging.info("Project")

            self.config(data)
            
            projects = self.tfs.get_projects()

            scrum_atomic_service = application_factories.ScrumAtomicProjectFactory()
            scrum_complex_service = application_factories.ScrumComplexProjectFactory()

            for tfs_project in projects:
                
                scrum_project = None
                scrum_project_service = None

                teams = self.tfs.get_teams(tfs_project.id)
                
                if (len(teams) > 1):
                    logging.info("Creating a Scrum Complex Project")
                    scrum_project = model_factories.ScrumComplexProjectFactory()
                    scrum_project_service = scrum_complex_service
                else:
                    logging.info("Creating a Scrum Atomic Project")
                    scrum_project = model_factories.ScrumAtomicProjectFactory()
                    scrum_project_service = scrum_atomic_service
                    
                #Persistindo a classe no banco
                scrum_project.name = tfs_project.name
                scrum_project.description = tfs_project.description
                scrum_project.organization = self.organization
                
                scrum_project_service.create(scrum_project)
                
                logging.info("Scrum Project Created")
                
                self.create_application_reference(
                    tfs_project.id, 
                    tfs_project.url,
                    self.PROJECT_TFS, 
                    scrum_project.uuid, 
                    scrum_project.type)
                    
                logging.info("Scrum Project's Application Reference Created")
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  
        