#!/usr/bin/env python3
import speech_recognition as sr
import moviepy.editor as mp
from transcript import get_large_audio_transcription
from argparse import ArgumentParser
import os

parser = ArgumentParser()
parser.add_argument(
    "-i",
    "--input",
    dest="input",
    help="The video (MP4) or audio(WAV) file to process.",
    metavar="FILE",
)

args = parser.parse_args()

transcript_only = True

path = "audio.wav"
if not transcript_only:
    print("Generating main audio file.")
    clip = mp.VideoFileClip(args.input)
    clip.audio.write_audiofile(path)

print(
    "Should transcript only? (will not generate audio chunks): {}".format(
        transcript_only
    )
)

generate_chunks = not transcript_only

r = sr.Recognizer()

if generate_chunks is True:
    exit
transcript = get_large_audio_transcription(path, generate_chunks)

filename = "{}_transcript .txt".format(os.path.basename(args.input).replace("\\", ""))

with open(filename, mode="w") as file:
    file.write(transcript)
    print("ready!")
