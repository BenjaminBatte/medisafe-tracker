import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import pytest
from app import create_app
from extensions import db

def test_routes():
    """Test API routes"""
    app = create_app()
    app.config['TESTING'] = True
    
    with app.app_context():
        try:
            print("🔧 Testing API routes...")
            
            # Create test client
            client = app.test_client()
            
            # Create test data
            from models.user import User
            from models.incident import Incident
            
            db.drop_all()
            db.create_all()
            
            user = User(
                first_name="Test",
                last_name="User",
                email="test@example.com"
            )
            db.session.add(user)
            db.session.commit()
            
            # Test health endpoint
            response = client.get('/api/v1/')
            print(f"✅ Health check: {response.status_code} - {response.get_json()}")
            
            # Test users endpoint
            response = client.get('/api/v1/users/')
            print(f"✅ Users endpoint: {response.status_code}")
            
            # Test incidents endpoint
            response = client.get('/api/v1/incidents/')
            print(f"✅ Incidents endpoint: {response.status_code}")
            
            # Test creating a user
            user_data = {
                "first_name": "Jane",
                "last_name": "Smith",
                "email": "jane.smith@example.com"
            }
            response = client.post('/api/v1/users/', json=user_data)
            print(f"✅ Create user: {response.status_code} - {response.get_json()}")
            
            # Test creating an incident
            incident_data = {
                "title": "API Test Incident",
                "description": "Created via API test",
                "severity": "High",
                "user_id": user.id
            }
            response = client.post('/api/v1/incidents/', json=incident_data)
            print(f"✅ Create incident: {response.status_code} - {response.get_json()}")
            
            print("\n🎉 All route tests passed!")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    test_routes()