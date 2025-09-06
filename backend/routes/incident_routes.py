from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from extensions import db
from models.incident import Incident
from schemas.incident_schema import IncidentSchema

# versioned blueprint
incident_bp = Blueprint("incidents", __name__, url_prefix="/api/v1/incidents")

incident_schema = IncidentSchema()
incidents_schema = IncidentSchema(many=True)


# --- Utility helpers ---
def error_response(message, status=400, details=None):
    payload = {"error": message, "status": status}
    if details:
        payload["details"] = details
    return jsonify(payload), status


# --- Routes ---

# GET all incidents with pagination
@incident_bp.route("/", methods=["GET"])
def get_incidents():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    pagination = Incident.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "data": incidents_schema.dump(pagination.items),
        "meta": {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page
        }
    })


# GET by ID
@incident_bp.route("/<int:incident_id>", methods=["GET"])
def get_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return error_response("Incident not found", 404)
    return {"data": incident_schema.dump(incident)}, 200


# CREATE
@incident_bp.route("/", methods=["POST"])
def create_incident():
    try:
        data = incident_schema.load(request.get_json() or {})
    except ValidationError as err:
        return error_response("Validation error", 400, err.messages)

    new_incident = Incident(**data)

    try:
        db.session.add(new_incident)
        db.session.commit()
        return {"data": incident_schema.dump(new_incident)}, 201
    except IntegrityError as e:
        db.session.rollback()
        return error_response("Database integrity error", 400, str(e.orig))


# UPDATE
@incident_bp.route("/<int:incident_id>", methods=["PUT"])
def update_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return error_response("Incident not found", 404)

    try:
        data = incident_schema.load(request.get_json() or {}, partial=True)
    except ValidationError as err:
        return error_response("Validation error", 400, err.messages)

    for key, value in data.items():
        setattr(incident, key, value)

    try:
        db.session.commit()
        return {"data": incident_schema.dump(incident)}, 200
    except IntegrityError as e:
        db.session.rollback()
        return error_response("Database integrity error", 400, str(e.orig))


# DELETE
@incident_bp.route("/<int:incident_id>", methods=["DELETE"])
def delete_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return error_response("Incident not found", 404)

    db.session.delete(incident)
    db.session.commit()
    return {"message": f"Incident {incident_id} deleted successfully"}, 200
