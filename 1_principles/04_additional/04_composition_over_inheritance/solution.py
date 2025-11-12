"""
Composition over Inheritance Solution - Flexible behavior composition
"""


# COMPONENTS - Individual behaviors that can be combined
class Color:
    def __init__(self, name):
        self.name = name

    def apply(self):
        return f"{self.name} color"


class Border:
    def __init__(self, style="solid"):
        self.style = style

    def draw(self):
        return f"{self.style} border"


class ShapeRenderer:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def render(self):
        return f"Rendering {self.shape_type}"


# SHAPES - Compose behaviors instead of inheriting
class Shape:
    def __init__(self, renderer, color=None, border=None):
        self.renderer = renderer  # Composition
        self.color = color  # Optional composition
        self.border = border  # Optional composition

    def draw(self):
        result = self.renderer.render()

        if self.color:
            result += f" with {self.color.apply()}"

        if self.border:
            result += f" and {self.border.draw()}"

        return result


class Circle(Shape):
    def __init__(self, radius, color=None, border=None):
        super().__init__(ShapeRenderer("circle"), color, border)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color=None, border=None):
        super().__init__(ShapeRenderer("rectangle"), color, border)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# EASY COMBINATIONS - No class explosion!
red_circle = Circle(5, Color("red"))
blue_bordered_rectangle = Rectangle(10, 20, Color("blue"), Border("solid"))
red_dashed_circle = Circle(3, Color("red"), Border("dashed"))


# Any combination possible without new classes!


# ANIMAL EXAMPLE - Behavioral composition
class Movement:
    def __init__(self, method):
        self.method = method

    def move(self):
        return f"Moving by {self.method}"


class Reproduction:
    def __init__(self, method):
        self.method = method

    def reproduce(self):
        return f"Reproducing by {self.method}"


class SoundMaker:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return f"Making sound: {self.sound}"


class Animal:
    def __init__(self, name, movement, reproduction, sound_maker):
        self.name = name
        self.movement = movement  # Composition
        self.reproduction = reproduction  # Composition
        self.sound_maker = sound_maker  # Composition

    def move(self):
        return self.movement.move()

    def reproduce(self):
        return self.reproduction.reproduce()

    def make_sound(self):
        return self.sound_maker.make_sound()


# FLEXIBLE ANIMAL CREATION
duck = Animal(
    "Duck",
    Movement("flying and swimming"),  # Multiple behaviors in one component
    Reproduction("laying eggs"),
    SoundMaker("quack")
)

dolphin = Animal(
    "Dolphin",
    Movement("swimming"),
    Reproduction("giving birth"),
    SoundMaker("clicking")
)


# Easy to create animals with any combination of behaviors!


# MEDIA PLAYER EXAMPLE - Feature composition
class AudioCodec:
    def __init__(self, format_type):
        self.format_type = format_type

    def decode_audio(self):
        return f"Decoding {self.format_type} audio"


class VideoCodec:
    def __init__(self, format_type):
        self.format_type = format_type

    def decode_video(self):
        return f"Decoding {self.format_type} video"


class StreamingCapability:
    def __init__(self, protocol):
        self.protocol = protocol

    def stream(self):
        return f"Streaming via {self.protocol}"


class MediaPlayer:
    def __init__(self, audio_codecs=None, video_codecs=None, streaming=None):
        self.audio_codecs = audio_codecs or []  # Composition
        self.video_codecs = video_codecs or []  # Composition
        self.streaming = streaming  # Optional composition

    def play_audio(self, format_type):
        for codec in self.audio_codecs:
            if codec.format_type == format_type:
                return codec.decode_audio()
        return f"Cannot play {format_type} audio"

    def play_video(self, format_type):
        for codec in self.video_codecs:
            if codec.format_type == format_type:
                return codec.decode_video()
        return f"Cannot play {format_type} video"

    def stream_media(self):
        if self.streaming:
            return self.streaming.stream()
        return "Streaming not supported"


# FLEXIBLE MEDIA PLAYER CREATION
basic_player = MediaPlayer(
    audio_codecs=[AudioCodec("MP3")],
    video_codecs=[VideoCodec("MP4")]
)

premium_player = MediaPlayer(
    audio_codecs=[AudioCodec("MP3"), AudioCodec("FLAC")],
    video_codecs=[VideoCodec("MP4"), VideoCodec("AVI")],
    streaming=StreamingCapability("HTTP")
)

# Easy to create players with any combination of features!


# BENEFITS OF COMPOSITION:
# 1. No class explosion - infinite combinations with finite components
# 2. Easy to test individual components in isolation
# 3. Runtime behavior modification possible
# 4. Code reuse across different contexts
# 5. Single Responsibility Principle maintained
# 6. Open/Closed Principle - add new behaviors without changing existing code
# 7. Flexible and maintainable architecture
