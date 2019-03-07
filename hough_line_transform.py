import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    while ret:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 250, apertureSize=5, L2gradient=True)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

        if lines is not None:
            for roh, theta in lines[0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*roh
                y0 = b*roh
                pts1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
                pts2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
                cv2.line(frame, pts1, pts2, (0,255,0), 2)
        cv2.imshow("Live Feed", frame)

        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()


if __name__=="__main__":
    main()