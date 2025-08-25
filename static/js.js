document.addEventListener("DOMContentLoaded", () => {
  const loginBtn = document.getElementById("loginBtn");
  const registerBtn = document.getElementById("registerBtn");
  const sidebar = document.getElementById("loginSidebar");
  const closeSidebar = document.getElementById("closeSidebar");
  const loginForm = document.getElementById("loginForm");

  // Otvaranje sidebar-a
  loginBtn.addEventListener("click", () => sidebar.classList.add("active"));
  closeSidebar.addEventListener("click", () => sidebar.classList.remove("active"));
  window.addEventListener("click", (e) => {
    if (e.target === sidebar) sidebar.classList.remove("active");
  });

  // Submit login forme
  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
      });
      const data = await response.json();

      if (data.success) {
        alert("✅ Login successful!");
        sidebar.classList.remove("active");
      } else {
        alert("❌ " + data.message);
      }
    } catch(err){
      console.error(err);
      alert("Error during login. Check console.");
    }
  });
});
