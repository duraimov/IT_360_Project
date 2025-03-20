import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

if len(sys.argv) >= 2 and sys.argv[1] == 'test':
    from scanner import testing

    testing()
else:
    from scanner import scanner

    scanner()
    