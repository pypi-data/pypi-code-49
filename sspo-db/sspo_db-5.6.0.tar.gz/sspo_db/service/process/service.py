from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.process.models import *
from sspo_db.service.base_service import BaseService
from sspo_db.service.core.service import ApplicationReferenceService

class ScrumProjectService(BaseService):
    def __init__(self):
        super(ScrumProjectService,self).__init__(ScrumProject)
    
class ScrumComplexProjectService(BaseService):
    def __init__(self):
        super(ScrumComplexProjectService,self).__init__(ScrumComplexProject)

class ScrumAtomicProjectService(BaseService):
    def __init__(self):
        super(ScrumAtomicProjectService,self).__init__(ScrumAtomicProject)

class ScrumProcessService(BaseService):
    def __init__(self):
        super(ScrumProcessService,self).__init__(ScrumProcess)

class ProductBacklogDefinitionService(BaseService):
    def __init__(self):
        super(ProductBacklogDefinitionService,self).__init__(ProductBacklogDefinition)

class SprintService(BaseService):
    def __init__(self):
        super(SprintService,self).__init__(Sprint)

    def retrive_by_name_and_project_name(self, sprint_name, project_name):
        return self.session.query(Sprint).join(ScrumProcess).join(ScrumProject).filter(ScrumProject.name.like(project_name), Sprint.name.like(sprint_name)).first()

class CerimonyService(BaseService):
    def __init__(self):
        super(CerimonyService,self).__init__(Cerimony)

class PlanningMeetingService(BaseService):
    def __init__(self):
        super(PlanningMeetingService,self).__init__(PlanningMeeting)

class DailyStandupMeetingService(BaseService):
    def __init__(self):
        super(DailyStandupMeetingService,self).__init__(DailyStandupMeeting)

class ReviewMeetingService(BaseService):
    def __init__(self):
        super(ReviewMeetingService,self).__init__(ReviewMeeting)

class RetrospectiveMeetingService(BaseService):
    def __init__(self):
        super(RetrospectiveMeetingService,self).__init__(RetrospectiveMeeting)