// Get elements
const loginBtn = document.getElementById('loginBtn');
const registerBtn = document.getElementById('registerBtn');
const loginModal = document.getElementById('loginModal');
const registerModal = document.getElementById('registerModal');
const closeBtns = document.querySelectorAll('.close');

// Open modals
loginBtn.onclick = () => loginModal.style.display = 'flex';
registerBtn.onclick = () => registerModal.style.display = 'flex';

// Close modals
closeBtns.forEach(btn => {
btn.onclick = () => {
loginModal.style.display = 'none';
registerModal.style.display = 'none';
}
});

// Close when clicking outside
window.onclick = (e) => {
if (e.target === loginModal) loginModal.style.display = 'none';
if (e.target === registerModal) registerModal.style.display = 'none';
};

document.getElementById("loginBtn").addEventListener("submit", async function(e) {
  e.preventDefault(); // sprečava reload stranice

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ username, password })
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    if (data.success) {
      alert("✅ Login successful!");
      // npr. redirect na dashboard
      // window.location.href = "/dashboard.html";
    } else {
      alert("❌ Invalid credentials: " + data.message);
    }
  } catch (error) {
    console.error("Error:", error);
    alert("Something went wrong. Check console.");
  }
});
