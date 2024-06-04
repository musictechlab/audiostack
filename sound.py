import audiostack
import os
from dotenv import load_dotenv

load_dotenv()

# First, paste your API key inside the quotation marks below:
audiostack.api_key = os.environ.get('AUDIOSTACK_API_KEY')

# This code example demonstrates functionality from the Content, Speech, Production and Delivery parts of the AudioStack API.
# Using the API, you can create production-ready audio assets in minutes.

# In Content, you can create scripts and manage your production assets.
script = """
<as:section name="main" soundsegment="main">
Music Tech Conference Bergen is an event dedicated for the music technology industry, where experts and enthusiasts can network, share insights, and learn about the latest developments.
If want to learn more about software development in Music Tech, or establish a new partnership with Bravelab, read more here bravelab.io/bergen</as:section>
"""


names = ["Cosmo"] # Add names to the list to generate multiple audio files using different voices
presets = ["musicenhanced"]
templates = ["sound_affects"]

print("Creating the script...")
script = audiostack.Content.Script.create(
    scriptText=script, scriptName="test", projectName="mastering_test"
)

for name in names:
    # In Speech, you can access top quality AI voice models, or use your own cloned voice.
    print(f"Synthesizing speech for {name}")
    speech = audiostack.Speech.TTS.create(scriptItem=script, voice=name, speed=1)
    for template in templates:
        for preset in presets:
            # In Production, you can dynamically mix content, apply sound designs and master your audio so that it sounds as professional as possible.
            print(
                f"Mixing the speech with template `{template}` using `{preset}` preset"
            )
            mix = audiostack.Production.Mix.create(
                speechItem=speech,
                soundTemplate=template,
                masteringPreset=preset,
            )
            # Now you can download the wav file, or use the Delivery API to encode it to another format.
            print("Downloading the wav file...")
            file_name = f"V1_{name}_{template}_{preset}"
            mix.download(fileName=file_name)
            current_directory = os.path.dirname(os.path.abspath(__file__))
            print(f"File downloaded to: {current_directory}/{file_name}.wav")

            # In Delivery, you can encode your audio to a variety of formats, and host it on our server!
            delivery = audiostack.Delivery.Encoder.encode_mix(
                productionItem=mix,
                preset="mp3_high",
                public=True,
            )
            print("MP3 file URL:", delivery.url)