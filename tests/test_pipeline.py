import unittest
import time
from utils.pdf_handler import extract_text_from_pdf
from utils.summary_extractor import summarize_text
from utils.keyword_extractor import extract_keywords

class TestPipeline(unittest.TestCase):

    def test_pdf_extraction(self):
        start_time = time.time()  
        try:
            text = extract_text_from_pdf("tests/sample_pdfs/short_sample_1.pdf")  
            self.assertTrue(len(text) > 0)
            print(f"PDF extraction took {time.time() - start_time:.2f} seconds.")  
        except Exception as e:
            self.fail(f"PDF extraction failed: {e}")  

    def test_summary_extraction(self):
        start_time = time.time()  
        try:
            text = "This is a short document for testing purposes."
            summary = summarize_text(text)
            self.assertEqual(summary, text)
            print(f"Summary extraction took {time.time() - start_time:.2f} seconds.")  
        except Exception as e:
            self.fail(f"Summary extraction failed: {e}")  

    def test_keyword_extraction(self):
        start_time = time.time()  
        try:
            text = "AI and Machine Learning are transforming industries."
            keywords = extract_keywords(text)
            self.assertIn("AI", keywords)
            self.assertIn("Machine Learning", keywords)
            print(f"Keyword extraction took {time.time() - start_time:.2f} seconds.")  
        except Exception as e:
            self.fail(f"Keyword extraction failed: {e}")  

if __name__ == "__main__":
    unittest.main()
