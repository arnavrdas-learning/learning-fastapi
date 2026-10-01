```bash

# 1. Create virtual environment:
python3 -m venv venv

# 2. Activate virtual environment:
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux

# 3. Install dependancies:
pip install -r requirements.txt

# 4. Run server:
uvicorn app.main:app --reload

# Save dependacies:
pip freeze > requirements.txt

# Check python version inside venv:
venv\Scripts\python.exe --version # Windows

# Deactivate virtual environment:
deactivate # Windows


```
