from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print "Oh, hello."

    def post_default(self, *args, **kwargs):
        pass

