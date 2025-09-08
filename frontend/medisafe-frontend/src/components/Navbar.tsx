import { Link, NavLink } from "react-router-dom";
import "./Navbar.css"; 

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary px-3 shadow-sm">
      <Link className="navbar-brand fw-bold text-white" to="/">
        MediSafe Tracker
      </Link>
      <div className="navbar-nav ms-auto">
        <NavLink to="/users" className="nav-link">
          Users
        </NavLink>
        <NavLink to="/incidents" className="nav-link">
          Incidents
        </NavLink>
      </div>
    </nav>
  );
}
