const { exec } = require('child_process');
function startAssistant() {
  const output = document.getElementById('output');
  output.textContent = "🎙️ Listening...";

  exec('./nova-venv/bin/python backend.py', (err, stdout, stderr) => {
    if (err) {
      output.textContent = `❌ Error: ${err.message}`;
      return;
    }
    output.textContent = `🧠 NOVA heard:\n${stdout}`;
  });
}
