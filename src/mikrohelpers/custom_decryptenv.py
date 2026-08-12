import os
import bcrypt
from dotenv import load_dotenv
from cryptography.fernet import Fernet

current_dir = os.getcwd()
env_at_root = os.path.join(current_dir, ".env")

script_dir = os.path.dirname(os.path.abspath(__file__))
env_relative_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".env"))

try:
  if os.path.exists(env_file):
    load_dotenv(dotenv_path=env_at_root, override=True)
  elif os.path.exists(env_relative_root):
    load_dotenv(dotenv_path=env_relative_root, override=True)
  else:
    load_dotenv(dotenv_path=".env", override=True)
except Exception:
  pass

class DecryptData:

  _fernet_instance = None

  @staticmethod
  def initialize_crypto(key: str):
    if key:
      DecryptData._fernet_instance = Fernet(key.encode("utf-8"))
  
  @staticmethod
  def password_bcrypt(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
    
  @staticmethod
  def env_data(var_name: str) -> str:
    try:
      encrypted_data = os.getenv(var_name)

      if not encrypted_data:
        return None

      if DecryptData._fernet_instance:
        return DecryptData._fernet_instance.decrypt(encrypted_data.encode()).decode()

      return None

    except Exception as err:
      return None
