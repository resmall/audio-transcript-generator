#!/usr/bin/env python3
import moviepy.editor as mp
from transcript import get_large_audio_transcription
from argparse import ArgumentParser
import os


def get_file_extension(file_path):
    filename, file_extension = os.path.splitext(file_path)
    return file_extension


def is_video_file(file_path):
    file_extension = get_file_extension(args.input)
    print("File extension" + file_extension)
    return True if file_extension == ".mp4" else False


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
path = "audio.wav"
transcript = ""
if is_video_file(args.input):
    print("Is video.")
    clip = mp.VideoFileClip(args.input)
    clip.audio.write_audiofile(path)
    transcript = get_large_audio_transcription(path, True)
else:
    transcript = get_large_audio_transcription(path, False)

filename = args.output

with open(filename, mode="w") as file:
    file.write(transcript)
    print("ready!")
