import subprocess


def execute_command(command):
    return subprocess.Popen(command,
                            shell=True,
                            stdout=subprocess.PIPE).stdout.read()
