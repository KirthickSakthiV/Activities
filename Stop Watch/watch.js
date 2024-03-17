
        let startTime;
        let running = false;
        let lapStartTime;
        let lapNumber = 1;

        function startStopwatch() {
            if (!running) {
                running = true;
                startTime = new Date().getTime() - (lapStartTime || 0);
                updateStopwatch();
            }
        }

        function pauseStopwatch() {
            running = false;
            lapStartTime = new Date().getTime() - startTime;
        }

        function resetStopwatch() {
            running = false;
            startTime = 0;
            lapStartTime = 0;
            lapNumber = 1;
            updateStopwatch();
            document.getElementById('time').textContent = '00:00:00';
            document.getElementById('lap-times').innerHTML = '';
        }

        function lapTime() {
            if (running) {
                const currentTime = new Date().getTime() - startTime;
                const lapTime = currentTime - lapStartTime;
                lapStartTime = currentTime;

                const lapTimesContainer = document.getElementById('lap-times');
                const lapElement = document.createElement('div');
                lapElement.textContent = `Lap ${lapNumber}: ${formatTime(lapTime)}`;
                lapTimesContainer.appendChild(lapElement);

                lapNumber++;
            }
        }

        function updateStopwatch() {
            if (running) {
                const currentTime = new Date().getTime() - startTime;
                document.getElementById('time').textContent = formatTime(currentTime);
                setTimeout(updateStopwatch, 10);
            }
        }

        function formatTime(milliseconds) {
            const totalSeconds = Math.floor(milliseconds / 1000);
            const minutes = Math.floor(totalSeconds / 60);
            const seconds = totalSeconds % 60;
            const centiseconds = Math.floor((milliseconds % 1000) / 10);
            return `${padNumber(minutes)}:${padNumber(seconds)}:${padNumber(centiseconds)}`;
        }

        function padNumber(number) {
            return number.toString().padStart(2, '0');
        }

        function showStopwatch() {
            document.getElementById('stopwatch-container').style.display = 'block';
            document.getElementById('settings-container').style.display = 'none';
        }

        function showSettings() {
            document.getElementById('stopwatch-container').style.display = 'none';
            document.getElementById('settings-container').style.display = 'block';
        }
 
	