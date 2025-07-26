# Realtime-Hand-recognition-and-index-tracking-using-mediapipe-and-tensorflow-Lite

Using MediaPipe (python Vesrion) predict hand pose. This is a simple program that recognizes hand signs and finger gestures with a single MLP using the detected key points

This repository contains the following contents:
- Sample application
- Hand sign recognition model using TFLite
- Finger gesture recognition model using TFLite
- Learning data for hand sign recognition
- Learning data for finger gesture recognition


# Requirements
- mediapipe 0.8.1
- OpenCV 3.4.2 or Later
- Tensorflow 2.3.0 or later
- tf-nightly 2.5.0.dev or later (Only when creating TFLite for an LSTM model)
- scikit-learn 0.23.2 or later (Only for usage of the confusion matrix)
- matplotlib 3.3.2 or later (Only for usage of the confusion matrix)


# For the application run

The following options can be specified when running the application:
- --device
  Sepcifying the camera device number (Default: 0, for webcam)
- --width
  Width at the time of camera capture (Default: 960)
- --height
  Height at the time of camera capture (Default:540)
- --use_static_image_mode
  Whether to use static_image_mode option for MediaPipe inference (Default: Unspecified)
- --min_detection_confidence
  Detection confidence threshold (Default: 0.5)
- --min_tracking_confidence
  Tracking confidence threshold (Default: 0.5)


## app.py

This is the program for the interface.
In addition, laearning data (key points) for hand sign and finger gesture recognition

##keypoint_classification.ipynb##
This is the model training script for hand sign recognition.

##point_history_classification.ipynb##
This is the model training script for finger gesture recognition.

##model/keypoint_clasifier##
This directory stores files related to hand sign recognition.
The following files are stored:
- Training data (keypoint.csv)
- Traied model (keypoint_classifier.tflite)
- Label data (keypoint_classifier_label.csv)
- Inference module (keypoint_classifier.py)

## model/point_history_classifier
This directory stores files related to finger gesture recognition.
the follwing files are stored:
- Training data (point_history.csv)
- Traied model (point_history_classifier.tflite)
- Label data (point_history_classifier_label.csv)
- Inference module (point_history_classifier.py)

## utils/cvfpscalc.py
This is the module for FPS measurement


# Reference
- [MediaPipe](https://ai.google.dev/edge/mediapipe/solutions/guide)
