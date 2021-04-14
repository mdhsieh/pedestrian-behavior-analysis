import cv2
import sys

# Get image frames from captured video
# input_video_name: Name of the video to save image frames from
def save_image_frames(input_video_name):
    videoName = input_video_name
    cap = cv2.VideoCapture(videoName)
    success, frame = cap.read()
        
    count = 0
    while success:
      # save 1 frame per second
      # cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
      # save 1 frame per 500 milliseconds
      cap.set(cv2.CAP_PROP_POS_MSEC,(count*500))
      # num is 4 characters long with leading 0
      filename = "frames/frame%s.jpg" % str(count).zfill(4)
      # save frame as JPEG file      
      cv2.imwrite(filename, frame)
      success, frame = cap.read()
      print('Read a new frame: ', success)
      count += 1

if len(sys.argv) >= 2:
    save_image_frames(sys.argv[1])
else:
    print("Usage: save-image-frames.py [input_video.mp4]")