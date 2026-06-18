from .custom_datetime import FormatDatetime
from .custom_dispatch import FormatDispatch
from .custom_ui import FormatUI
from .custom_decryptenv import DecryptData

class DataFormatter(
  FormatDatetime,
  FormatDispatch,
  FormatUI,
  DecryptData
):
  pass