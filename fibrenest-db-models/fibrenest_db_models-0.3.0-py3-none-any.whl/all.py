from fibrenest_db_models.common import *


class ONT(Base):
    __tablename__ = 'ont'

    id = Column(Integer, primary_key=True)
    sn = Column(String(length=64), nullable=False, unique=True)
    portid = Column(Integer, nullable=False)
    slotid = Column(Integer, nullable=False)
    frameid = Column(Integer, nullable=False)
    ontid = Column(Integer)
    model = Column(String(length=64))
    netbox_siteid = Column(Integer)
    olt_ip = Column(String(length=64), nullable=False)
    sitename = Column(String(length=256))
    ont_registered = Column(Boolean, nullable=False, default=False, comment='If the ONT is registered on the OLT or not')
    ont_register_datetime = Column(DateTime)
    prov_type = Column(Enum(CPEProvTypeENUM), comment='Provisioning type of the ONT. Valid values: bridge or gateway')
    s_vlan = Column(Integer)
    c_vlan = Column(Integer)

    subscription = relationship('SUBSCRIPTION', back_populates='ont')

    def __repr__(self):
        return repr(self)
