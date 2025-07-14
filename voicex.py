import os
import pyttsx3
import subprocess
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def shutdown():
    if os.name == "nt":
        # For Windows operating system
        speak("Windows turning off")
        os.system("shutdown /s /t 5")

    elif os.name == "posix":
        # For Unix/Linux/Mac operating systems
        speak("Windows turning off")
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported operating system.")


def restart():
    if os.name == "nt":
        # For Windows operating system
        speak("Windows Restarting")
        os.system("shutdown /r /t 0")
    elif os.name == "posix":
        # For Unix/Linux/Mac operating systems
        speak("Windows Restarting")
        os.system("sudo shutdown -r now")
    else:
        print("Unsupported operating system.")


def go_to_ex():
    subprocess.Popen(["explorer.exe", "/e", "/select,", "Desktop"])
    speak("Opening your desktop in explorer")


def go_to_pc():
    subprocess.Popen(r"cmd /c start shell:MyComputerFolder")
    speak("Opening your pc")

def log_off():
    """Log off the current user."""
    speak("Windows logoff initiated")
    os.system("shutdown -l")


amazon = "https://www.amazon.com"
google = "https://www.google.com"
youtube = "https://www.youtube.com/"

print("1. Shutdown")
print("2. Restart")
print("3. log off...")
print("4. Go to file explorer...")
print("5. open google")
print("6. open amazon")
print("7. open pc")
print("8. open youtube")
# if _name_ == "_main_":
speak("Hello, we are team voiceX, how can I help you?")

# Record the audio
with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

    try:
        # Using google speech recognition
        text = r.recognize_google(audio, language="en-in")
        print("You said: ", text)

        if text.lower() == "shutdown":
            shutdown()
        elif text.lower() == "restart":
            restart()
        elif text.lower() == "log off":
            log_off()
        elif text.lower() == "go to file explorer":
            go_to_ex()
        elif text.lower() == "open pc":
            go_to_pc()
        elif text.lower() == "open google":
            speak("opening google")
            webbrowser.open(google)
        elif text.lower() == "open amazon":
            speak("opening amazon")
            webbrowser.open(amazon)
        elif text.lower() == "open youtube":
            speak("opening youtube")
            webbrowser.open(youtube)

        else:
            print("Invalid command. Please say 'shutdown', 'restart', 'log off', 'go to file explorer', 'open pc', 'open google', or 'open amazon'.")

    except Exception as e:
        speak("say that again")
        print("Say that again please...")
