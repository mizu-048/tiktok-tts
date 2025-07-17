import requests, base64, random, argparse, os, playsound, re, textwrap
from constants import voices  # Make sure this exists or handle fallback

# --- MAIN TTS FUNCTION (uses reverse proxy) ---
def tts(text: str, voice: str = "en_us_001", filename: str = "voice.mp3", play: bool = False):
    if not text.strip():
        print("Error: Text is empty.")
        return

    api_url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice": voice
    }

    try:
        r = requests.post(api_url, headers=headers, json=payload)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    try:
        b64_audio = r.json()["data"]
        audio_data = base64.b64decode(b64_audio)
    except (KeyError, ValueError) as e:
        print("Failed to decode audio from response:", e)
        return

    with open(filename, "wb") as f:
        f.write(audio_data)

    print(f"✅ Audio saved to {filename}")

    if play:
        playsound.playsound(filename)


# --- BATCH MERGE FUNCTION ---
def batch_create(filename: str = 'voice.mp3'):
    with open(filename, 'wb') as out:
        def sorted_alphanumeric(data):
            convert = lambda text: int(text) if text.isdigit() else text.lower()
            alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
            return sorted(data, key=alphanum_key)

        for item in sorted_alphanumeric(os.listdir('./batch/')):
            with open('./batch/' + item, 'rb') as f:
                out.write(f.read())


# --- MAIN SCRIPT ENTRYPOINT ---
def main():
    parser = argparse.ArgumentParser(description="TikTok TTS via reverse proxy")
    parser.add_argument("-v", "--voice", help="the code of the desired voice")
    parser.add_argument("-t", "--text", help="the text to be read")
    parser.add_argument("-f", "--file", help="use this if you wanna use 'text.txt'")
    parser.add_argument("-n", "--name", help="The name for the output file (.mp3)")
    parser.add_argument("-p", "--play", action='store_true', help="use this if you want to play your output")
    args = parser.parse_args()

    # Text source
    if args.file:
        req_text = open(args.file, 'r', encoding='utf-8', errors='ignore').read()
    elif args.text:
        req_text = args.text
    else:
        print('⚠️ You must specify --text or --file')
        return

    # Voice
    text_speaker = args.voice or 'en_us_002'
    if text_speaker == "random":
        text_speaker = randomvoice()

    # Output filename
    filename = args.name or 'voice.mp3'

    # Handle long text (batch)
    if args.file:
        chunk_size = 200
        textlist = textwrap.wrap(req_text, width=chunk_size, break_long_words=True, break_on_hyphens=False)

        batch_dir = './batch/'
        os.makedirs(batch_dir, exist_ok=True)

        for i, item in enumerate(textlist):
            tts(item, text_speaker, f'{batch_dir}{i}.mp3', False)

        batch_create(filename)

        for item in os.listdir(batch_dir):
            os.remove(batch_dir + item)
        os.rmdir(batch_dir)

        return

    # Single TTS
    tts(req_text, text_speaker, filename, args.play)


# --- RANDOM VOICE PICKER ---
def randomvoice():
    return random.choice(voices)


# --- SAMPLE ALL VOICES ---
def sampler():
    for voice in voices:
        print(voice)
        tts("TikTok Text To Speech Sample", voice, f"{voice}.mp3", False)


# --- ENTRY POINT ---
if __name__ == "__main__":
    main()
