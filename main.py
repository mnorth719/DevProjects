import os

from flask import Flask, render_template, request

from database import repo_service
from services.mail_service import Actions as mail_service

template_location = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__, template_folder=template_location, static_url_path='/static')


@app.route("/")
def index():
    repos = repo_service.Actions.get_all_repositories()
    return render_template('index.html', repos=repos)


@app.route("/mail", methods=['POST'])
def mail():
    name = request.form.get('name', None)
    phone = request.form.get('phone', None)
    email = request.form.get('email', None)
    message = request.form.get('message', None)
    mail_service.send(name, phone, email, message)
    return 'OK'


if __name__ == "__main__":
    from database.manager import check_db_exists

    # Test purposes
    check_db_exists()
    app.run()
