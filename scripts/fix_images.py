import os

# 1x1 Blue Pixel PNG (合法文件头)
ONE_PIXEL_PNG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xfc\xcf\xc0\x00\x00\x03\x01\x01\x00y\xfc\x0c\x88\x00\x00\x00\x00IEND\xaeB`\x82'

paths = [
    "content/zh/post/2026-03-04-website-launch/featured.png",
    "content/en/post/2026-03-04-website-launch/featured.png"
]

for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(ONE_PIXEL_PNG)
    print(f"[+] Fixed raster image: {p}")

print("[*] Image fix complete.")
