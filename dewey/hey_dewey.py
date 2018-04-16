#! /usr/bin/env python
"""Dewey, our friendly CLI friend!

Usage:
  dewey workon <app_name>
  dewey (checkout | co) <branch_name>
  dewey (new-branch | nb) <branch_name>
  dewey dev-setup
  dewey up
  dewey sync
  dewey pull
  dewey restart
  dewey bash
  dewey build
  dewey android
  dewey ios
  dewey setup
  dewey reset
  dewey syncdb
  dewey test
  dewey init
  dewey hi
  dewey upgrade

Options:
  -h --help     Show this screen.
  --version     Show version.

Hidden commands for scripts:
  --pre         Output the pre-command scripts for execution.
  --post        Output the post-command scripts for execution.

Details of use:
  dewey workon <app_name>   Change to the specified sidebar codebase.
  dewey (checkout | co) <branch_name>
  dewey (new-branch | nb) <branch_name>
  dewey up          Start the dev machines
  dewey dev-setup   Update the system developer libraries
  dewey sync        Pull from github, generate a difference report
  dewey setup       Set up a given codebase
  dewey bash        WIP SSH into the main docker container
  dewey pull        WIP Pull the latest docker image.
  dewey restart     WIP Restart docker
  dewey build       WIP Build for native devices
  dewey android     WIP Run the latest build on android
  dewey ios         WIP Run the latest build on ios
  dewey reset       WIP Update npm, bower, and all ionic packages and plugins
  dewey syncdb      WIP Run django syncdb
  dewey test        WIP Run all tests
  dewey init        WIP Initialize docker for first setup
  dewey hi          Say hello
  dewey upgrade     Upgrade dewey

"""
import os
import sys
from docopt import docopt

from dewey import VERSION
from dewey.util import suppress_stdout_stderr


def main():
    # Handle pre/post handlers
    run_pre = False
    run_post = False
    if "--pre" in sys.argv:
        run_pre = True
        sys.argv.remove("--pre")
    if "--post" in sys.argv:
        run_post = True
        sys.argv.remove("--post")

    # Platform detection
    platform = None
    if sys.platform == "win32":
        platform = "Windows"
    elif sys.platform == "darwin":
        platform = "MacOSX"
    elif sys.platform == "linux2":
        platform = "Linux"

    arguments = {}
    if run_pre or run_post:
        with suppress_stdout_stderr():
            try:
                arguments = docopt(__doc__, version='Dewey %s' % VERSION)
            except:
                pass
    else:
        arguments = docopt(__doc__, version='Dewey %s' % VERSION)

    for arg_name, value in arguments.items():
        if value is True:
            arg_name = arg_name.replace("-", "_")
            try:
                command_module = __import__("dewey.commands.%s" % arg_name, fromlist=['Command'])
                cmd = getattr(command_module, 'Command')()
                cmd.set_platform(platform)
                if run_pre:
                    print(cmd.run_pre(**arguments))
                elif run_post:
                    print(cmd.run_post(**arguments))
                else:
                    cmd.run_command(**arguments)
            except:
                if not run_pre and not run_post:
                    import traceback
                    traceback.print_exc()
                    print("Unable to find a command module for %s" % arg_name)


if __name__ == '__main__':
    main()
