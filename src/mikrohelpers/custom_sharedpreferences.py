import json
import flet as ft

class AppStorage:
  def __init__(self):
    self.sp = ft.SharedPreferences()

  async def set_object(self, key: str, value: dict):
    await self.sp.set(key, json.dumps(value))

  async def get_object(self, key: str) -> dict | None:
    data_json = await self.sp.get(key)
    if data_json:
      try:
        return json.loads(data_json)
      except Exception:
        return None
    return None
