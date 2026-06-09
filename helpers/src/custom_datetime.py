from datetime import datetime

class FormatDatetime:

  @staticmethod
  def format_tanggal(dt_string):
    if not dt_string:
      return "-"
      
    tanggal_raw = str(dt_string)[:10]
    
    try:
      dt_obj = datetime.strptime(tanggal_raw, "%Y-%m-%d")
      return dt_obj.strftime("%d-%m-%Y")
      
    except ValueError:
      return tanggal_raw

  @staticmethod
  def format_jam(dt_string):
    if not dt_string:
      return "-"
      
    try:
      dt_obj = datetime.strptime(str(dt_string).split(".")[0], "%Y-%m-%d %H:%M:%S")
      return dt_obj.strftime("%H:%M:%S")
      
    except ValueError:
      return str(dt_string)[11:16] if len(str(dt_string)) >= 16 else "-"

  @staticmethod
  def hitung_durasi(start_str, end_str):
    if not start_str or not end_str:
      return "00:00:00"
      
    try:
      start_time = datetime.fromisoformat(start_str.replace("Z", "").replace(" ", "T"))
      end_time = datetime.fromisoformat(end_str.replace("Z", "").replace(" ", "T"))
      selisih = end_time - start_time
      total_detik = int(selisih.total_seconds())
      
      if total_detik < 0:
        return "00:00:00"
        
      jam = total_detik // 3600
      menit = (total_detik % 3600) // 60
      detik = total_detik % 60
      return f"{jam:02d}:{menit:02d}:{detik:02d}"
      
    except Exception:
      return "00:00:00"
