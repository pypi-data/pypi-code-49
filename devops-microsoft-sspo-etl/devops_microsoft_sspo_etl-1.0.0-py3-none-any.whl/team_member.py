from .base_entity import BaseEntity
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import re  

import logging
logging.basicConfig(level=logging.INFO)

class TeamMember(BaseEntity):

    def do(self,data):

        try:
            logging.info("Team Member")

            self.config(data)
            
            projects = self.tfs.get_projects()
            application_person = application_factories.PersonFactory()
            application_scrum_team = application_factories.ScrumTeamFactory()
            application_development_team = application_factories.DevelopmentTeamFactory()
            application_scrum_master = application_factories.ScrumMasterFactory()
            application_developer = application_factories.DeveloperFactory()
            
            for project in projects:
                logging.info("Team Member: retrive teams from " +project.name)
                teams = self.tfs.get_teams(project.id)
                for team_tfs in teams:
                    
                    team_members = self.tfs.get_team_members(project.id,team_tfs.id)
                    logging.info("Team Member: retrive team member from " +team_tfs.name)
                    
                    for team_member in team_members:
                        person = application_person.retrive_by_external_uuid(team_member.identity.id)   
                            
                        if person is None:
                            logging.info("Team Member: create a person")
                                
                            email = None
                                
                            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
                                
                            if(re.search(regex,team_member.identity.unique_name)): 
                                email = team_member.identity.unique_name

                            person = model_factories.PersonFactory(name=team_member.identity.display_name,
                                                                        email=email,
                                                                        organization = self.organization)
                                
                            application_person.create (person)
                                
                            logging.info("Team Member: create a person's reference")

                            application_reference = model_factories.ApplicationReferenceFactory(
                                                        name = person.name,
                                                        description = person.description,
                                                        application = self.application.id,
                                                        external_id = team_member.identity.id,
                                                        external_url = team_member.identity.url,
                                                        external_type_entity = self.TEAM_MEMBER_TFS,
                                                        internal_uuid = person.uuid,
                                                        entity_name = person.__tablename__
                                                    )

                            self.application_application_reference.create(application_reference)
                        
                        scrum_team = application_scrum_team.retrive_by_external_uuid(team_tfs.id)  
                        development_team = application_development_team.retrive_by_external_uuid(team_tfs.id)   
                        
                        logging.info("Team Member: creating a team member")
                        
                        if team_member.is_team_admin:
                            logging.info("Team Member: Scrum Master")
                            scrum_master = model_factories.ScrumMasterFactory(
                                name = person.name,
                                description = person.description,
                                person = person,
                                team = scrum_team,
                                team_role = ""
                            )
                            application_scrum_master.create(scrum_master)
                            
                        else:
                            logging.info("Team Member: Developer")
                            developer = model_factories.DeveloperFactory(
                                name = person.name,
                                description = person.description,
                                person = person,
                                team = development_team,
                                team_role = ""
                            )
                            application_developer.create(developer)
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)              