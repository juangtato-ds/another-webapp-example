import abc

from song_backend.business.song.lyrics_analyser.lyrics_analyser_command import LyricsAnalyserCommand
from song_backend.business.song.lyrics_analyser.lyrics_analyser_result import LyricsAnalyserResult


class LyricsAnalyserAclAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    async def analyse(self, command: LyricsAnalyserCommand) -> LyricsAnalyserResult:
        raise NotImplementedError()
