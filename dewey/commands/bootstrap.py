import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        # return "echo 'Bootstrapping...\n' && boot2docker restart && sleep 2 && boot2docker init && boot2docker start --vbox-share=disable"
        pass

    def run_command(self, *args, **kwargs):
        # # Base OSX Dev
        # output = subprocess.check_output("docker-osx-dev", shell=True, )
        # try:
        #     running = subprocess.check_output("docker ps", shell=True)
        # except:
        #     running = subprocess.check_output("docker ps", shell=True)

        # Dev DNS
        # if "ruudud/devdns" not in running:
        #     try:
        #         output = subprocess.check_output("docker run -d --name devdns -p 53:53/udp -v /var/run/docker.sock:/var/run/docker.sock ruudud/devdns --restart always", shell=True, )
        #     except:
        #

        # Dev DNS
        # if "dnsdock" not in running:
        #     try:
        #         output = subprocess.check_output("docker run -d -v /var/run/docker.sock:/var/run/docker.sock --name dnsdock -p 172.17.0.1:53:53/udp tonistiigi/dnsdock", shell=True, )
        #     except:
        #         output = subprocess.check_output("docker run -d -v /var/run/docker.sock:/var/run/docker.sock -p 172.17.0.1:53:53/udp tonistiigi/dnsdock", shell=True, )

        # if "docker-cleanup" not in running:
        #     # Old image cleanup
        #     try:
        #         output = subprocess.check_output("docker run -d --name cleanup --restart always -v /var/run/docker.sock:/var/run/docker.sock:rw -v /var/lib/docker:/var/lib/docker:rw meltwater/docker-cleanup:latest ", shell=True, )
        #     except:
        #         output = subprocess.check_output("docker run meltwater/docker-cleanup:latest -d --restart always -v /var/run/docker.sock:/var/run/docker.sock:rw -v /var/lib/docker:/var/lib/docker:rw", shell=True, )        

        # Get the latest boot2docker
        # output = subprocess.check_call("docker-machine upgrade default", shell=True, )

        # Syncdb
        print("Ready for development")

    def post_default(self, *args, **kwargs):
        # return "cd ~/sidebar/core; docker-compose --project-name bu up --no-recreate"
        # return "docker-osx-dev -e .git -e bower_components -e node_modules -e source -e *.pyc -e app/frontends/app/dist -e app/frontends/app/build -e app/frontends/marketing/dist -e app/frontends/marketing/build -e docker/postgres"
        # return "cd app/api; python manage.py"
        pass
