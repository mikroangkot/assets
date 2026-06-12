import re

class FormatDispatch:

  @staticmethod
  def format_bus(teks):
    bersih = str(teks).upper()
    bersih = re.sub(r"[^A-Z0-9]", "", bersih)
    match = re.match(r"^([A-Z]+)(\d+)$", bersih)

    if match:
      huruf = match.group(1)
      angka = match.group(2)
      return f"{huruf}-{angka}"
      
    return teks

  @staticmethod
  def format_rute(teks_koridor):
    bersih = str(teks).upper()
    bersih = re.sub(r"[^A-Z0-9]", "", bersih)
    match = re.match(r"^([A-Z]+)(\d+)$", bersih)

    if match:
      huruf = match.group(1)
      angka = int(match.group(2))
      return f"{huruf}{angka}"
      
    return teks
