from .src.custom_datetime import FormatDatetime
from .src.custom_dispatch import FormatDispatch
from .src.custom_ui import FormatUI
from .src.custom_decryptenv import DecryptData

class DataFormatter(
  FormatDatetime,
  FormatDispatch,
  FormatUI,
  DecryptData
):
  pass
