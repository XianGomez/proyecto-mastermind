import sys
import os

# Esto añade 'src' al path para que los tests y los archivos de src se encuentren
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
