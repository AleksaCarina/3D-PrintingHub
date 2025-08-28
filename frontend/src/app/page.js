"use client";
import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-50 font-sans text-gray-700">
      {/* Header */}
      <header className="bg-orange-600 text-white text-center py-8 text-[3rem] font-bold">
        3D Printing Marketplace
      </header>
      {/* Hero / Intro Section (F-pattern style) */}
      <section className="max-w-[1200px] mx-auto px-6 py-12 grid grid-cols-2 gap-8 items-center">
        {/* Left column: text */}
        <div className="space-y-6">
          <h1 className="text-[2.4rem] font-semibold">
            Discover and Sell Amazing 3D Art
          </h1>
          <p className="text-[1.6rem]">
            Browse unique 3D printed designs from talented artists or showcase your own work. Easy, fast, and secure.
          </p>

          <div className="flex gap-4">
            <Link href="/login">
              <button className="bg-orange-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-orange-700 transition">
                Login
              </button>
            </Link>
            <Link href="/register">
              <button className="bg-white text-orange-600 border-2 border-orange-600 px-6 py-3 rounded-lg font-semibold hover:bg-orange-50 transition">
                Register
              </button>
            </Link>
          </div>
        </div>

        {/* Right column: placeholder 3D image */}
        <div className="h-[24rem] w-[24rem] bg-orange-400 rounded-lg justify-self-center relative"></div>
      </section>

      {/* Featured Section (second F-pattern row) */}
      <section className="max-w-[1200px] mx-auto px-6 py-12 grid grid-cols-2 gap-8 items-center">
        {/* Left column: image */}
        <div className="h-[24rem] w-[24rem] bg-orange-400 rounded-lg justify-self-center relative"></div>

        {/* Right column: text */}
        <div className="space-y-6">
          <h2 className="text-[2rem] font-semibold">
            Sell Your 3D Designs
          </h2>
          <p className="text-[1.6rem]">
            Upload your 3D models, set your price, and reach a community of enthusiasts who appreciate your work.
          </p>
          <Link href="/register">
            <button className="bg-orange-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-orange-700 transition">
              Start Selling
            </button>
          </Link>
        </div>
      </section>

      {/* Call-to-action footer section */}
      <section className="bg-orange-50 py-12 text-center">
        <h3 className="text-[2rem] font-semibold mb-6">
          Ready to explore 3D creations?
        </h3>
        <div className="flex justify-center gap-4">
          <Link href="/login">
            <button className="bg-orange-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-orange-700 transition">
              Login
            </button>
          </Link>
          <Link href="/register">
            <button className="bg-white text-orange-600 border-2 border-orange-600 px-6 py-3 rounded-lg font-semibold hover:bg-orange-50 transition">
              Register
            </button>
          </Link>
        </div>
      </section>
    </main>
  );
}