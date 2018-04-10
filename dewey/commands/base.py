import pickle
import sys

from clint import resources

VALID_PLATFORMS = ["Windows", "MacOSX", "Linux"]

class Brain(object):
    pass


class DeweyCommand(object):

    def __init__(self):
        resources.init('sidebar', 'dewey')
        brain_pickle = resources.user.read('config.py')
        if brain_pickle:
            self.brain = pickle.load(brain_pickle)
        else:
            self.brain = Brain()

    def answer_yes_or_no(self, question, default="yes"):
        """Ask a yes/no question via raw_input() and return their answer.

        "question" is a string that is presented to the user.
        "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

        The "answer" return value is one of "yes" or "no".
        """
        valid = {"yes":True,   "y":True,  "ye":True,
                 "no":False,     "n":False}
        if default == None:
            prompt = " [y/n] "
        elif default == "yes":
            prompt = " [Y/n] "
        elif default == "no":
            prompt = " [y/N] "
        else:
            raise ValueError("invalid default answer: '%s'" % default)

        while True:
            sys.stdout.write(question + prompt)
            choice = raw_input().lower()
            if default is not None and choice == '':
                return valid[default]
            elif choice in valid:
                return valid[choice]
            else:
                sys.stdout.write("Please respond with 'yes' or 'no' "\
                                 "(or 'y' or 'n').\n")

    def question_with_default(self, question, default=None):
        """Ask a question, with a default value."""
        prompt = ""
        if default:
            prompt = " [%s]" % default

        while True:
            sys.stdout.write(question + prompt)
            choice = raw_input()
            if default is not None and choice == '':
                return default
            else:
                choice

    def save(self):
        resources.user.read('config.py', pickle.dump(self.brain))

    def set_platform(self, platform):
        assert platform in VALID_PLATFORMS
        self.platform = platform

    def run_pre(self, *args, **kwargs):
        if not self.platform:
            raise OSError("echo 'Dewey doesn't know your operating system. Sorry!'")
        if self.platform == "Windows":
            try:
                ret = self.pre_windows(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "MacOSX":
            try:
                ret = self.pre_macosx(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "Linux":
            try:
                ret = self.pre_unix(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        else:
            raise OSError("echo 'Dewey doesn't know how to run pre for %s'" % self.platform)

    def pre_default(self, *args, **kwargs):
        raise NotImplementedError("Pre-command not written!")

    def pre_windows(self, *args, **kwargs):
        """Returns a string to execute on windows"""
        return self.pre_default(self, *args, **kwargs)

    def pre_macosx(self, *args, **kwargs):
        """Returns a string to execute on Mac OS X"""
        return self.pre_default(self, *args, **kwargs)

    def pre_unix(self, *args, **kwargs):
        """Returns a string to execute on unix"""
        return self.pre_default(self, *args, **kwargs)

    def run_command(self, *args, **kwargs):
        """Runs the body of the command (should not have current shell side effects.)"""
        pass

    def run_post(self, *args, **kwargs):
        if not self.platform:
            raise OSError("echo 'Dewey doesn't know your operating system. Sorry!'")
        if self.platform == "Windows":
            try:
                ret = self.post_windows(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "MacOSX":
            try:
                ret = self.post_macosx(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "Linux":
            try:
                ret = self.post_unix(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        else:
            raise OSError("echo 'Dewey doesn't know how to run post for %s'" % self.platform)

    def post_default(self, *args, **kwargs):
        raise NotImplementedError("Post-command not written!")

    def post_windows(self, *args, **kwargs):
        """Returns a string to execute on windows"""
        return self.post_default(self, *args, **kwargs)

    def post_macosx(self, *args, **kwargs):
        """Returns a string to execute on Mac OS X"""
        return self.post_default(self, *args, **kwargs)

    def post_unix(self, *args, **kwargs):
        """Returns a string to execute on unix"""
        return self.post_default(self, *args, **kwargs)
