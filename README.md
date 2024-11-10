# Real-Time Sound Level Detection

This Python project detects and classifies sound levels (Low, Medium, High) in real-time using a microphone. The code leverages `sounddevice` for audio input, along with `numpy` and `scipy` for signal processing.

## Features
- **Real-Time Detection**: Analyzes audio input continuously.
- **Sound Classification**: Classifies sound levels based on RMS (Root Mean Square) thresholds.
- **Adjustable Parameters**: Customize duration, sample rate, and thresholds as needed.

## Requirements
- Python 3.x
- `numpy`, `scipy`, and `sounddevice` Python libraries
- `PortAudio` library (required by `sounddevice`)


### Step 1: Clone the Repository
```bash
git clone https://github.com/Lovekush-1509/ML-projects.git
cd ML-projects
```


## Install Python Dependencies
```
pip install numpy sounddevice scipy
```

## Running the Project
```
python sound_detection.py
 ```
