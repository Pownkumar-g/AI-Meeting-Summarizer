from summarization import summarize_transcript


transcript = """
The project team discussed the new website design.
Sarah will prepare the homepage mockup by Friday.
John decided that the application will use PostgreSQL.
The team agreed to conduct user testing next week.
"""


result = summarize_transcript(transcript)

print("\nGenerated Summary:\n")
print(result)