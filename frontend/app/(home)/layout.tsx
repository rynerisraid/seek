import { Navbar } from "./navbar";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <div className="mt-0">{children}</div>
    </div>
  );
}
