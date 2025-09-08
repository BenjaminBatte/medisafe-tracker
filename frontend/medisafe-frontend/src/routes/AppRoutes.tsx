import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "../pages/HomePage";
import UsersPage from "../pages/UsersPage";
import IncidentsPage from "../pages/IncidentsPage";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function AppRoutes() {
  return (
    <Router>
      <div className="d-flex flex-column min-vh-100">
        <Navbar />
        <main className="flex-grow-1 container mt-4">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/users" element={<UsersPage />} />
            <Route path="/incidents" element={<IncidentsPage />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}
