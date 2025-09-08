import type { Incident } from "../api/incidents";
import styles from "./IncidentTable.module.css";

interface IncidentTableProps {
  incidents: Incident[];
}

export default function IncidentTable({ incidents }: IncidentTableProps) {
  if (!incidents || incidents.length === 0) {
    return <p className="text-muted">No incidents reported yet.</p>;
  }

  return (
    <div className="table-responsive">
      <table className={`table table-bordered table-hover ${styles.table}`}>
        <thead className="table-dark">
          <tr>
            <th>#</th>
            <th>Title</th>
            <th>Severity</th>
            <th>Description</th>
            <th>User ID</th>
          </tr>
        </thead>
        <tbody>
          {incidents.map((i, idx) => (
            <tr key={i.id}>
              <td>{idx + 1}</td>
              <td>{i.title}</td>
              <td>
                <span
                  className={`badge ${
                    i.severity === "Critical"
                      ? "bg-danger"
                      : i.severity === "High"
                      ? "bg-warning text-dark"
                      : "bg-secondary"
                  }`}
                >
                  {i.severity}
                </span>
              </td>
              <td>{i.description}</td>
              <td>{i.user_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
