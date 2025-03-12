import os
import subprocess
import multiprocessing
from tqdm import tqdm


def convert_video(args):
    """
    Convert a single video to YUV format.
    Function designed to be used with multiprocessing.
    """
    video_path, yuv_output_path, is_hdr = args
    
    file = os.path.basename(video_path)
    
    # Build the appropriate ffmpeg command based on video type
    if is_hdr:
        cmd = [
            "ffmpeg", "-i", video_path, 
            "-pix_fmt", "yuv420p10le", 
            "-c:v", "rawvideo", 
            yuv_output_path
        ]
        print(f"Converting HDR video {file} to {yuv_output_path} with yuv420p10le format...")
    else:
        cmd = [
            "ffmpeg", "-i", video_path, 
            "-pix_fmt", "yuv420p", 
            "-c:v", "rawvideo", 
            yuv_output_path
        ]
        print(f"Converting SDR video {file} to {yuv_output_path} with yuv420p format...")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error converting {file}: {result.stderr}"
    else:
        return f"Successfully converted {file} to {yuv_output_path}."


def convert_videos_to_yuv(input_dir, output_dir):
    """
    Converts all video files in the specified directory to YUV format.
    Uses different ffmpeg commands for HDR and SDR videos.
    Processes videos in parallel using multiprocessing.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Prepare arguments for parallel processing
    conversion_args = []
    
    for file in os.listdir(input_dir):
        # Process only files with video extensions
        if file.endswith((".mp4", ".mkv")):  # Add more extensions if needed
            video_path = os.path.join(input_dir, file)
            video_name, _ = os.path.splitext(file)
            yuv_output_path = os.path.join(output_dir, f"{video_name}.yuv")
            
            # Determine if the video is HDR or SDR based on filename
            is_hdr = "HDR" in file
            
            # Add to arguments list
            conversion_args.append((video_path, yuv_output_path, is_hdr))
    
    # Determine the number of processes to use (use 75% of available cores)
    num_processes = max(1, int(multiprocessing.cpu_count() * 0.75))
    print(f"Using {num_processes} processes for parallel conversion")
    
    # Process videos in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = list(tqdm(
            pool.imap(convert_video, conversion_args),
            total=len(conversion_args),
            desc="Converting videos"
        ))
    
    # Print results
    for result in results:
        print(result)


if __name__ == "__main__":
    # Input and output directories
    input_directory = "ICME_Dataset/train_videos"
    output_directory = "ICME_Dataset/train_videos_yuv"
    convert_videos_to_yuv(input_directory, output_directory)
