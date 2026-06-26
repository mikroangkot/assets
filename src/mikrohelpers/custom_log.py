from datetime import datetime

class DataLog:

  @staticmethod
  def log_msg(message,tag="INFO"):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{current_time} [{tag}]: {message}")
