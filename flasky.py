# -*- coding: UTF-8 -*-
__author__ = 'hunter'
from flask_migrate import Migrate
import os
from app import create_app, db

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
migrate = Migrate(app, db)


# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Role=Role)
#
#
# @app.cli.command()
# @click.argument('test_names', nargs=-1)
# def test(test_names):
#     """Run the unit tests."""
#     import unittest
#     if test_names:
#         tests = unittest.TestLoader().loadTestsFromNames(test_names)
#     else:
#         tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    os.putenv("simple-flask-web-env", "dev")
    app.run()
