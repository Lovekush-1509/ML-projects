import numpy as np
import sounddevice  as sd
from scipy.fft import fft
import time

# Parameters
DURATION = 1  # Duration of each recording in seconds
SAMPLE_RATE = 44100  # Sampling rate in Hz
LOW_THRESHOLD = 0.01  # Threshold for low sound level
MEDIUM_THRESHOLD = 0.03  # Threshold for medium sound level

def calculate_rms(audio_data):
    """Calculate the RMS (Root Mean Square) of audio data to measure sound level."""
    return np.sqrt(np.mean(audio_data**2))

def classify_sound_level(rms_value):
    """Classify sound level based on RMS value."""
    if rms_value < LOW_THRESHOLD:
        return "Low"
    elif rms_value < MEDIUM_THRESHOLD:
        return "Medium"
    else:
        return "High"

def detect_sound_level():
    print("Starting Real-Time Sound Level Detection. Press Ctrl+C to stop.")
    try:
        while True:
            # Record audio for a specified duration
            audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
            sd.wait()  # Wait for the recording to complete
            # audio_path = 'Downloads\JVSTIN - CLANDESTINA (Slowed - Reverb) [TubeRipper.com].mp3'
            # audio_data, sample_rate = librosa.load(audio_path, sr=44100)
            
            # Convert to a 1D numpy array
            audio_data = audio_data.flatten()
            
            # Calculate RMS value
            rms_value = calculate_rms(audio_data)
            
            # Classify sound level
            sound_level = classify_sound_level(rms_value)
            
            # Output the result
            print(f"Sound Level: {sound_level} (RMS: {rms_value:.5f})")
            
            # Sleep briefly before the next recording
            time.sleep(0.5)
    
    except KeyboardInterrupt:
        print("\nReal-Time Sound Level Detection stopped.")

# Run the sound level detection
detect_sound_level()
