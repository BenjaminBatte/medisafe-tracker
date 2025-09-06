from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from extensions import db
from models.user import User
from schemas.user_schema import UserSchema

# versioned blueprint
user_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


# --- Utility helpers ---
def error_response(message, status=400, details=None):
    payload = {"error": message, "status": status}
    if details:
        payload["details"] = details
    return jsonify(payload), status


# --- Routes ---

# Get all users with pagination
@user_bp.route("/", methods=["GET"])
def get_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "data": users_schema.dump(pagination.items),
        "meta": {
            "total": pagination.total,
            "page": pagination.page,
            "pages": pagination.pages,
            "per_page": pagination.per_page
        }
    })


# Get a user by ID
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return error_response("User not found", 404)
    return {"data": user_schema.dump(user)}, 200


# Create a new user
@user_bp.route("/", methods=["POST"])
def add_user():
    try:
        data = user_schema.load(request.get_json() or {})
    except ValidationError as err:
        return error_response("Validation error", 400, err.messages)

    new_user = User(**data)

    try:
        db.session.add(new_user)
        db.session.commit()
        return {"data": user_schema.dump(new_user)}, 201
    except IntegrityError as e:
        db.session.rollback()
        if "users_email_key" in str(e.orig):
            return error_response("Email already exists", 409)
        return error_response("Database integrity error", 400, str(e.orig))


# Update a user by ID
@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return error_response("User not found", 404)

    try:
        data = user_schema.load(request.get_json() or {}, partial=True)
    except ValidationError as err:
        return error_response("Validation error", 400, err.messages)

    for key, value in data.items():
        setattr(user, key, value)

    try:
        db.session.commit()
        return {"data": user_schema.dump(user)}, 200
    except IntegrityError as e:
        db.session.rollback()
        if "users_email_key" in str(e.orig):
            return error_response("Email already exists", 409)
        return error_response("Database integrity error", 400, str(e.orig))


# Delete a user by ID
@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return error_response("User not found", 404)

    db.session.delete(user)
    db.session.commit()
    return {"message": f"User {user_id} deleted successfully"}, 200
