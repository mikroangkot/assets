from .src.custom_datetime import FormatDatetime
from .src.custom_dispatch import FormatDispatch
from .src.custom_ui import FormatUI

class DataFormatter(
  FormatDatetime,
  FormatDispatch,
  FormatUI
):
  pass
