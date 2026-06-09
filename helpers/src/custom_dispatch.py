import re

class FormatDispatch:

  @staticmethod
  def format_bus(teks):
    bersih = teks.upper().replace(" ", "").replace("-", "")
    match = re.match(r"^([A-Z]+)(\d+)$", bersih)

    if match:
      huruf = match.group(1)
      angka = match.group(2)
      return f"{huruf}-{angka}"
      
    return teks

  @staticmethod
  def format_rute(teks_koridor):
    if not teks_koridor:
      return "-"

    koridor = str(teks_koridor).upper()
    koridor = koridor.replace(" ", "").replace("JAK", "JAK.")
    koridor = koridor.replace("..", ".")
    hasil = re.sub(r"JAK\.(\d)(?!\d)", r"JAK.0\1", koridor)
    return hasil
