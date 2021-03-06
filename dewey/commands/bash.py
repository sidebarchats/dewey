from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "docker-compose run api bash"

    def run_command(self, *args, **kwargs):
        print("Upgraded.")

    def post_default(self, *args, **kwargs):
        pass
