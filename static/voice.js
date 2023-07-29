const startButton = document.querySelector('#start-button');
const stopButton = document.querySelector('#stop-button');
const results = document.querySelector('#txtBox2');

const recognition = new webkitSpeechRecognition();
recognition.interimResults = true;
recognition.continuous = true;
recognition.lang = 'ur';  // Set the language to Urdu

startButton.addEventListener('click', function() {
  recognition.start();
});

stopButton.addEventListener('click', function() {
  recognition.stop();
});

recognition.addEventListener('result', function(event) {
  let text = '';
  for (let i = event.resultIndex; i < event.results.length; i++) {
    text += event.results[i][0].transcript;
  }
  results.textContent = text;
});
