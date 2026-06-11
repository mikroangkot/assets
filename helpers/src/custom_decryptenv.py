import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

class DecryptData:
  
  @staticmethod
  def password_bcrypt(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
    
  @staticmethod
  def env_data(var_name: str) -> str:
    try:
      encrypted_data = os.getenv(var_name)
      crypto_key = os.getenv("CRYPTO_KEY")

      if not encrypted_data or not crypto_key:
        return None

      f = Fernet(crypto_key.encode())
      return f.decrypt(encrypted_data.encode()).decode()

    except Exception as err:
      return None
