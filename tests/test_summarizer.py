"""
Tests for the summarizer module.
"""

from src.main import Summarizer

def test_summarizer_initialization():
    """Test that the summarizer can be initialized."""
    summarizer = Summarizer()
    assert isinstance(summarizer, Summarizer)

def test_basic_summarization():
    """Test that the summarize method returns a string."""
    summarizer = Summarizer()
    text = "This is a test text that needs to be summarized."
    summary = summarizer.summarize(text)
    assert isinstance(summary, str) 