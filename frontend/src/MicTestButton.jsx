// Save this as src/MicTestButton.js
import React from "react";

function MicTestButton() {
  const requestMic = () => {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(() => {
        alert("Microphone access granted! Now try your voice navigation.");
      })
      .catch(err => {
        alert("Microphone blocked or denied: " + err.message);
        console.error(err);
      });
  };

  return (
    <button onClick={requestMic}>
      Enable Microphone (Test)
    </button>
  );
}

export default MicTestButton;
