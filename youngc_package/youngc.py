try:
    import Crypto
    del Crypto
except ImportError:
    print("[ERROR] You may install Crypto model by 'sudo pip install pycryptodome'")
    raise



from Crypto.Util.number import long_to_bytes
from Crypto.Util.number import bytes_to_long




