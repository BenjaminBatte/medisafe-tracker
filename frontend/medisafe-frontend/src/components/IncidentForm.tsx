import { useState } from "react";
import type { Incident } from "../api/incidents";
import styles from "./IncidentForm.module.css";

interface IncidentFormProps {
  onSubmit: (incident: Incident) => Promise<void>;
}

export default function IncidentForm({ onSubmit }: IncidentFormProps) {
  const [form, setForm] = useState<Incident>({
    title: "",
    description: "",
    severity: "Low",
    user_id: 1, // default for testing, later make dynamic
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await onSubmit(form);
    setForm({ title: "", description: "", severity: "Low", user_id: 1 });
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <input
        className={`form-control mb-2 ${styles.input}`}
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
      />
      <textarea
        className={`form-control mb-2 ${styles.textarea}`}
        name="description"
        placeholder="Description"
        value={form.description}
        onChange={handleChange}
      />
      <select
        className={`form-control mb-2 ${styles.select}`}
        name="severity"
        value={form.severity}
        onChange={handleChange}
      >
        <option value="Low">Low</option>
        <option value="Medium">Medium</option>
        <option value="High">High</option>
        <option value="Critical">Critical</option>
      </select>
      <input
        className={`form-control mb-2 ${styles.input}`}
        type="number"
        name="user_id"
        placeholder="User ID"
        value={form.user_id}
        onChange={handleChange}
      />
      <button className={`btn btn-danger ${styles.button}`}>Add Incident</button>
    </form>
  );
}
