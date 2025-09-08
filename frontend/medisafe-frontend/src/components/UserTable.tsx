import type { User } from "../api/users";
import styles from "./UserTable.module.css";

interface UserTableProps {
  users: User[];
}

export default function UserTable({ users }: UserTableProps) {
  if (!users || users.length === 0) {
    return <p className="text-muted">No users found.</p>;
  }

  return (
    <div className="table-responsive">
      <table className={`table table-striped table-hover ${styles.table}`}>
        <thead className="table-dark">
          <tr>
            <th>#</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u, idx) => (
            <tr key={u.id}>
              <td>{idx + 1}</td>
              <td>{u.first_name}</td>
              <td>{u.last_name}</td>
              <td>{u.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
