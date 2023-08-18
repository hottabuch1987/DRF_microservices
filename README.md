### Project
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Микросервисы+на+Django+REST+framework+ )](https://git.io/typing-svg)

### Start
python3 -m venv venv
#
source venv/bin/activate
#
pip install -r requirements.txt

### for each microservice
python manage.py makemigrations
#
python manage.py migrate
#
python manage.py createsuperuser
#
python manage.py runserver
