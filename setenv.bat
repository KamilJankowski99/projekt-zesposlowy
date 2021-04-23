CALL .\Scripts\activate.bat
SET FLASK_APP=project
SET FLASK_DEBUG=1
pip install --upgrade --force-reinstall -r requirements.txt
CALL flask run