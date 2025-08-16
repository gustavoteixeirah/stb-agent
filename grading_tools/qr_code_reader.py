import json
from typing import Any
from smolagents import tool
import cv2 # Importamos a biblioteca os para pegar o nome do arquivo

@tool
def detect_and_decode_qr(image_path: str) -> Any:
    """
    Detects and decodes a QR code from a given image file.

    Args:
        image_path (str): The path to the image file containing the QR code.

    Returns:
        str or None: The decoded data from the QR code if found, otherwise None.
    """
    # Read the image
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return None

    # Create a QRCodeDetector object
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    # The detectAndDecode method returns:
    # 1. decoded_data: The decoded string from the QR code.
    # 2. points: The vertices of the detected QR code's bounding box.
    # 3. straight_qrcode: The straightened, binarized QR code image.
    decoded_data, points, straight_qrcode = detector.detectAndDecode(img)

    if decoded_data:
        print(f"QR Code detected. Decoded data: {decoded_data}")
        # Optional: Draw bounding box if points are available
        # if points is not None:
        #     points = points[0].astype(int)
        #     cv2.polylines(img, [points], True, (0, 255, 0), 2)
        #     cv2.imshow("QR Code Detected", img)
        #     cv2.waitKey(0)
        #     cv2.destroyAllWindows()
        return decoded_data
    else:
        print("No QR Code detected in the image.")
        return None