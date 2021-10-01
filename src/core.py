import urllib3
import json
import os
import re
import random
import pathlib
import time
import subprocess
import shlex
from .dotdict import dotdict

def find_file_in_directory_parents(haystack, needle):
    haystack = pathlib.Path(haystack).absolute()
    dirs = [haystack] + list(haystack.parents)
    for dir in dirs:
        globs = list(dir.glob(needle))
        if len(globs):
            return globs
    else:
        return []
    

def envsubst(str):
    """
    Mimic posix `envsubst` command by replacing `$VAR` format text in strings
    with synonymous environment variable value if present in the environment
    e.g. envsubst("$SHELL $TERM") -> "/bin/bash xterm-256color"
    """
    simple_shell_var_regex = re.compile(r'(?<!\\)\$([A-Za-z0-9_]+)')
    braced_shell_var_regex = re.compile(r'(?<!\\)\$\{([A-Za-z0-9_]+)\}')
    
    for envvar in braced_shell_var_regex.findall(str):
        str = str.replace(f'${{{envvar}}}', os.getenv(envvar, ''))
    
    for envvar in simple_shell_var_regex.findall(str):
        str = str.replace(f'${envvar}', os.getenv(envvar, ''))
    
    return str
    

def generate_password(length: int=32, seed=None) -> str:
    if seed:
        random.seed(seed)
        
    return ''.join(
        [
            random.choice(
                'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~%^*-_=+'
            )
            for i in range(length)
        ]
    )
    

def json_pretty_print(j):
    print( json.dumps(j, indent=4) )
    

def git_repo_info(path=None):
    if path is not None:
        path = pathlib.Path(path).expanduser()
    else:
        path = pathlib.Path.cwd()
        
    git_info = {}
    for key, command in {
                            "path":   "git rev-parse --show-toplevel",
                            "branch": "git branch --no-color --show-current",
                            "remote": "git remote -v"
                        }.items():
        git_info[key] = (
            subprocess.run(
                shlex.split(command),
                cwd=path,
                capture_output=True,
                text=True
            )
            .stdout
            .strip()
        )
    
    git_info['remote'] = git_info['remote'].partition(' (fetch)')[0].partition('origin\t')[2]
    
    return git_info