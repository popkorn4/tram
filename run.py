import sys
from os import path as p


from flask_script import Manager, Server
from App import app

manager = Manager(app)

manager.add_command("runserver", Server(
                                    use_debugger = True,
                                    use_reloader = True,
                                    port = 5002)
)

if  __name__ == "__main__":
    manager.run()