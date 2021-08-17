import cv2
import numpy as np
import pyautogui
import pytesseract



def type_string(string):
    pyautogui.write(string)

def capture_image(camera):
    return_value, image = camera.read()
    #return image
    #print(return_value)
    #cv2.imshow("test", image)
    cv2.imwrite('test.png', image)
    #cv2.waitKey(0)

def process_image(image):
    
    font = cv2.FONT_HERSHEY_SIMPLEX 

    frame = image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0.5)
    edge = cv2.Canny(blur, 50, 100, 2)

    contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)


    for contour, hier in zip(contours, hierarchy):
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Measure Size', edge)
    cv2.waitKey(0)

    return image

def ocr_image(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)

def main():
    camera = cv2.VideoCapture(0)
    for _ in range(0,10):
        image = capture_image(camera)

    camera.release()
    # image = cv2.imread('test.png')
    # image = process_image(image)
    # print(ocr_image(image))

if __name__ == '__main__':
    main()