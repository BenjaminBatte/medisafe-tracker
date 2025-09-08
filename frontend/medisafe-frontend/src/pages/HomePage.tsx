import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <div className="text-center mt-5">
      <h1 className="display-4 mb-4">Welcome to MediSafe Tracker 🚀</h1>
      <p className="lead mb-5">
        Track medication incidents and manage users effectively.  
        Stay safe, stay on schedule.
      </p>

      <div className="d-flex justify-content-center gap-3">
        <Link to="/users" className="btn btn-primary btn-lg">
          👤 Manage Users
        </Link>
        <Link to="/incidents" className="btn btn-danger btn-lg">
          ⚠️ Track Incidents
        </Link>
      </div>
    </div>
  );
}
