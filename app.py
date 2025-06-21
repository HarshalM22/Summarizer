from src.utils import read_file, write_file
from src.text_cleaner import clean_text
from src.summarizer import summarize
from src.keyword_extractor import extract_keywords
from src.config import SUMMARY_SENTENCES, KEYWORD_COUNT

def main():
    raw_text = read_file('data/sample.txt')
    cleaned = clean_text(raw_text)
    summary = summarize(cleaned, SUMMARY_SENTENCES)
    keywords = extract_keywords(cleaned, KEYWORD_COUNT)
    write_file('outputs/summary.txt', summary)
    write_file('outputs/keywords.txt', '\n'.join(keywords))
    print('Summary:', summary)
    print('Keywords:', keywords)

if __name__ == '__main__':
    main()
