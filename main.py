from flask import Flask, render_template
from database import repo_service
import os
template_location = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__, template_folder=template_location, static_url_path='/static')


@app.route("/")
def index():
    repos = repo_service.Actions.get_all_repositories()
    return render_template('index.html', repos=repos)


if __name__ == "__main__":
    from database.manager import check_db_exists

    # Test purposes
    check_db_exists()
    app.run()
