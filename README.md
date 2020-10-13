# financial_assistant

This is simple financial assistant which fixes your finances and you can analyze them

### Work with project

For correct work this service, you need have os `Linux` and bunch `poetry` with `pyenv`, and nex act for configure service correctlu only for Linux with the above bunch .  
After clone project you need execute next acts:
```
pyenv local 3.8.5
poetry install
poetry run python src/__main__.py
```

This project using NoSql database (mongodb), and else it not included, you need execute:
```
sudo systemctl start mongodb
```

### Useful links 
1. [poetry](https://github.com/python-poetry/poetry)
2. [pyenv](https://github.com/pyenv/pyenv)