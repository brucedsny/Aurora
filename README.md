# GeriOS-Core: Open-Source Geriatric Care Infrastructure

**GeriOS-Core** is a foundational framework of open-source primitives designed to solve the "Invisible Infrastructure" gap in geriatric technology. As the global population ages, there is a critical lack of standardized, non-invasive software modules for cognitive support, circadian stabilization, and early-stage health telemetry.

This repository provides the core logic for developers to build safe, AI-driven interventions for elderly patients, particularly those with neurodegenerative conditions like Dementia and Alzheimer's.

## 🛠 Core Modules (Alpha)

### 1. `circadian-anchor` (Sundowning Prevention)
An IoT-integration module that acts as an artificial biological clock. It uses automated light/sound modulation to mitigate Sundowning Syndrome confusion at dusk.
- **Tech:** Python, IoT-Mock API, Circadian Scheduling.

### 2. `binary-ui-framework` (Cognitive Load Reduction)
A UI/UX component library that forces a binary decision flow (Choice Reduction). It targets decision fatigue in the aging brain by abstracting complex lists into simple A/B selections.
- **Tech:** React/JavaScript.

### 3. `care-noise-filter` (Logistics & Affection Summarizer)
A structured data extractor designed to process high-velocity social chat logs (e.g., WhatsApp family groups) into actionable "Logistics" and emotional "Affection" tokens, filtering out cognitive noise.
- **Tech:** Python / LLM System Prompting.

### 4. `biometric-keystroke-monitor` (Hydration/Cognitive Telemetry)
Uses keystroke dynamics (inter-key latency) to detect motor slowing. This serves as a non-invasive proxy for early dehydration or cognitive fatigue.
- **Tech:** Vanilla JavaScript / Motor Latency Analytics.

### 5. `acoustic-gait-analyzer` (Pre-Fall Detection)
A digital signal processing (DSP) concept for floor-mic analysis. It identifies the acoustic frequency of "shuffling" feet to predict fall risks before they occur.
- **Tech:** Python / Audio Frequency Analysis.

### 6. `skin-health-analyzer` (Pressure Ulcer & Hydration Monitoring)
A vision-based skin health module that continuously assesses pressure zones, skin hydration (turgor), and discoloration anomalies (pallor, jaundice, cyanosis). Alerts caregivers when high-risk conditions are detected to prevent pressure ulcers and dehydration in bedridden patients.
- **Tech:** Python / Computer Vision (CNN / Color-Space Analysis).

## 📈 Ecosystem Significance (Ecosystem Impact Track)
According to the **Section 2.2** of the Claude for OSS Program, this project serves as a **foundational package** for:
- Health-tech NGOs.
- Non-profit care facilities.
- Independent developers building accessible tools for the elderly.

## 📄 License
MIT License - Open for use by health organizations worldwide.
