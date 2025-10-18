import os
import sys

src = os.path.join(os.path.dirname(__file__), "..", "src")
if src not in sys.path:
    sys.path.insert(0, os.path.abspath(src))
