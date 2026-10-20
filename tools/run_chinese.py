"""Entry point for the Simplified Chinese community executable."""
import sys
from nvidia_vbios.windows_loader.gui import main

if __name__ == '__main__':
    args = sys.argv[1:]
    if '--lang' not in args:
        args = ['--lang', 'zh_CN', *args]
    raise SystemExit(main(args))
