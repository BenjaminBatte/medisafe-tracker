import { useState } from "react";
import type { User } from "../api/users";
import styles from "./UserForm.module.css";

interface UserFormProps {
  onSubmit: (user: User) => Promise<void>;
}

export default function UserForm({ onSubmit }: UserFormProps) {
  const [form, setForm] = useState<User>({
    first_name: "",
    last_name: "",
    email: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await onSubmit(form);
    setForm({ first_name: "", last_name: "", email: "" });
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <input
        className={`form-control mb-2 ${styles.input}`}
        name="first_name"
        placeholder="First name"
        value={form.first_name}
        onChange={handleChange}
      />
      <input
        className={`form-control mb-2 ${styles.input}`}
        name="last_name"
        placeholder="Last name"
        value={form.last_name}
        onChange={handleChange}
      />
      <input
        className={`form-control mb-2 ${styles.input}`}
        type="email"
        name="email"
        placeholder="Email"
        value={form.email}
        onChange={handleChange}
      />
      <button className={`btn btn-primary ${styles.button}`}>Add User</button>
    </form>
  );
}
