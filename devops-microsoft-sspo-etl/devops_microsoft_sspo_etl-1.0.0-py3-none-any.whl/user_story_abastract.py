from .base_entity import BaseEntity
from datetime import datetime
from sspo_db.application import factories as application_factories
from sspo_db.model import factories as model_factories
import logging
logging.basicConfig(level=logging.INFO)

class UserStoryAbstract(BaseEntity):

    def __init__(self):

        super().__init__()
        self.application_product_backlog = application_factories.ProductBacklogFactory()
        self.application_team_member = application_factories.TeamMemberFactory()
        self.product_backlogs = {}
        self.team_members = {}

    def config(self, data):
        super().config(data)
        
    def retrive_project_name(self, element):
        project_name = self.check_value(element,"System.AreaLevel2") 
        if project_name is None:
            project_name = self.check_value(element,"System.AreaLevel1") 
        return project_name

    def retrive_team_members(self, element, seon_element):
        try:
            created_by = self.check_value(element,'System.CreatedBy')
            activated_by = self.check_value(element,'Microsoft.VSTS.Common.ActivatedBy') 
            closed_by = self.check_value(element,'Microsoft.VSTS.Common.ClosedBy') 
            assigned_by = self.check_value(element,'System.AssignedTo')

            project_name = self.retrive_project_name(element)

            if created_by is not None and created_by is not 'None':
                team_member = self.retrive_team_member_seon(created_by,project_name)
                seon_element.created_by = team_member.id
                            
            if activated_by is not None and activated_by is not 'None':
                team_member = self.retrive_team_member_seon(activated_by,project_name)
                seon_element.activated_by = team_member.id
            
            if closed_by is not None and closed_by is not 'None':
                team_member = self.retrive_team_member_seon(closed_by,project_name)
                seon_element.closed_by = team_member.id
            
            if assigned_by is not None and assigned_by is not 'None':
                logging.info("Assigned: "+assigned_by['id'])
                team_member = self.retrive_team_member_seon(assigned_by,project_name)
                if team_member is not None:
                    seon_element.assigned_by = [team_member]
        
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)              

        
        
    def retrive_product_backlog(self, project_name):
        if project_name in self.product_backlogs:
            return self.product_backlogs[project_name]
        else:
            product_backlog = self.application_product_backlog.retrive_by_project_name(project_name)
            self.product_backlogs[project_name] = product_backlog 
            return product_backlog    

    def validate_date_format(self, date):

        try:
            return datetime.strptime(str(date), '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            return datetime.strptime(str(date), '%Y-%m-%dT%H:%M:%SZ')

    def retrive_dates(self, element, seon_element):

        created_data = self.check_value(element,'System.CreatedDate')
        activated_date = self.check_value(element,'Microsoft.VSTS.Common.ActivatedDate')
        resolved_date = self.check_value(element,'Microsoft.VSTS.Common.ResolvedDate')
        closed_date = self.check_value(element,'Microsoft.VSTS.Common.ClosedDate')

        if created_data is not None and created_data is not 'None':
            seon_element.created_date = self.validate_date_format(str(created_data)) 
                            
        if activated_date is not None and activated_date is not 'None':
            seon_element.activated_date = self.validate_date_format(str(activated_date))
                    
        if resolved_date is not None and resolved_date is not 'None':
            seon_element.resolved_date = self.validate_date_format(str(resolved_date)) 
                    
        if closed_date is not None and closed_date is not 'None':
            seon_element.closed_date = self.validate_date_format(str(closed_date))
            
    def set_name_description (self, element, seon_element):
        seon_element.name = element.fields['System.Title']
        seon_element.description = str(self.check_value(element,'System.Description'))
        
    