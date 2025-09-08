import "./Footer.css";
import "/node_modules/@fortawesome/fontawesome-free/css/all.min.css";

export default function Footer() {
  return (
    <footer className="footer">
      <p className="mb-0">
        © {new Date().getFullYear()} <span>MediSafe Tracker</span> · Built with ❤️ using <span>React</span> + <span>Flask</span>
      </p>
      <div className="social-icons">
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
          <i className="fab fa-twitter"></i>
        </a>
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
          <i className="fab fa-facebook-f"></i>
        </a>
        <a href="https://github.com" target="_blank" rel="noopener noreferrer">
          <i className="fab fa-github"></i>
        </a>
        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer">
          <i className="fab fa-linkedin-in"></i>
        </a>
      </div>
    </footer>
  );
}
