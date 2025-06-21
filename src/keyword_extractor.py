import yake

def extract_keywords(text, max_keywords=5):
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)
    return [kw for kw, score in keywords[:max_keywords]]
