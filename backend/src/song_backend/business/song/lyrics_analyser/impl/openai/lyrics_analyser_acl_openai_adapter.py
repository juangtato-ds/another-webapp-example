from typing import Any
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

from song_backend.business.song.lyrics_analyser.lyrics_analyser_acl_adapter import (
    LyricsAnalyserAclAdapter,
)
from song_backend.business.song.lyrics_analyser.lyrics_analyser_command import LyricsAnalyserCommand
from song_backend.business.song.lyrics_analyser.lyrics_analyser_result import LyricsAnalyserResult
from song_backend.business.song.lyrics_analyser.impl.openai.openai_prompts import (
    openai_prompt_countries_template,
)


class LyricsAnalyserAclOpenaiAdapter(LyricsAnalyserAclAdapter):
    # Config
    _apikey: str
    # Client
    _llm: ChatOpenAI
    _country_chain: LLMChain
    _summary_chain: LLMChain

    def __init__(self, apikey: str) -> None:
        self._apikey = apikey
        self._llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",  # type: ignore
            temperature=0,
            max_tokens=1000,
            openai_api_key=self._apikey,  # type: ignore
        )
        self._country_chain = LLMChain(
            llm=self._llm,
            prompt=PromptTemplate.from_template(openai_prompt_countries_template),
            verbose=False,
        )

    @staticmethod
    def _process_countries_response(response: Any) -> list[str]:
        result: list[str] = []
        if (
            response is not None
            and "text" in response
            and response["text"] is not None
            and response["text"] != "-"
        ):
            result = response["text"].split(",")
        return result

    async def analyse(self, command: LyricsAnalyserCommand) -> LyricsAnalyserResult:
        country_list = self._process_countries_response(
            self._country_chain.invoke(input={"song_lyrics": command.lyrics})
        )

        return LyricsAnalyserResult(country_list=country_list)
