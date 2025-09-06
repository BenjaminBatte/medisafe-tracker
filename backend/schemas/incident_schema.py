from extensions import ma
from models.incident import Incident

class IncidentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Incident
        load_instance = False   
        include_fk = True       

    id = ma.auto_field(dump_only=True)
    title = ma.auto_field(required=True)
    description = ma.auto_field(required=True)
    severity = ma.auto_field(required=True)
    user_id = ma.auto_field(required=True)
