import os, sys

base_path = getattr(sys, "_MEIPASS", os.path.dirname(__file__))

# ffmpeg path
ffmpeg_path = os.path.join(base_path, "ffmpeg.exe")

# Playwright browsers path
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(base_path, "playwright-browsers")


import ffmpeg

# ffmpeg_path = "./ffmpeg.exe"

def merge(aud,vid,output):
    video_file = vid
    audio_file = aud
    output_file = f"./outputs/{output}"

    # video_file = "video.mp4"
    # audio_file = "audio.webm"
    # output_file = "./outputs/output.mp4"

    input_video = ffmpeg.input(video_file)
    input_audio = ffmpeg.input(audio_file)

    # if video_file.endswith(".mp4") and audio_file.endswith(".webm"):
    #     ffmpeg.output(input_video, input_audio, output_file, vcodec='copy', acodec='aac').run(cmd=ffmpeg_path)
    #     return
    #
    # if video_file.endswith(".webm") and audio_file.endswith(".m4a"):
    #     ffmpeg.output(input_video, input_audio, output_file, vcodec='copy', acodec='aac').run(cmd=ffmpeg_path)
    #     return

    ffmpeg.output(input_video, input_audio, output_file, vcodec='copy', acodec='copy').run(cmd=ffmpeg_path)

# merge()