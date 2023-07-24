from moviepy.editor import VideoFileClip
import assemblyai as aai

def extract_audio_from_video(video_path, output_audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)

if __name__ == "__main__":
    input_video_path = "videoplayback.mp4"  # Replace with the actual path to your video
    output_audio_path = "output_audio.wav"
    output_text_path = "output_text.txt"

    # Step 1: Extract audio from video
    extract_audio_from_video(input_video_path, output_audio_path)
    print("Audio extracted successfully!")

    # Step 2: Transcribe audio using AssemblyAI
    aai.settings.api_key = ""
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("output_audio.wav")

    # Step 3: Save the text to a file
    with open(output_text_path, "w") as text_file:
        text_file.write(transcript.text)

    print("Text extracted and saved to output_text.txt.")
