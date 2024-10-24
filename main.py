import os
import time
from concurrent.futures import ThreadPoolExecutor
from utils.pdf_handler import extract_text_from_pdf
from utils.summary_extractor import summarize_text
from utils.keyword_extractor import extract_keywords
from utils.db_manager import save_to_mongo

def process_pdf(pdf_path):
    start_time = time.time()  
    try:
        text = extract_text_from_pdf(pdf_path)
        summary = summarize_text(text)
        keywords = extract_keywords(text)
        
        save_to_mongo(pdf_path, summary, keywords)
        print(f"Processed {pdf_path}")

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    
    end_time = time.time()  
    print(f"Processed {pdf_path} in {end_time - start_time:.2f} seconds.")  

def process_all_pdfs(folder_path):
    start_time = time.time()  

    with ThreadPoolExecutor() as executor:
        futures = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(folder_path, filename)
                futures.append(executor.submit(process_pdf, pdf_path))

        
        for future in futures:
            future.result()

    end_time = time.time()  
    print(f"Processed all PDFs in {end_time - start_time:.2f} seconds.")  

if __name__ == "__main__":
    process_all_pdfs("tests/sample_pdfs/")
