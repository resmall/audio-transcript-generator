#!/usr/bin/env python3
import speech_recognition as sr
import moviepy.editor as mp
from transcript import get_large_audio_transcription
from argparse import ArgumentParser
import time


parser = ArgumentParser()
parser.add_argument(
    "-i",
    "--input",
    dest="input",
    help="The video (MP4) or audio(WAV) file to process.",
    metavar="FILE",
)
# parser.add_argument(
#     "-o",
#     "--output",
#     dest="output_directory",
#     help="The output directiory where the transcript should be stored.",
#     metavar="FOLDER",
# )

args = parser.parse_args()

path = "audio.wav"
clip = mp.VideoFileClip(args.input)
clip.audio.write_audiofile(path)

r = sr.Recognizer()

transcript = get_large_audio_transcription(path)

filename = "recognized_{}.txt".format(time.strftime("%s", time.gmtime()))

with open(filename, mode="w") as file:
    file.write(transcript)
    print("ready!")

# Small file
# audio = sr.AudioFile(args.output)
# with audio as source:
#     audio_file = r.record(source)
# result = r.recognize_google(audio_file)

# with open("recognized.txt", mode="w") as file:
#     file.write("Recognized Speech:")
#     file.write("\n")
#     file.write(result)
#     print("ready!")
