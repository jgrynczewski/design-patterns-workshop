"""
Composition over Inheritance Violation - Explosion of inheritance hierarchy
"""


class Shape:
    def draw(self):
        return "Drawing shape"

    def calculate_area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        return "Drawing circle"

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return "Drawing rectangle"

    def calculate_area(self):
        return self.width * self.height


# PROBLEM: Adding colors requires new inheritance chains
class RedCircle(Circle):
    def draw(self):
        return "Drawing red circle"


class BlueCircle(Circle):
    def draw(self):
        return "Drawing blue circle"


class RedRectangle(Rectangle):
    def draw(self):
        return "Drawing red rectangle"


class BlueRectangle(Rectangle):
    def draw(self):
        return "Drawing blue rectangle"


# PROBLEM: Adding borders creates even more classes
class RedBorderedCircle(RedCircle):
    def draw(self):
        return "Drawing red circle with border"


class BlueBorderedCircle(BlueCircle):
    def draw(self):
        return "Drawing blue circle with border"


class RedBorderedRectangle(RedRectangle):
    def draw(self):
        return "Drawing red rectangle with border"


class BlueBorderedRectangle(BlueRectangle):
    def draw(self):
        return "Drawing blue rectangle with border"


# PROBLEM: What about dashed borders?
class RedDashedBorderedCircle(RedBorderedCircle):
    def draw(self):
        return "Drawing red circle with dashed border"


# ... and so on for every combination!


class Animal:
    def make_sound(self):
        return "Some sound"

    def move(self):
        return "Moving"


class Mammal(Animal):
    def give_birth(self):
        return "Giving birth to live young"


class Bird(Animal):
    def lay_eggs(self):
        return "Laying eggs"


class FlyingBird(Bird):
    def fly(self):
        return "Flying"


class SwimmingBird(Bird):
    def swim(self):
        return "Swimming"


# PROBLEM: What about birds that both fly and swim?
class FlyingSwimmingBird(FlyingBird, SwimmingBird):  # Multiple inheritance
    pass


class WaterMammal(Mammal):
    def swim(self):
        return "Swimming"


class LandMammal(Mammal):
    def walk(self):
        return "Walking"


# PROBLEM: What about mammals that swim and walk?
class AmphibiousMammal(WaterMammal, LandMammal):  # Multiple inheritance
    pass


# REAL WORLD EXAMPLE: Media Player
class MediaPlayer:
    def play(self):
        return "Playing media"


class AudioPlayer(MediaPlayer):
    def play_audio(self):
        return "Playing audio"


class VideoPlayer(MediaPlayer):
    def play_video(self):
        return "Playing video"


class MP3Player(AudioPlayer):
    def play(self):
        return "Playing MP3"


class MP4Player(VideoPlayer):
    def play(self):
        return "Playing MP4"


# PROBLEM: Device that plays both audio and video?
class MultimediaPlayer(AudioPlayer, VideoPlayer):  # Multiple inheritance issues
    def play(self):
        # Which parent's play() method to call?
        return "Playing multimedia"


# PROBLEM: Adding streaming capabilities
class StreamingAudioPlayer(AudioPlayer):
    def stream_audio(self):
        return "Streaming audio"


class StreamingVideoPlayer(VideoPlayer):
    def stream_video(self):
        return "Streaming video"


# PROBLEM: Streaming multimedia player?
class StreamingMultimediaPlayer(StreamingAudioPlayer, StreamingVideoPlayer):
    # Inheritance hierarchy explosion!
    pass

# PROBLEMS WITH THIS APPROACH:
# 1. Exponential growth of classes for each feature combination
# 2. Multiple inheritance conflicts and ambiguity
# 3. Code duplication across similar classes
# 4. Rigid hierarchy - hard to add new features
# 5. Violation of Single Responsibility Principle
# 6. Difficult to test individual features
# 7. Hard to maintain and extend
