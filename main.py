from pathlib import Path
import json
import os


with open("res/cards.json", "r") as file:
    cards = json.load(file)


def download_image(image_id: str, image_url: str) -> None:
    path = Path(f"res/cards/{image_id[0]}")
    path.mkdir(exist_ok=True, parents=True)
    path = path / f"{image_id}.jpg"
    if path.exists(): return
    command = f'curl "{image_url}" -s -o {path}'
    os.system(command)


progress = 0
total = len(cards)
for v in cards.values():
    download_image(str(v["id"]), v["card_image"])    
    progress += 1
    os.system("clear")
    print(f"{progress}/{total}")