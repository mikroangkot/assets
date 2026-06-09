import flet as ft
import re
from datetime import datetime

class DataFormatter:

	@staticmethod
	def show_snackbar(page, message: str, warna: str):
		color_value = getattr(ft.Colors, warna, ft.Colors.YELLOW_900)
		snack_bar = ft.SnackBar(
			content = ft.Text(
				message,
				color = ft.Colors.WHITE,
				weight = ft.FontWeight.BOLD,
				text_align = ft.TextAlign.CENTER,
			),
			bgcolor = ft.Colors.with_opacity(0.5, color_value)
		)
		page.overlay.append(snack_bar)
		snack_bar.open = True
		page.update()

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
