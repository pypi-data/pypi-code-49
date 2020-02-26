from .base_entity import BaseEntity
import logging

logging.basicConfig(level=logging.INFO)

from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
class Sprint(BaseEntity):
    
    def do(self,data):
        try:

            self.config(data)
            logging.info("Interaction")

            self.application_sprint =  application_factories.SprintFactory()
            
            application_scrum_atomic = application_factories.ScrumAtomicProjectFactory()
            application_sprint_backlog = application_factories.SprintBacklogFactory()

            # Buscando os projetos do TFS
            projects = self.tfs.get_projects()
            
            for project in projects:
                
                atomic = True
                teams = self.tfs.get_teams(project.id)
                
                if len(teams) > 1:
                    atomic = False
                
                for team in teams: 

                    interactions = self.tfs.get_interactions(project,team)
                    project_id = team.id 
                    
                    if atomic: 
                        project_id = project.id

                    atomic_project = application_scrum_atomic.retrive_by_external_uuid(project_id)
                    scrum_process = atomic_project.scrum_process

                    sprint = model_factories.SprintFactory(name = "Limbo", description = "Limbo", scrum_process = scrum_process )
                    
                    self.application_sprint.create(sprint)
                    
                    sprint_backlog = model_factories.SprintBacklogFactory()
                    sprint_backlog.sprint = sprint.id
                    sprint_backlog.name = sprint.name
                    sprint_backlog.description = sprint.description
                    application_sprint_backlog.create(sprint_backlog)
                        
                    for interaction in interactions:
                    
                        logging.info("Interaction: Creating interaction")
                        
                        name = interaction.name
                        interaction_id = interaction.id
                        finish = interaction.attributes.finish_date 
                        start = interaction.attributes.start_date 
                        
                        sprint = model_factories.SprintFactory(name = name, 
                            description =name, 
                            scrum_process = scrum_process,
                            startDate = start,
                            endDate = finish
                            )
                    
                        self.application_sprint.create(sprint)

                        application_reference = model_factories.ApplicationReferenceFactory(
                                                        name =name,
                                                        description = name,
                                                        application = self.application.id,
                                                        external_id = interaction.id,
                                                        external_type_entity = self.SPRINT_TFS,
                                                        internal_uuid = sprint.uuid,
                                                        entity_name = sprint.__tablename__
                                                        
                                                    )

                        self.application_application_reference.create(application_reference)
                        
                        logging.info("Interaction: Sprint Backlog")
                        
                        sprint_backlog = model_factories.SprintBacklogFactory(
                            name = sprint.name,
                            description = sprint.description,
                            sprint = sprint.id
                        )
                        
                        application_sprint_backlog.create(sprint_backlog)
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)  



                    