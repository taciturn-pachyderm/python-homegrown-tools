from .lib import *

import sys, os, io, argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    'files',
    metavar='<path to .yml or .json or \'-\' for stdin>',
    type=str,
    nargs='*',
    help='zero or more file paths containing a YAML or JSON serialized object to translate to the opposite format. Specify - to read the object serialization from stdin and attempt to guess the format.'
)

args = parser.parse_args()


if len(args.files) < 1:
    print(
        "WARNING: no file arguments provided, defaulting to stdin. To explicitly specify stdin pass '-' as an argument.",
        file=sys.stderr
    )
    args.files=['-']
    
conversion_map = {
    '.json': json2yaml,
    '.jsonc': json2yaml,
    '.yml': yaml2json,
    '.yaml': yaml2json,
}

for file in args.files:
    if file == '-':
        file = io.StringIO(sys.stdin.read())
        
    try:
        ext = os.path.splitext(file)[1]
        print(conversion_map[ext](file))
        
    except (KeyError, IndexError, TypeError):
        try: print( json2yaml(file) )
        except json.decoder.JSONDecodeError:
            file.seek(0)
            print( yaml2json(file) )
        pass