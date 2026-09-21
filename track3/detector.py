from PIL import Image
import sys


def classify_image(path):
    image = Image.open(path).convert("RGB")

    red_pixels = 0
    total_pixels = image.width * image.height

    for r, g, b in image.getdata():
        if r > 150 and r > g * 1.5 and r > b * 1.5:
            red_pixels += 1

    red_ratio = red_pixels / total_pixels

    if red_ratio > 0.30:
        return "DEFECT"
    return "OK"


def main():
    if len(sys.argv) != 2:
        print("Usage: python detector.py <image_path>")
        return

    result = classify_image(sys.argv[1])
    print(result)


if __name__ == "__main__":
    main()
