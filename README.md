# Lab 4 Word Game

## Setup (Virtual Environment + Dependencies)

1. Create a virtual environment in the project root:

```powershell
python -m venv .venv
```

2. Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

3. Install required packages from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## How To Run The Game

Run the UI entrypoint:

```powershell
python play.py
```

## How To Run Tests

1. Make sure the virtual environment is activated.
2. Run:

```powershell
pytest
```

## Note

Do not run `python tests/test_main.py` directly if you want full test reporting; use `pytest` instead.
