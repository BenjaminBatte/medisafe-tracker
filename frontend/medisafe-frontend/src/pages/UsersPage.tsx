import { useEffect, useState } from "react";
import { getUsers, addUser, type User } from "../api/users";
import UserForm from "../components/UserForm";
import UserTable from "../components/UserTable";

export default function UsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchUsers = async (p = 1) => {
    const res = await getUsers(p);
    setUsers(res.data.users);
    setPage(res.data.page);
    setTotalPages(res.data.pages);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleAddUser = async (user: User) => {
    await addUser(user);
    fetchUsers(page); // refresh current page
  };

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <UserForm onSubmit={handleAddUser} />
      <UserTable users={users} />

      {/* Pagination */}
      <nav className="mt-3">
        <ul className="pagination">
          <li className={`page-item ${page === 1 ? "disabled" : ""}`}>
            <button className="page-link" onClick={() => fetchUsers(page - 1)}>
              Previous
            </button>
          </li>

          {[...Array(totalPages)].map((_, idx) => (
            <li
              key={idx}
              className={`page-item ${page === idx + 1 ? "active" : ""}`}
            >
              <button
                className="page-link"
                onClick={() => fetchUsers(idx + 1)}
              >
                {idx + 1}
              </button>
            </li>
          ))}

          <li className={`page-item ${page === totalPages ? "disabled" : ""}`}>
            <button className="page-link" onClick={() => fetchUsers(page + 1)}>
              Next
            </button>
          </li>
        </ul>
      </nav>
    </div>
  );
}
