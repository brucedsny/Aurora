class CognitiveTracker {
    constructor(baselineSpeedMs = 300) {
        this.baselineSpeedMs = baselineSpeedMs; // Normal average time between keys
        this.lastKeyPressTime = null;
        this.sluggishKeystrokesCount = 0;
    }

    analyzeKeystroke() {
        const currentTime = new Date().getTime();

        if (this.lastKeyPressTime) {
            const timeDiff = currentTime - this.lastKeyPressTime;
            
            // If the user takes significantly longer than their baseline to find the next key
            if (timeDiff > this.baselineSpeedMs * 2.5) {
                this.sluggishKeystrokesCount++;
            }

            // Trigger intervention if a pattern of cognitive slowing is detected
            if (this.sluggishKeystrokesCount > 5) {
                this.triggerHydrationIntervention();
                this.sluggishKeystrokesCount = 0; // Reset after warning
            }
        }
        this.lastKeyPressTime = currentTime;
    }

    triggerHydrationIntervention() {
        console.warn("[Health Alert] Cognitive slowing detected in motor skills.");
        alert("Your typing is a bit slower today. Let's take a 5-minute break and drink a glass of water!");
    }
}

// Attach to an interface
const tracker = new CognitiveTracker();
// document.getElementById('messageInput').addEventListener('keyup', () => tracker.analyzeKeystroke());
