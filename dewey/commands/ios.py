import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print("Building for iOS...")
        subprocess.call("gulp ionic_build", cwd="app", shell=True)
        subprocess.call("ionic build ios", cwd="app/native/ionic", shell=True)
        subprocess.call("open app/native/ionic/platforms/ios/SideBar.xcodeproj", shell=True)
        subprocess.call("say iOS build is done", shell=True, )

    def post_default(self, *args, **kwargs):
        pass
