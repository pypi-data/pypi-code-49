from .base_entity import BaseEntity
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import logging
logging.basicConfig(level=logging.INFO)

class ScrumProjectTeam(BaseEntity):
    
    def do(self, data):
        try:
            self.config(data)
        
            logging.info("Project Team")
            
            projects = self.tfs.get_projects()

            self.application_complex_scrum_project = application_factories.ScrumComplexProjectFactory()
            self.application_atomic_scrum_project = application_factories.ScrumAtomicProjectFactory()
            self.application_scrum_process = application_factories.ScrumProcessFactory()
            self.application_product_backlog_definition = application_factories.ProductBacklogDefinitionFactory()
            self.application_product_backlog = application_factories.ProductBacklogFactory()

            for project in projects:
                
                logging.info("Getting Project Teams from: "+project.name)
                teams = self.tfs.get_teams(project.id)
                scrum_project = None
                
                for team in teams:
                    scrum_project = self.application_atomic_scrum_project.retrive_by_external_uuid(project.id)

                    if scrum_project is not None:
                        self.create_scrum_process(team, scrum_project)
                    else:
                        scrum_project = self.application_complex_scrum_project.retrive_by_external_uuid(project.id)
                        logging.info("Creating a scrum atomic project, scrum process and scrum team")   

                        scrum_atomic_project = self.create_scrum_atomic_project(team, scrum_project)
                        self.create_scrum_process(team, scrum_atomic_project)
        
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  

                    
    def create_scrum_atomic_project(self, team, complex_project):
        try:
            scrum_atomic_project = model_factories.ScrumAtomicProjectFactory(
                                name=team.name,
                                description = team.description,
                                organization =  self.organization,
                                scrum_complex_project_id =complex_project.id)
            
            if complex_project is not None:
                scrum_atomic_project.root = False
                        
            application_scrum_atomic_project = application_factories.ScrumAtomicProjectFactory()
            application_scrum_atomic_project.create(scrum_atomic_project)

            application_reference = model_factories.ApplicationReferenceFactory(
                            name = team.name,
                            description = team.description,
                            application = self.application.id,
                            external_id = team.id,
                            external_url = team.url,
                            external_type_entity = self.TEAM_TFS,
                            internal_uuid = scrum_atomic_project.uuid,
                            entity_name = scrum_atomic_project.type
                        )

            self.application_application_reference.create(application_reference)
            return scrum_atomic_project
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  
    
    def create_scrum_process (self, team, scrum_project):
        try:
            logging.info("Creating a scrum process")    
            scrum_process = model_factories.ScrumProcessFactory(name=team.name, description=team.description, scrum_project = scrum_project)
            self.application_scrum_process.create(scrum_process)
                        
            logging.info("Creating a product backlog definition")    
            product_backlog_definition = model_factories.ProductBacklogDefinitionFactory(name=team.name, description=team.description, scrum_process = scrum_process)
            self.application_product_backlog_definition.create(product_backlog_definition)
                        
            logging.info("Creating a product backlog")   
            product_backlog = model_factories.ProductBacklogFactory(name=team.name, description=team.description, product_backlog_definition = product_backlog_definition.id)
            self.application_product_backlog.create(product_backlog)
                        
            logging.info("Creating a scrum team")  

            scrum_team = model_factories.ScrumTeamFactory(name = team.name, 
                                                                        description = team.description, 
                                                                        scrum_project= scrum_project.id,
                                                                        organization = self.organization)
            
            application_scrum_team = application_factories.ScrumTeamFactory()
            application_scrum_team.create(scrum_team)
                        
            logging.info("Creating a development team")  
            development_team = model_factories.DevelopmentTeamFactory(name = team.name, 
                                                                        description = team.description, 
                                                                        scrum_team_id = scrum_team.id)
                        
            application_development_team = application_factories.DevelopmentTeamFactory()
            application_development_team.create(development_team)
                        
            logging.info("Creating a Application Reference")  
            #Persistindo a referencia
            application_reference = model_factories.ApplicationReferenceFactory(
                            name = scrum_team.name,
                            description = scrum_team.description,
                            application = self.application.id,
                            external_id = team.id,
                            external_url = team.url,
                            external_type_entity = self.TEAM_TFS,
                            internal_uuid = scrum_team.uuid,
                            entity_name = scrum_team.type
                        )
            self.application_application_reference.create(application_reference)

            #Persistindo a referencia
            application_reference = model_factories.ApplicationReferenceFactory(
                            name = development_team.name,
                            description = development_team.description,
                            application = self.application.id,
                            external_id = team.id,
                            external_url = team.url,
                            external_type_entity = self.TEAM_TFS,
                            internal_uuid = development_team.uuid,
                            entity_name = development_team.type
                        )
            self.application_application_reference.create(application_reference)

        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  
