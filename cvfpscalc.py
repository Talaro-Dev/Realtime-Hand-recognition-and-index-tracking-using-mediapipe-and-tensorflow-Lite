from collections import deque
import cv2 as cv

class CvFpsCalc(object):
    def __init__(self, buffer_len=1):
        self.start_tick = cv.getTickCount()
        self.freq = 100.0 / cv.getTickFrequency()
        self._difftimes = deque(maxlen=buffer_len)
    
    def get(self):
        current_tick = cv.getTickCount()
        different_time = (current_tick - self.start_tick) * self.freq
        self.start_tick = current_tick

        self._difftimes.append(different_time)

        fps = 1000.0 / (sum(self._difftimes) / len(self._difftimes))
        fps_rounded = round(fps, 2)

        return fps_rounded
