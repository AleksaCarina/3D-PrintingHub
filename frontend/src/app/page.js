// app/page.js

"use client";
import "./globals.css";
import { useState } from "react";
import Image from 'next/image';
import Link from 'next/link';


export default function HomePage() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div>
      <header>
        <div className="TitleHeader">
          <img
            className="imgTitle"
            src="/logo.png"
            alt="3D Hub"
            style={{ height: "40px", verticalAlign: "middle" }}
          />
          <div className="nameTitle">3D Hub</div>
        </div>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="#" className="active">About Us</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
        <div className="auth-buttons">
          <button onClick={() => setSidebarOpen(true)}>Login</button>
          <button>Register</button>
        </div>
      </header>

      <main>
        <section className="about">
          <h1>About Us</h1>
          <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
        </section>
              {/* replace <img .../> with <Image .../> */}
      <Image src="/logo.png" alt="Logo" width={256} height={64} priority />

      {/* replace <a href="/">...</a> with <Link href="/">...</Link> */}
      <p>
        Go <Link href="/">home</Link>
      </p>

      </main>

      {sidebarOpen && (
        <div className="sidebar">
          <span onClick={() => setSidebarOpen(false)}>&times;</span>
          <h2>Login</h2>
          <form>
            <input type="text" placeholder="Username" />
            <input type="password" placeholder="Password" />
            <button type="submit">Login</button>
          </form>
        </div>
      )}
    </div>
  );
}
