#!/usr/bin/env python
import cv2 as cv
import rospy
import rospkg
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
package_path = rospkg.RosPack().get_path('task5')
face_cascade.load(package_path + '/config/haarcascade_frontalface_alt.xml')
eyes_cascade.load(package_path + '/config/haarcascade_eye_tree_eyeglasses.xml')


def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    return frame


def imageCallback(img):
    bridge = CvBridge()
    img = bridge.imgmsg_to_cv2(img)
    img = detectAndDisplay(img)
    img = bridge.cv2_to_imgmsg(img, encoding="bgr8")
    pub = rospy.Publisher('viewer', Image, queue_size=10)
    pub.publish(img)


def start():
    rospy.init_node("face")
    rospy.Subscriber("/usb_cam/image_raw", Image, imageCallback)
    rospy.spin()

# if __name__ == '__main__':
start()