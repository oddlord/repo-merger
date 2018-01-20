import os
import re
import shutil
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def blue(str):
    return bcolors.OKBLUE + str + bcolors.ENDC

def red(str):
    return bcolors.FAIL + str + bcolors.ENDC

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def remove_dir(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path, ignore_errors=False, onerror=None)

def get_repo_name(repo_url):
    try:
        repo_name = re.search('/(.+?).git', repo_url).group(1)
    except AttributeError:
        print red('Invalid repository URL: ' + repo_url + '\nAborting.')
        sys.exit(1)
    return repo_name
