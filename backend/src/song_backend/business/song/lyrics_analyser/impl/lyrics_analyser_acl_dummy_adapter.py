from song_backend.business.song.lyrics_analyser.lyrics_analyser_acl_adapter import (
    LyricsAnalyserAclAdapter,
)
from song_backend.business.song.lyrics_analyser.lyrics_analyser_command import LyricsAnalyserCommand
from song_backend.business.song.lyrics_analyser.lyrics_analyser_result import LyricsAnalyserResult


class LyricsAnalyserAclDummyAdapter(LyricsAnalyserAclAdapter):
    async def analyse(self, command: LyricsAnalyserCommand) -> LyricsAnalyserResult:
        return LyricsAnalyserResult(
            country_list=["Spain", "United Kingdom", "Rumania", "Portugal", "France"]
        )
