from insouwiki.services.audio_extractor import AudioExtractor
from insouwiki.services.youtube_audio_extractor import YouTubeAudioExtractor


def test_youtube_audio_extractor_is_audio_extractor():
    extractor = YouTubeAudioExtractor()

    assert isinstance(extractor, AudioExtractor)