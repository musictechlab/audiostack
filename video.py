import audiostack
import os
from dotenv import load_dotenv

load_dotenv()

audiostack.api_key = os.environ.get('AUDIOSTACK_API_KEY')


print(f"Combining video with your voiceover...")
def combine_audio(video, audio):
    if (audio):
        os.system(
            f"""ffmpeg \
                -i {video} -i {audio} \
                -c:v copy \
                -map 0:v -map 1:a \
                -shortest \
                -y assets/output.mp4""")

def create_video():
        VOICE="cosmo"
        try:     
            combine_audio("assets/in-video-test.mp4", "assets/in-sound.wav")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    create_video()
