import speech_recognition as sr

#This function use audio file as input system
def VoiceToText_audiof(audio_file, output_file):
    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

        try:
            text = r.recognize_google(audio, language="en-EN")
            words = text.split()
            space = ''
            for i in range(0, len(words), 7):
                line = ' '.join(words[i:i + 7])
                space += line + '\n'
            with open(output_file, "w") as file:
                file.write(space)
            return "Output saved to text file: " + output_file
        except sr.UnknownValueError:
            return "Audio not recognized."
        except sr.RequestError:
            return "Could not access Google Web Speech API."


# This function use microphone as input system
def VoiceToText_mic(output_file):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Start talking...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-EN")
        words = text.split()
        space = ''
        for i in range(0, len(words), 7):
            line = ' '.join(words[i:i + 7])
            space += line + '\n'
        with open(output_file, "w") as file:
            file.write(space)
        return "Output saved to text file: " + output_file
    except sr.UnknownValueError:
        return "Audio not recognized."
    except sr.RequestError:
        return "Could not access Google Web Speech API."


# This function is used to choose the input system and printing output
def VoiceToText_output():
    global output
    choice = input("Please choose your input system:\n1. Microphone\n2. Audio File\nPlease make a choice (1 or 2): ")
    output_file = "output.txt"

    if choice == "1":
        output = VoiceToText_mic(output_file)
    elif choice == "2":
        audio_file = input("Please write audio file name: ")
        output = VoiceToText_audiof(audio_file, output_file)
    else:
        output = "Invalid choice."

    print(output)


VoiceToText_output()
