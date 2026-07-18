from .custom_datetime import FormatDatetime
from .custom_dispatch import FormatDispatch
from .custom_ui import FormatUI
from .custom_decryptenv import DecryptData
from .custom_log import DataLog
from .custom_sharedpreferences import AppStorage

class DataFormatter(
  FormatDatetime,
  FormatDispatch,
  FormatUI,
  DecryptData,
  DataLog,
  AppStorage
):
  pass
