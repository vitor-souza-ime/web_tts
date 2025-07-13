
## Overview

`web_tts` is a Python-based application that extracts textual content from web pages and converts it into synthesized speech audio. The system leverages web scraping techniques with Beautiful Soup, text-to-speech conversion using Google Text-to-Speech (gTTS), and audio playback with Pygame. This tool is designed to facilitate digital accessibility and content consumption through automated audio generation from online text.

## Features

- Extracts text from specified HTML tags (default: paragraphs `<p>`) on web pages.
- Cleans and processes extracted text for optimal speech synthesis.
- Converts text to high-quality audio using Google's TTS API.
- Plays the generated audio seamlessly via Pygame.
- Configurable parameters for tag selection and paragraph limits.

## Requirements

- Python 3.6 or higher
- Libraries:
  - requests
  - beautifulsoup4
  - gTTS
  - pygame

## Installation

Install the required packages using pip:

```bash
pip install requests beautifulsoup4 gTTS pygame
````

## Usage

The main script is `main.py`. To run the program, execute the following command:

```bash
python main.py
```

By default, the script extracts text from the Wikipedia page on Artificial Intelligence and converts the first few paragraphs to audio, which is then played back.

### Configuration

* Modify the `url` variable inside `main.py` to change the target web page.
* Adjust `seletor_tag` and `limite_paragrafos` parameters in the `extrair_texto_da_web` function to customize which HTML tags and how many paragraphs are extracted.

## Example

```bash
[1] Extracting text from the page...
Texto extraído (parcial):
Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals...

[2] Converting text to audio...
[✔] Audio saved as: ia_audio.mp3

[3] Playing audio with pygame...
[🔊] Playing audio...
```

## License

This project is licensed under the MIT License.

## Acknowledgments

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
* [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/)
* [Pygame](https://www.pygame.org/)


