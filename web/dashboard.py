"""
OmniTrace Web Dashboard launcher.

Serves the interactive dashboard and REST API on http://localhost:5000/
This is a thin wrapper around api.py so `python web/dashboard.py` works
exactly like `python api.py`.

Developed by JOJIN JOHN.
"""

import os
import sys

# Make the project root importable regardless of where this is launched from.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from api import app  # noqa: E402

if __name__ == '__main__':
    print("OmniTrace dashboard running at http://localhost:5000/dashboard")
    app.run(host='0.0.0.0', port=5000, debug=False)
