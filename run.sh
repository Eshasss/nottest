python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
uvicorn uvicorn src.main:app --reload