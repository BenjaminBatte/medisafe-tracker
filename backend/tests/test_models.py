import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from app import create_app
from extensions import db

def test_models():
    """Test database models and relationships"""
    app = create_app()
    
    with app.app_context():
        try:
            print("🔧 Testing database models and relationships...")
            
            # Import models
            from models.user import User
            from models.incident import Incident
            
            print("✅ Models imported successfully")
            
            # Check table structure
            print("\n📊 User table columns:", [c.name for c in User.__table__.columns])
            print("📊 Incident table columns:", [c.name for c in Incident.__table__.columns])
            
            # Check foreign keys
            print("\n🔗 Incident foreign keys:")
            for fk in Incident.__table__.foreign_keys:
                print(f"  - {fk}")
            
            # Create tables
            print("\n🛠️ Creating database tables...")
            db.drop_all()  # Clean slate
            db.create_all()
            print("✅ Tables created successfully")
            
            # Test basic CRUD operations
            print("\n🧪 Testing CRUD operations...")
            
            # Create a user
            user = User(
                first_name="John",
                last_name="Doe",
                email="john.doe@example.com"
            )
            db.session.add(user)
            db.session.commit()
            print("✅ User created successfully")
            
            # Create an incident
            incident = Incident(
                title="Test Incident",
                description="This is a test incident",
                severity="Medium",
                user_id=user.id
            )
            db.session.add(incident)
            db.session.commit()
            print("✅ Incident created successfully")
            
            # Test relationships
            print(f"\n🔗 Testing relationships...")
            print(f"User {user.first_name} has {len(user.incidents)} incidents")
            print(f"Incident belongs to user: {incident.user.first_name} {incident.user.last_name}")
            
            # Test querying
            users = User.query.all()
            incidents = Incident.query.all()
            
            print(f"\n📋 Found {len(users)} users and {len(incidents)} incidents")
            
            # Test serialization
            from schemas.user_schema import UserSchema
            from schemas.incident_schema import IncidentSchema
            
            user_schema = UserSchema()
            incident_schema = IncidentSchema()
            
            user_data = user_schema.dump(user)
            incident_data = incident_schema.dump(incident)
            
            print(f"\n📦 User JSON: {user_data}")
            print(f"📦 Incident JSON: {incident_data}")
            
            print("\n🎉 All tests passed! Database relationships are working correctly.")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    test_models()