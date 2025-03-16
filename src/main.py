from src.polly_tts import synthesize_speech

def main():
    text = "Hallo, ich bin AWS Polly. Wie geht es Ihnen?"
    synthesize_speech(text)

if __name__ == "__main__":
    main()