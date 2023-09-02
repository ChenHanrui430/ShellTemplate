#!/bin/bash

# Function to check if a file has a video extension
is_video() {
  case "$1" in
    *.ts|*.avi|*.mp4|*.wmv|*.flv|*.mkv|*.rmvb|*.rm|*.mov)
      return 0 # True
      ;;
    *)
      return 1 # False
      ;;
  esac
}

# Check if FFmpeg is installed
if ! command -v ffmpeg &>/dev/null; then
  echo "FFmpeg not found. Please install FFmpeg first."
  exit 1
fi

# Check for the argument (path)
if [ $# -ne 1 ]; then
  echo "Usage: $0 /path/to/videos"
  exit 1
fi

# Get the path to the videos
videos_path="$1"
output_parent_dir=$(dirname "$videos_path")

# Create an "output" directory in the parent directory of the videos
output_dir="$output_parent_dir/output"
mkdir -p "$output_dir"

# Process video files
for file in "$videos_path"/*; do
  if [ -f "$file" ] && is_video "$file"; then
    output_file="$output_dir/$(basename "$file" | sed "s/\.[^.]*$/.mp4/")"

    if [ ! -f "$output_file" ]; then
      ffmpeg -i "$file" -crf 17 "$output_file"
      echo "Converted $file to $output_file"
    else
      echo "Skipped $file (already converted)"
    fi
  fi
done

