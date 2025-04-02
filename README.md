# SRT Encoder

This project provides a simple script to embed subtitles (`.srt` files) into video files using `ffmpeg`.

## Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Build the development container or install dependencies manually:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script to embed subtitles into a video:
```sh
python src/encode_srt.py <input_video> <input_srt> <output_video>
```

### Example:
```sh
python src/encode_srt.py input.mp4 subtitles.srt output.mp4
```

## Requirements
- Python 3.11+
- `ffmpeg`
- Dependencies from `requirements.txt`

## License
MIT License
