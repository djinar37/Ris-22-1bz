import pyaudio
import wave
from gpiozero import LED
import random
import time

LED_PINS = [14, 15, 23, 24, 21]
leds = [LED(pin) for pin in LED_PINS]

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("vois on")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("vois off")

stream.stop_stream()
stream.close()
audio.terminate()

with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"fille {WAVE_OUTPUT_FILENAME}")

random_led = random.choice(leds)
random_led.on()

print(f" on {random_led.pin.number}")

time.sleep(2)
random_led.off()

