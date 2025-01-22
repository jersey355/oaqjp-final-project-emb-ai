import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):

        data = emotion_detector("I am glad this happened")
        self.assertEqual(data["dominant_emotion"], "joy")

        data = emotion_detector("I am really mad about this")
        self.assertEqual(data["dominant_emotion"], "anger")

        data = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(data["dominant_emotion"], "disgust")

        data = emotion_detector("I am so sad about this")
        self.assertEqual(data["dominant_emotion"], "sadness")

        data = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(data["dominant_emotion"], "fear")

unittest.main()