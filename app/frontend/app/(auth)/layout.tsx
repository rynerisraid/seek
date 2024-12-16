// auth/layout.tsx
export default function AuthLayout({ children }: {children:React.ReactNode}) {
  return (
    <div className="flex items-center justify-center h-screen bg-gray-100">
      {children}
    </div>
  );
}