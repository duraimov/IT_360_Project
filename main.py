import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'virustotal_python-1.1.0')))

if len(sys.argv) >= 2 and sys.argv[1] == 'test':
    from scanner import testing

    testing()
else:
    from scanner import scanner

    scanner()
    