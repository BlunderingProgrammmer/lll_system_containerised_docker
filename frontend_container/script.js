const promptInput = document.getElementById('prompt-input');
const submitBtn = document.getElementById('submit-btn');
const llmOutput = document.getElementById('llm-output');
const listenBtn = document.getElementById('listen-btn');

// Determine backend URL based on environment
const hostname = window.location.hostname;
const LLM_BACKEND_URL = hostname === 'localhost' || hostname === '127.0.0.1' ? 'http://localhost:8000/generate' : 'http://backend:8000/generate';
const TTS_SERVICE_URL  = hostname === 'localhost' || hostname === '127.0.0.1' ? 'http://localhost:8002/process' : 'http://prompt_voice:8002/process';

let audio = null;

async function fetchLLMResponse(prompt) {
  llmOutput.textContent = "Loading...";
  try {
    const res = await fetch(LLM_BACKEND_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, max_length: 50 })
    });
    if (!res.ok) throw new Error(`Backend error: ${res.statusText}`);
    const data = await res.json();
    llmOutput.textContent = data.response;

    await playAudio(prompt, data.response);
  } catch (error) {
    llmOutput.textContent = `Error: ${error.message}`;
    listenBtn.style.display = 'none';
  }
}

async function playAudio(prompt, response) {
  try {
    const sessionId = Date.now().toString();
    const res = await fetch(TTS_SERVICE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId, prompt, response })
    });
    if (!res.ok) throw new Error(`TTS service error: ${res.statusText}`);
    const { audio_url } = await res.json();
    if (audio) {
      audio.pause();
      audio = null;
    }
    audio = new Audio(`${TTS_SERVICE_URL.replace('/process', '')}${audio_url}`);
    listenBtn.style.display = 'inline-block';
  } catch (error) {
    console.error(error);
    listenBtn.style.display = 'none';
  }
}

submitBtn.onclick = () => {
  const prompt = promptInput.value.trim();
  if (prompt) fetchLLMResponse(prompt);
};

listenBtn.onclick = () => {
  if (audio) {
    audio.play();
  }
};
