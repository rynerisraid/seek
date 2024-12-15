import Link from "next/link";
import Image from "next/image";

export const Navbar = () => {
  return (
    <nav className="flex items-center justify-between h-full w-full bg-white shadow-md px-8 py-4">
      {/* Logo and Brand Name */}
      <div className="flex gap-3 items-center shrink-0">
        <Link href="/">
          <Image src="/logo.svg" alt="logo" width={160} height={28} />
        </Link>
        <h3 className="text-xl font-semibold text-gray-800">Seek</h3>
      </div>

      {/* Navigation Links */}
      <div className="hidden md:flex items-center space-x-8">
        <Link href="/">
          <span className="text-gray-600 hover:text-blue-600 transition">
            Home
          </span>
        </Link>
        <Link href="/features">
          <span className="text-gray-600 hover:text-blue-600 transition">
            Features
          </span>
        </Link>
        <Link href="/pricing">
          <span className="text-gray-600 hover:text-blue-600 transition">
            Pricing
          </span>
        </Link>
        <Link href="/about">
          <span className="text-gray-600 hover:text-blue-600 transition">
            About
          </span>
        </Link>
      </div>

      {/* Login and Signup Buttons */}
      <div className="flex items-center space-x-4">
        <Link href="/sign-in">
          <span className="text-gray-600 hover:text-blue-600 transition">
            Sign In
          </span>
        </Link>
        <Link href="/sign-up">
          <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition">
            Sign Up
          </button>
        </Link>
      </div>
    </nav>
  );
};
