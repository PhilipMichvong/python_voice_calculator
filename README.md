# Instrukcje instalacji projektu

## Krok 1: Pobierz kod źródłowy

Sklonuj repozytorium z kodem źródłowym na swój lokalny komputer:

```bash
git clone https://adres_repozytorium.git
```

```
cd nazwa_projektu
```

## Krok 2: Utwórz wirtualne środowisko

Utwórz wirtualne środowisko, aby izolować zależności projektu. Możesz użyć venv lub virtualenv. Przykład z użyciem venv:

```bash
python -m venv venv

```

## Krok 3: Aktywuj wirtualne środowisko:

Dla systemu Windows:

```bash
venv\Scripts\activate
```

Dla systemu Unix lub MacOS:

```
source venv/bin/activate

```

## Krok 4: Zainstaluj zależności

Użyj pliku requirements.txt, aby zainstalować wszystkie niezbędne zależności:

```bash
pip install -r requirements.txt
```

## Krok 4: Uruchom projekt

Teraz możesz uruchomić swój projekt. Upewnij się, że wirtualne środowisko jest aktywowane, a następnie:

```bash
python main.py
```

To wszystko! Teraz powinieneś mieć projekt uruchomiony z izolowanymi zależnościami w wirtualnym środowisku.

Upewnij się, że zmienisz `https://adres_repozytorium.git` i `nazwa_projektu` na odpowiedni
