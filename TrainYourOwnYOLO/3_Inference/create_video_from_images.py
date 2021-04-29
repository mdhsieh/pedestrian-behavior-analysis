import cv2
import os

# Combine all files from detection results folder into a video.
# Then display the video.
# All files must be the same size.

image_folder = "../Data/Source_Images/Test_Image_Detection_Results"
extension = ".png" # ".jpg"
video_name = "../video.avi"
WAIT_TIME_IN_MS = 1000

'''
Create a video.
'''
def create_video():
    images = [img for img in os.listdir(image_folder) if img.endswith(extension)]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

'''
Display the video.
'''
def display_video():
    cap = cv2.VideoCapture(video_name)

    while(cap.isOpened()):
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.waitKey(WAIT_TIME_IN_MS)

    cap.release()
    cv2.destroyAllWindows()
    
# Main
create_video()
display_video()