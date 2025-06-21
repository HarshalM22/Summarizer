from src.summarizer import summarize

def test_summarize():
    text = "This is a test document. It contains multiple sentences. It should be summarized."
    result = summarize(text, 2)
    assert isinstance(result, str) and len(result) > 0
