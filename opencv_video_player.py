import cv2

def main():
    windowname = "opencv video player"
    cv2.namedWindow(windowname)
    filename = "/home/raj/Videos/Daredevil/Daredevil S01 Season 01 Complete 720p WEBRip x265 AAC E-Subs [GWC]/Daredevil.S01E01.720p.WEBrip-[Bi-3-Seda.Ir].mkv"
    cap = cv2.VideoCapture(filename)

    while cap.isOpened():
        ret, frame = cap.read()
        print(ret)

        if ret:
            cv2.imshow(windowname, frame)
            if cv2.waitKey(33) == 27:
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()