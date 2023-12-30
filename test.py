import cv2
from matplotlib import pyplot as plt

# 이미지를 로드합니다.
image_path = "./1.mkv_20231230_145508.520.png"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny 엣지 디텍터를 사용하여 엣지를 검출합니다.
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Let's break down the process and see each step.

# Step 1: Edge Detection Visualization
# Apply GaussianBlur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

# Display the edge detection result
plt.figure(figsize=(10, 7))
plt.imshow(edges, cmap="gray")
plt.title("Edge Detection Result")
plt.axis("off")
plt.show()

# Step 2: Contour Detection and Visualization
# Find contours on the blurred and edge-detected image for better accuracy
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Draw all contours to see what has been detected
all_contours_image = image.copy()
cv2.drawContours(all_contours_image, contours, -1, (0, 255, 0), 1)

# Display the contour detection result
plt.figure(figsize=(10, 7))
plt.imshow(cv2.cvtColor(all_contours_image, cv2.COLOR_BGR2RGB))
plt.title("All Contours Detected")
plt.axis("off")
plt.show()


# Step 3: Find the largest rectangle contour which should be the card
def find_largest_rectangle(contours):
    largest_area = 0
    largest_rectangle = None
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        if len(approx) == 4:
            area = cv2.contourArea(approx)
            if area > largest_area:
                largest_area = area
                largest_rectangle = approx
    return largest_rectangle


# Find the largest rectangle contour
largest_rectangle = find_largest_rectangle(contours)

# Draw the largest rectangle contour if one is found
if largest_rectangle is not None:
    largest_rect_image = image.copy()
    cv2.drawContours(largest_rect_image, [largest_rectangle], -1, (0, 255, 0), 3)

    # Display the largest rectangle contour result
    plt.figure(figsize=(10, 7))
    plt.imshow(cv2.cvtColor(largest_rect_image, cv2.COLOR_BGR2RGB))
    plt.title("Largest Rectangle Contour")
    plt.axis("off")
    plt.show()
else:
    print("No rectangle contour found.")
