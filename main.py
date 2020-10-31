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
parser.add_argument(
    "-o",
    "--output",
    dest="output",
    help="Path and filename where the output should be stored.",
    metavar="FILE",
)

args = parser.parse_args()

# Means the audio file will not be reprocessed in case you are just tweaking the params for the audio translation.
transcript_only = False


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

filename = args.output

with open(filename, mode="w") as file:
    file.write(transcript)
    print("ready!")
