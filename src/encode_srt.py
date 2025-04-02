import ffmpeg
import sys

def encode_srt(video_file, srt_file, output_file):
    (
        ffmpeg
        .input(video_file)
        .output(output_file, vf=f'subtitles={srt_file}')
        .run()
    )

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python encode_srt.py <input_video> <input_srt> <output_video>")
        sys.exit(1)
    
    encode_srt(sys.argv[1], sys.argv[2], sys.argv[3])

