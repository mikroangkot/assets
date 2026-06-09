from .src.custom_ui import FormatUI
from .src.custom_datetime import FormatDatetime
from .src.custom_dispatch import FormatDispatch

class DataFormatter(
  FormatUI,
  FormatDatetime,
  FormatDispatch
):
  pass
