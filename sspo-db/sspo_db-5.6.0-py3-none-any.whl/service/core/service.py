from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sspo_db.model.core.models import *
from sspo_db.service.base_service import BaseService

class ApplicationTypeService(BaseService):
    def __init__(self):
        super(ApplicationTypeService,self).__init__(ApplicationType)

class ConfigurationService(BaseService):
    def __init__(self):
        super(ConfigurationService,self).__init__(Configuration)

class ApplicationReferenceService(BaseService):
    def __init__(self):
        super(ApplicationReferenceService,self).__init__(ApplicationReference)

    def retrive_by_external_id (self, external_id):
        return self.session.query(ApplicationReference).filter(ApplicationReference.external_id == external_id).first()
    
    def retrive_by_external_id_and_seon_entity_name (self, external_id, seon_entity_name):
        return self.session.query(ApplicationReference).filter(ApplicationReference.external_id == external_id, 
                                                               ApplicationReference.entity_name == seon_entity_name).first()

class ApplicationService(BaseService):
    def __init__(self):
        super(ApplicationService,self).__init__(Application)
    
    def retrive_by_name(self, name):
        return self.session.query(Application).filter(Application.name == name).first()
        
