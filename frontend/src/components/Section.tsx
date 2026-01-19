import { ReactNode } from "react";

type Props = {
  title: string;
  children: ReactNode;
};

export default function Section({ title, children }: Props) {
  return (
    <section
      style={{
        border: "1px solid #ddd",
        padding: 16,
        borderRadius: 4,
      }}
    >
      <h2 style={{ marginTop: 0 }}>{title}</h2>
      {children}
    </section>
  );
}
