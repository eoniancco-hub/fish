from pathlib import Path
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

def png_chunk(kind, data):
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

def write_png(path, width, height, bg, accent):
    rows = []
    for y in range(height):
        row = bytearray([0])
        for x in range(width):
            stripe = ((x // 28) + (y // 28)) % 2 == 0
            edge = x < 8 or y < 8 or x >= width - 8 or y >= height - 8
            color = accent if edge or stripe else bg
            row.extend(color)
        rows.append(bytes(row))
    raw = b"".join(rows)
    data = b"\x89PNG\r\n\x1a\n"
    data += png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    data += png_chunk(b"IDAT", zlib.compress(raw, 9))
    data += png_chunk(b"IEND", b"")
    path.write_bytes(data)

palette = {
    "logo.png": ((247, 243, 234), (245, 158, 11)),
    "mechanic.png": ((22, 50, 79), (245, 158, 11)),
    "generator.png": ((63, 70, 82), (255, 209, 102)),
    "toolbox.png": ((245, 158, 11), (23, 23, 23)),
    "wrench.png": ((229, 231, 235), (63, 70, 82)),
    "multimeter.png": ((23, 23, 23), (255, 209, 102)),
    "smoke.png": ((229, 231, 235), (247, 243, 234)),
    "spark.png": ((255, 209, 102), (245, 158, 11)),
    "construction-site.jpg": ((22, 50, 79), (255, 209, 102)),
    "storefront.jpg": ((247, 243, 234), (245, 158, 11)),
    "event-power.jpg": ((63, 70, 82), (255, 209, 102)),
    "home-backup.jpg": ((229, 231, 235), (22, 50, 79)),
    "texture.jpg": ((23, 23, 23), (63, 70, 82)),
}

for name, colors in palette.items():
    write_png(ASSETS / name, 320, 220, *colors)

print(f"Generated {len(palette)} placeholder assets in {ASSETS}")

