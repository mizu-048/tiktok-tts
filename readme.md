# TikTok Text-to-speech API
Inspired by: https://github.com/oscie57/tiktok-voice and https://github.com/Equicord/Equicord/blob/main/src/equicordplugins/vcNarratorCustom/index.tsx

## FOR DOCUMENTATION, VISIT THE [WIKI](https://github.com/mizu/tiktok-tts/wiki)

This is a simple Python program that accesses the TikTok API through a reverse and gives you an `.mp3` file with what it says in the specified voice.

## Usage

To use this, you need Python 3.8+ and all of the required packages installed.

To install required packages, run `pip3 install playsound requests` or `pip3 install -r requirements.txt`
if for some reason you are having errors installing playsound like
× Getting requirements to build wheel did not run successfully.
│ exit code: 1

instead do `pip install playsound==1.2.2`

### Read from file
1. Make sure you have your text in plaintext. You can name it anything
2. Run `py main.py -v VOICE -f FILENAME.txt` (see voices below)

There is no character limit, though only latin characters are supported.

### Read from argument
1. Run `py main.py -v VOICE -t TEXT -n FILENAME.mp3` (see voices below)

This has a 200 character limit, but you can have non-latin characters (as long as it has a TTS supported voice)

### Play from text
Optionally, if you want to listen to the file instead of saving to a file, you can use the `-p` argument to play directly and then delete. If you get error `263`, ignore it, it doesn't affect the program itself.

## Voice Options

**Since the list has gotten quite large, I have moved it to [the wiki](https://github.com/oscie57/tiktok-voice/wiki/Voice-Codes)**

Languages Supported:
- Portuguese (Brazil)
- German
- English (Australia)
- English (United Kingdom)
- English (United States)
- English (Disney)
- Spanish
- Spanish (Mexico)
- French
- Indonesian
- Japanese
- Korean

## Samples

You can find samples of all the voices in [/samples/](https://github.com/mizu-048/tiktok-tts/blob/main/samples/)

## Credits
- Orignal source: https://github.com/oscie57/tiktok-voice
- Reverse Proxy Thing: https://github.com/Equicord/Equicord/blob/main/src/equicordplugins/vcNarratorCustom/index.tsx
