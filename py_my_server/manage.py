# coding:utf-8
from flask_script import Manager
from hello_rubbish import create_app, db
from flask_migrate import Migrate, MigrateCommand

app = create_app("dev")
manage = Manager(app)
Migrate(app, db)
manage.add_command("db", MigrateCommand)

# python3 manage.py runserver -h0.0.0.0 -p5000
if __name__ == "__main__":
    manage.run()
