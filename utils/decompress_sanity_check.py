#!/usr/bin/env python3
import os
import subprocess
import json
from pathlib import Path

def get_video_info(video_path):
    """Get video information using ffprobe."""
    cmd = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_format',
        '-show_streams',
        video_path
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error analyzing {video_path}: {e}")
        return None

def check_yuv_conversion(original_dir, yuv_dir):
    """Check if videos in original_dir are losslessly converted to YUV in yuv_dir."""
    original_dir = Path(original_dir)
    yuv_dir = Path(yuv_dir)
    
    # Get list of original videos
    original_videos = list(original_dir.glob('**/*.mp4'))
    if not original_videos:
        original_videos = list(original_dir.glob('**/*.mkv'))
    
    if not original_videos:
        print(f"No video files found in {original_dir}")
        return
    
    print(f"Found {len(original_videos)} videos in {original_dir}")
    
    # Check each original video
    missing_yuv = []
    potentially_lossy = []
    
    for orig_video in original_videos:
        # Determine expected YUV filename
        rel_path = orig_video.relative_to(original_dir)
        expected_yuv = yuv_dir / rel_path.with_suffix('.yuv')
        
        # Check if YUV file exists
        if not expected_yuv.exists():
            missing_yuv.append(str(rel_path))
            continue
        
        # Get video information
        orig_info = get_video_info(orig_video)
        if not orig_info:
            continue
        
        # For YUV files, we need to check dimensions and pixel format differently
        # since ffprobe might not work directly on raw YUV files
        
        # Check file size as a basic sanity check
        # YUV files are typically larger than compressed videos
        orig_size = orig_video.stat().st_size
        yuv_size = expected_yuv.stat().st_size
        
        if yuv_size <= orig_size:
            potentially_lossy.append(str(rel_path))
            print(f"Warning: {rel_path} - YUV file size ({yuv_size}) is smaller than original ({orig_size})")
    
    # Print results
    if missing_yuv:
        print(f"\nMissing YUV files ({len(missing_yuv)}):")
        for video in missing_yuv:
            print(f"  - {video}")
    
    if potentially_lossy:
        print(f"\nPotentially lossy conversions ({len(potentially_lossy)}):")
        for video in potentially_lossy:
            print(f"  - {video}")
    
    if not missing_yuv and not potentially_lossy:
        print("\nAll videos appear to be losslessly converted to YUV format.")

def check_ffmpeg_conversion_command():
    """Check if the ffmpeg command used for conversion was lossless."""
    # This would require checking logs or history
    # For now, we'll just provide the recommended lossless command
    print("\nRecommended lossless ffmpeg conversion command:")
    print("ffmpeg -i input.mp4 -c:v rawvideo -pixel_format yuv420p output.yuv")
    print("\nNote: To verify the exact command used, check your conversion script or command history.")

if __name__ == "__main__":
    # Paths to video directories
    original_dir = "ICME_Dataset/train_videos"
    yuv_dir = "ICME_Dataset/train_videos_yuv"
    
    print("Checking YUV conversion...")
    check_yuv_conversion(original_dir, yuv_dir)
    check_ffmpeg_conversion_command()
