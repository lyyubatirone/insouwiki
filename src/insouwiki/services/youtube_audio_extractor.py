from pathlib import Path

from yt_dlp import YoutubeDL

from insouwiki.domain.document import Document
from insouwiki.services.audio_extractor import AudioExtractor


class YouTubeAudioExtractor(AudioExtractor):
    """
    Extracteur audio réel basé sur yt-dlp.

    Il extrait la piste audio d'un document YouTube
    dans un dossier fourni par l'appelant.
    """

    def extract(
        self,
        document: Document,
        output_directory: Path,
    ) -> Path:
        output_directory.mkdir(parents=True, exist_ok=True)

        output_template = str(output_directory / "%(id)s.%(ext)s")

        options = {
            "format": "bestaudio/best",
            "outtmpl": output_template,
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "m4a",
                }
            ],
        }

        with YoutubeDL(options) as ydl:
            info = ydl.extract_info(
                str(document.original_url),
                download=True,
            )

            prepared_path = Path(ydl.prepare_filename(info))
            audio_path = prepared_path.with_suffix(".m4a")

        if not audio_path.exists():
            raise FileNotFoundError(
                f"Le fichier audio attendu n'a pas été créé : {audio_path}"
            )

        return audio_path