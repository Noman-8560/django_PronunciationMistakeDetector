const startButton = document.getElementById('startRecording');
const stopButton = document.getElementById('stopRecording');
const audioPlayer = document.getElementById('audioPlayer');
let mediaRecorder;
let audioChunks = [];

startButton.addEventListener('click', () => {
    console.log('Start button clicked'); // Add this line for debugging
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            console.log('getUserMedia success'); // Add this line for debugging
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = event => {
                if (event.data.size > 0) {
                    audioChunks.push(event.data);
                }
            };

            mediaRecorder.onstop = () => {
                console.log('Recording stopped'); // Add this line for debugging
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                const audioData = URL.createObjectURL(audioBlob);

                audioPlayer.src = audioData;
                audioPlayer.play();
            };

            mediaRecorder.start();
            startButton.disabled = true;
            stopButton.disabled = false;
        })
        .catch(error => {
            console.error('Error accessing microphone:', error);
        });
});

stopButton.addEventListener('click', () => {
    console.log('Stop button clicked'); // Add this line for debugging
    if (mediaRecorder) {
        mediaRecorder.stop();
        startButton.disabled = false;
        stopButton.disabled = true;
    }
});
