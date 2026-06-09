import flet as ft

class FormatUI:
  
  @staticmethod
  def show_snackbar(page, message: str, warna: str):
    color_value = getattr(ft.Colors, warna, ft.Colors.YELLOW_900)
    snack_bar = ft.SnackBar(
      content = ft.Text(
        message,
        color = ft.Colors.WHITE,
        weight = ft.FontWeight.BOLD,
        text_align = ft.TextAlign.CENTER
      ),
      bgcolor = ft.Colors.with_opacity(0.5, color_value)
    )
    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()
