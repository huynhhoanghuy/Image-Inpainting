import cv2
import numpy as np

drawing = True  # true if mouse is pressed
mode = True


# mouse callback function
def paint_draw(event, former_x, former_y, flags, param):
    global current_former_x, current_former_y, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        current_former_x, current_former_y = former_x, former_y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.line(image, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 255), 5)
                cv2.line(mask, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 0), 5)
                current_former_x = former_x
                current_former_y = former_y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.line(image, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 255), 5)
            cv2.line(mask, (current_former_x, current_former_y), (former_x, former_y), (0, 0, 0), 5)
            current_former_x = former_x
            current_former_y = former_y
    return former_x, former_y


image = cv2.imread("examples/places2/case1_raw.png")
mask = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("OpenCV Paint Brush")
cv2.setMouseCallback('OpenCV Paint Brush', paint_draw)
while True:
    cv2.imshow('OpenCV Paint Brush', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Escape KEY
        cv2.imwrite("painted_image.jpg", mask)
        break

cv2.destroyAllWindows()