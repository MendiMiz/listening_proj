from flask import Flask

from app.db.sql_database import init_db
from app.routes.emails_route import emails_blueprint

app = Flask(__name__)
app.register_blueprint(emails_blueprint, url_prefix="/api/email")


if __name__ == '__main__':
    init_db()
    app.run()

