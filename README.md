## OpenCV Study Project
A comprehensive collection of Python scripts demonstrating the core capabilities of the OpenCV library. This repository serves as a personal learning log for computer vision techniques, ranging from basic image processing to real-time video manipulation and object detection.

# 📂 Project Structure
The repository is organized by specific functions and modules:
| File / Directory | Description |
| :--- | :--- |
| **FaceRecognitionTechnology.py** | Implementation of Haar Cascades for detecting faces in images. |
| **video.py** | Handling video streams, camera input, and applying real-time filters (Canny, Blur, Dilation). |
| **image.py** | Basics of image loading, resizing, cropping, and color space conversions. |
| **img_transform.py** | Geometric transformations including rotation, translation (shifting), and flipping. |
| **img_bit_operations.py** | Logical operations (AND, OR, XOR, NOT) using bitwise masks. |
| **img_formats.py** | Working with different color spaces like HSV, LAB, and RGB, plus channel splitting/merging. |
| **masks.py** | Using geometric shapes as masks to isolate specific parts of an image. |
| **sopla_paint.py** | Drawing primitives (rectangles, circles, lines) and rendering text on canvas. |
| **faces.xml** | Pre-trained Haar Cascade classifier for face detection. |
| **/images** | Directory containing source assets (images/videos) for testing. |
# 🚀 Key Features Explored


### 1. 🖼️ Image Processing Basics
* **Color Conversion:** Switching between `BGR`, `Gray`, `HSV`, and `LAB`.
* **Filters:** Applying `Gaussian Blur` and `Canny Edge Detection`.
* **Morphological Ops:** Using `dilate` and `erode` to manipulate edge thickness.

### 2. 📐 Geometric Transformations
* **Rotation:** Custom functions for image rotation around a center point.
* **Translation:** Matrices for shifting images along X and Y axes.
* **Resizing:** Proportional scaling and manual cropping.

### 3. 🎭 Bitwise Operations & Masking
* **Logic:** Combining images using logical operators (`AND`, `OR`, `XOR`, `NOT`).
* **ROI:** Creating complex masks to extract specific regions of interest.

### 4. 👤 Face Detection
* **Haar Cascades:** Utilizing `CascadeClassifier` to identify facial coordinates.
* **Bounding Boxes:** Drawing rectangles around detected objects using `cv2.rectangle`.

### 5. 🎥 Video Analysis
* **Streams:** Processing video files and live camera feeds.
* **Real-time:** Applying frame-by-frame transformations on the fly.
