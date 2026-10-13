# Disability Assistance System

Dispozitiv purtabil (pe piept sau în rucsac) care ajută persoanele cu deficiențe de vedere să afle ce obiecte sunt în fața lor și cât de departe se află, prin anunțuri audio. Proiect de licență, TST Multimedia, UPT.

**Stare:** în lucru. Funcțiile de mai jos sunt ținta proiectului, nu tot ce există deja.

## Funcții țintă

- Detecție de obiecte în timp real (YOLO11n)
- Tracking: fiecare obiect primește un ID și este anunțat o singură dată
- Estimare de distanță (din dimensiunea obiectului în imagine, plus senzor ToF VL53L1X)
- Feedback audio în română, rulat într-un fir separat, cu praguri de alertă
- Funcționare complet offline pe Raspberry Pi 4

## Hardware

- Raspberry Pi 4 Model B (4 GB)
- Cameră USB
- Senzor ToF VL53L1X (I2C)
- Căști sau difuzor mic
- Powerbank 5 V / 3 A, radiator + ventilator

## Structura repository-ului

```
src/        codul Python
models/     modele (nu se urcă pe GitHub dacă sunt mari)
docs/       scheme, poze, note
tests/      clipuri video de test și scripturi de test
requirements.txt
```

## Rulare pe laptop (dezvoltare)

```bash
git clone <linkul repository-ului>
cd disability-assistance-system
python -m venv .venv
# Windows:  .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate
pip install -r requirements.txt
```

Pe laptop se dezvoltă și se testează logica (detecție, tracking, praguri, audio) pe cameră sau pe clipuri înregistrate. Senzorul ToF și butonul GPIO există doar pe Pi, deci pe laptop se simulează.

## Rulare pe Raspberry Pi 4

```bash
sudo apt install git python3-venv
git clone <linkul repository-ului>
cd disability-assistance-system
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Activează I2C din `sudo raspi-config` (Interface Options) pentru senzorul ToF. Viteza (FPS) se măsoară întotdeauna pe Pi, nu pe laptop.

Comanda de pornire va fi adăugată aici când există `src/main.py`.

## Plan

1. Detecție și măsurarea FPS pe Pi
2. Tracking și zone stânga / centru / dreapta
3. Audio
4. Distanță (bounding box + ToF)
5. Montaj hardware
6. Evaluare
7. Redactarea lucrării

## Licență

MIT (vezi `LICENSE`). Atenție: Ultralytics YOLO este sub licență AGPL-3.0; verifică implicațiile dacă publici codul.
