from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print "Still need to write this!"

    def post_default(self, *args, **kwargs):
        pass

