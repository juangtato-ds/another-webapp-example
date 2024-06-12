openai_prompt_summary_template = """SYSTEM: You are an intelligent agent able to analyse song lyrics and provide helpful data 
INSTRUCTION: Given the following SONG LYRICS summarize them. DO NOT give explanations or add any additional information.
SONG LYRICS:
``` 
{song_lyrics}
``` 
SUMMARY: """

openai_prompt_countries_template = """SYSTEM: You are an intelligent agent able to analyse song lyrics and provide helpful data. 
INSTRUCTION: Given the following SONG LYRICS, identify and list all the COUNTRIES mentioned. DO NOT give explanations or add any additional information. If the SONG LYRICS doesn't mention any COUNTRIES, reply "-".
SONG LYRICS:
```
I took a trip to France and Italy,
Then sailed across to Spain,
Visited the great pyramids in Egypt,
And saw the wonders of Japan,
Oh, from France to Japan. 
```
COUNTRIES: France, Italy, Spain, Egypt, Japan
SONG LYRICS:
```
{song_lyrics}
```
COUNTRIES: """
