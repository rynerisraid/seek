export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen flex flex-col">
      <div>This is nav bar</div>
      <div className="mt-0">{children}</div>
    </div>
  );
}
