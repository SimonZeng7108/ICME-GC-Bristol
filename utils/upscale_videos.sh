#!/bin/bash

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg is not installed. Please install it first."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p ICME_GC_MP4_upscaled

# Process all MP4 files in the ICME_GC_MP4 directory
for video in ICME_GC_MP4/*.mp4; do
    # Extract just the filename
    filename=$(basename "$video")
    
    # Get video resolution
    resolution=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$video")
    width=$(echo $resolution | cut -d'x' -f1)
    height=$(echo $resolution | cut -d'x' -f2)
    
    echo "Processing $filename (Current resolution: ${width}x${height})..."
    
    # Check if already 3840x2160
    if [ "$width" -eq 3840 ] && [ "$height" -eq 2160 ]; then
        echo "Skipping $filename - already at target resolution (3840x2160)"
        continue
    fi
    
    # Run the upscaling command to reach 3840x2160
    echo "Upscaling $filename to 3840x2160..."
    ffmpeg -i "$video" -vf "scale=3840:2160:flags=bicubic" "ICME_GC_MP4_upscaled/$filename"
    
    echo "Completed $filename"
done

echo "All videos have been upscaled successfully!" 