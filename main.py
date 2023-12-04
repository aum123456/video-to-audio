from moviepy.editor import VideoFileClip

def convert_video_to_mp3(video_file, output_folder='ssup_boii'):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the video file
    video_clip = VideoFileClip(video_file)

    # Extract the audio
    audio_clip = video_clip.audio

    # Define the output MP3 file path
    output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(video_file))[0]}.mp3")

    # Write the audio to an MP3 file
    audio_clip.write_audiofile(output_file)

    # Close the clips
    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    import os

    # Specify the folder containing (ONLY!!) the video files
    video_folder = r'C:\Users\Aum Patil\Desktop\video-folder'

    # Specify the output folder for MP3 files
    output_folder = r'C:\Users\Aum Patil\Desktop\audio-folder'

    # Get a list of all video files in the folder
    video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.mkv', '.avi'))]

    # Convert each video to MP3
    for video_file in video_files:
        try:
            video_file_path = os.path.join(video_folder, video_file)
            convert_video_to_mp3(video_file_path, output_folder)
        except:
            print('Skipping this file due to some error.')
            continue