import speech_recognition as sr
import pyttsx3
import http.client
import os


class VoiceAssistant:
    def __init__(self, name="Assistant"):
        self.name = name
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.meteostat_api_key = os.environ.get('METEOSTAT_API_KEY',
                                                '5e1ecabc66msh694b39570340884p13dccdjsn1e9bc0e24113')
        self.google_news_api_key = os.environ.get('GOOGLE_NEWS_API_KEY',
                                                  '5e1ecabc66msh694b39570340884p13dccdjsn1e9bc0e24113')

        # Configure text-to-speech
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Select female voice (optional)
        self.engine.setProperty('rate', 175)  # Adjust speech rate

        # Calibrate for ambient noise
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

        print(f"{self.name} initialized and ready.")
        self.speak(f"Hello, I'm {self.name}, your personal voice assistant. How can I assist you?")

    def speak(self, text):
        """Convert text to speech."""
        print(f"{self.name}: {text}")  # Output as text
        self.engine.say(text)  # Output as speech
        self.engine.runAndWait()

    def listen(self):
        """Listen for a command."""
        with self.microphone as source:
            print("Listening...")
            try:
                # Adding a timeout to prevent infinite blocking
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.WaitTimeoutError:
                print("Listening timed out waiting for a command.")
                self.speak("I didn't hear anything. Could you please say that again?")
                return ""
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
                self.speak("Sorry, I didn't understand that.")
                return ""
            except sr.RequestError:
                print("Speech recognition service is unavailable.")
                self.speak("Speech recognition service is currently unavailable.")
                return ""

    def get_meteostat_weather(self, lat, lon, start, end):
        """Get historical weather data from Meteostat API."""
        print("Fetching historical weather data...")
        self.speak("Fetching historical weather data now.")
        try:
            conn = http.client.HTTPSConnection("meteostat.p.rapidapi.com")
            headers = {
                'x-rapidapi-key': self.meteostat_api_key,
                'x-rapidapi-host': "meteostat.p.rapidapi.com"
            }

            endpoint = f"/point/monthly?lat={lat}&lon={lon}&start={start}&end={end}"
            conn.request("GET", endpoint, headers=headers)
            res = conn.getresponse()
            data = res.read()
            weather_data = data.decode("utf-8")

            print(f"Weather data: {weather_data}")
            self.speak("The historical weather data has been fetched. Check your terminal for details.")
        except Exception as e:
            error_message = f"Error fetching Meteostat data: {e}"
            print(error_message)
            self.speak(error_message)

    def get_google_news(self):
        """Get the latest business news from Google News API."""
        print("Fetching Google News headlines...")
        self.speak("Fetching Google News headlines now. Please wait.")
        try:
            conn = http.client.HTTPSConnection("google-news13.p.rapidapi.com")
            headers = {
                'x-rapidapi-key': self.google_news_api_key,
                'x-rapidapi-host': "google-news13.p.rapidapi.com"
            }

            conn.request("GET", "/business?lr=en-US", headers=headers)
            res = conn.getresponse()
            data = res.read()
            news_data = data.decode("utf-8")

            print(f"News headlines: {news_data}")
            self.speak("The latest business news headlines have been fetched. Check your terminal for details.")
        except Exception as e:
            error_message = f"Error fetching Google News data: {e}"
            print(error_message)
            self.speak(error_message)

    def run(self):
        """Main loop to run the assistant."""
        self.speak("I am ready and listening for your commands.")
        try:
            while True:
                command = self.listen()  # Listen for a command
                if "weather" in command:
                    # Example command: "get weather"
                    self.get_meteostat_weather(52.5244, 13.4105, "2020-01-01", "2020-12-31")
                elif "news" in command:
                    # Example command: "get news"
                    self.get_google_news()
                elif "exit" in command or "quit" in command:
                    print("Exiting the program. Goodbye!")
                    self.speak("Goodbye! Have a great day!")
                    break
                else:
                    print("Command not recognized. Please try again.")
                    self.speak("I didn't quite catch that. Could you please repeat the command?")
        except KeyboardInterrupt:
            print("\nProgram terminated by user. Cleaning up...")
            self.speak("Goodbye! Have a great day!")


if __name__ == "__main__":
    assistant = VoiceAssistant("Jarvis")
    assistant.run()
