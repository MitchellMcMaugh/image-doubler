import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog
from PIL import Image


def double_image_size(image_path, output_path):
    try:
        img = Image.open(image_path)
        width, height = img.size
        new_img = Image.new("RGB", (width * 2, height * 2))

        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                new_img.putpixel((x * 2, y * 2), pixel)
                new_img.putpixel((x * 2 + 1, y * 2), pixel)
                new_img.putpixel((x * 2, y * 2 + 1), pixel)
                new_img.putpixel((x * 2 + 1, y * 2 + 1), pixel)

        new_img.save(output_path)
        print("Image size doubled successfully.")
    except Exception as e:
        print(f"Error doubling image size: {e}")


class ImagePickerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.image_path = None
        self.pick_image()

    def pick_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        self.image_path, _ = QFileDialog.getOpenFileName(self, "Pick an Image", "", "Image Files (*.png *.jpg *.bmp)")
        if self.image_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Doubled Image", "", "Image Files (*.png *.jpg *.bmp)")
            if output_path:
                double_image_size(self.image_path, output_path)
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImagePickerApp()
    window.setWindowTitle('Image Picker')
    sys.exit(app.exec_())