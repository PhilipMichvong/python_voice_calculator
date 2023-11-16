import speech_recognition as sr
import pyttsx3


class Recognizer:
    def __init__(self):
        pass

    def Listening(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                actions = ["dodawanie", "odejmowanie", "mnożenie", "dzielenie"]
                self.speak_in_polish(
                    f"wybierz jedną z akcji: {actions} lub pomoc - aby uzyskac pomoc")

                while True:
                    audio = recognizer.listen(source, timeout=3)
                    action = recognizer.recognize_google(
                        audio, language='pl-PL')
                    action = action.lower()  # Zamień na małe litery

                    if action == "pomoc":
                        self.print_help()
                        continue  # Wróć do oczekiwania na komendę
                    if action == "koniec":
                        return 0

                    print(f"Wybrana akcja: {action}")

                    if action not in actions:
                        print(
                            f"Nie rozpoznano poprawnie, wybierz jedną z akcji: {actions}")
                        continue  # Wróć do oczekiwania na poprawną komendę

                    self.speak_in_polish("Podaj pierwszą liczbę")
                    audio = recognizer.listen(source, timeout=5)
                    num1 = self.parse_number(
                        recognizer.recognize_google(audio, language='pl-PL'))
                    if num1 is not None:
                        print(f"Pierwsza liczba: {num1}")
                        self.speak_in_polish("Podaj drugą liczbę")
                        audio = recognizer.listen(source, timeout=5)
                        num2 = self.parse_number(
                            recognizer.recognize_google(audio, language='pl-PL'))

                    if num2 is not None:
                        print(f"Druga liczba: {num2}")
                        result = self.perform_operation(action, num1, num2)
                        if result is not None:
                            self.speak_in_polish(f"Wynik: {result}")
                    else:
                        print("Nie rozpoznano drugiej liczby poprawnie.")

            except sr.WaitTimeoutError:
                print("Czas na nagranie liczb minął. Spróbuj ponownie.")
            except sr.UnknownValueError:
                print("Nie udało się rozpoznać mowy (liczby).")
            except sr.RequestError as e:
                print(f"Nie udało się obsłużyć zapytania, błąd: {e}")

    def parse_number(self, text):
        try:
            # Zamień ewentualny przecinek na kropkę
            return float(text.replace(",", "."))
        except ValueError:
            try:
                return self.polish_word_to_number(text)
            except ValueError:
                print(f"Nie udało się zinterpretować liczby: {text}")
                return None

    def polish_word_to_number(self, word):
        word = word.lower()
        numbers_dict = {
            'jeden': 1,
            'dwa': 2,
            'trzy': 3,
            'cztery': 4,
            'pięć': 5,
            'sześć': 6,
            'siedem': 7,
            'osiem': 8,
            'dziewięć': 9
        }
        return numbers_dict.get(word, None)

    def perform_operation(self, action, num1, num2):
        if action in ['dodawanie', 'dodawania']:
            return num1 + num2
        elif action in ["odejmowanie", 'odejmowania']:
            return num1 - num2
        elif action in ["mnożenie", "mnożenia"]:
            return num1 * num2
        elif action in ["dzielenie", "dzielenia"]:
            if num2 == 0:
                print("Nie można dzielić przez zero!")
                return None
            return num1 / num2
        elif action == "koniec":
            return 1

    def print_help(self):
        print("Komendy dostępne w programie:")
        print(" - Dodawanie")
        print(" - Odejmowanie")
        print(" - Mnożenie")
        print(" - Dzielenie")
        print(" - Pomoc (aby wyświetlić tę listę)")

    def speak_in_polish(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('voice', 'pl')
        engine.say(text)
        engine.runAndWait()
        print(text)


def main():
    recognize = Recognizer()
    recognize.Listening()


if __name__ == "__main__":
    main()
