#pip install requests beautifulsoup4 gTTS pygame

import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import pygame
import re
import os

# === Função para extrair texto da web ===
def extrair_texto_da_web(url, seletor_tag='p', limite_paragrafos=5):
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.content, 'html.parser')
    
    paragrafos = soup.find_all(seletor_tag)
    texto_extraido = ' '.join([p.get_text() for p in paragrafos[:limite_paragrafos]])
    
    texto_limpo = re.sub(r'\s+', ' ', texto_extraido).strip()
    return texto_limpo

# === Função para converter texto em áudio com gTTS ===
def texto_para_audio(texto, nome_arquivo="saida_audio.mp3", idioma='pt'):
    tts = gTTS(text=texto, lang=idioma)
    tts.save(nome_arquivo)
    print(f"[✔] Áudio salvo como: {nome_arquivo}")
    return nome_arquivo

# === Função para reproduzir áudio usando pygame ===
def reproduzir_audio(caminho_audio):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho_audio)
    pygame.mixer.music.play()
    print("[🔊] Reproduzindo áudio...")
    while pygame.mixer.music.get_busy():
        continue

# === Execução principal ===
if __name__ == "__main__":
    url = "https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial"

    print("[1] Extraindo texto da página...")
    texto = extrair_texto_da_web(url)
    print(f"Texto extraído (parcial):\n{texto[:300]}...\n")

    print("[2] Convertendo para áudio...")
    caminho_audio = texto_para_audio(texto, "ia_audio.mp3", idioma='pt')

    print("[3] Reproduzindo áudio com pygame...")
    reproduzir_audio(caminho_audio)
