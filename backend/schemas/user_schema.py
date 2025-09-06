from extensions import ma
from models.user import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = False  

    id = ma.auto_field(dump_only=True) 
    first_name = ma.auto_field(required=True)
    last_name = ma.auto_field(required=True)
    email = ma.auto_field(required=True)
