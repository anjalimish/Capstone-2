# Capstone-2
# **Lane Lines Detection Using Python and OpenCV** 
### In this project, we used Python and OpenCV to detect lanes on the road. We developed a processing pipeline that works on a series of individual images, and applied the result to a video stream.

Pipeline architecture:
---
1. Load test images.
2. Apply Color Selection
3. Apply Canny edge detection.
   - Apply gray scaling to the images.
   - Apply Gaussian smoothing.
   - Perform Canny edge detection.
4. Determine the region of interest.
5. Camera Calibration
6. Detecting lane area
7. Apply on image & video streams.



