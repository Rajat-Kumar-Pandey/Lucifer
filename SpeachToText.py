# pip install SpeechRecognition==3.8.1

import speech_recognition as sr
import os
import threading
#pip install mtranslate
from mtranslate import translate
from colorama import Fore,Style,init

init(autoreset=True)
def print_loop():
    # while True:
        print(Fore.GREEN + "I am Lucifer... Ready to Serv You" , end="" , flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        
def Translate_hindi_to_engligh(text):
    english_text = translate(text,"en-us")
    return english_text
def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False     #slow down other voice
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 2
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 2
    recognizer.non_speaking_duration = 2
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "I am Lucifer... Ready to Serv You" , end="" , flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r" + Fore.CYAN + "Recongnize..." , end="", flush=True)
                recognizer_text = recognizer.recognize_google(audio).lower()
                if recognizer_text:
                    trans_text = Translate_hindi_to_engligh(recognizer_text)
                    print("\r" + Fore.LIGHTMAGENTA_EX + "Rajat : " + trans_text)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognizer_text = ""
            finally:
                print("\r" , end="" , flush=True)
            
            os.system("cls" if os.name == "nt" else "clear")
        stt_thread = threading.Thread(target=Speech_To_Text_Python)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()

Speech_To_Text_Python()
        