import argparse
import sys
import wave
import struct

parser = argparse.ArgumentParser()
parser.add_argument('--voice')
parser.add_argument('--output')
args = parser.parse_args()

text = sys.stdin.read()
words = len(text.split())
# 150 wpm -> 2.5 words per sec
duration_sec = words / 2.5
if duration_sec < 1: duration_sec = 1.0
frames = int(44100 * duration_sec)

print(f'Mocking VO to {args.output} ({duration_sec}s)')

with wave.open(args.output, 'wb') as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    # Write silence chunked to avoid large memory
    chunk = struct.pack('<h', 0) * 44100
    written = 0
    while written < frames:
        to_write = min(44100, frames - written)
        f.writeframesraw(chunk[:to_write*2])
        written += to_write

