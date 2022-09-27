import subprocess, shlex

def popen(cmdline, stdin=None, **kwargs):
    p = (
        subprocess.Popen(
            shlex.split(cmdline),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            **kwargs
        )
    )
    return (
        *(
            o.decode().strip()
            for o in p.communicate(stdin)
        ),
        p.returncode
    )