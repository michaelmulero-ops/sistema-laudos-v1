import streamlit as st
import os
import subprocess
import sys

# Tenta instalar o Groq automaticamente se ele não estiver no servidor
try:
    from groq import Groq
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "groq"])
    from groq import Groq

import time
from datetime import datetime
from PIL import Image, ImageDraw
