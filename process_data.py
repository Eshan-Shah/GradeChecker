import fitz  # PyMuPDF
import os
import pandas as pd

def extract_text_from_pdfs(folder_path):
    extracted_data = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            doc_path = os.path.join(folder_path, file_name)
            with fitz.open(doc_path) as doc:
                for page in doc:
                    text = page.get_text()
                    extracted_data.append({
                        "file": file_name,
                        "page": page.number + 1,
                        "text": text
                    })
    
    return pd.DataFrame(extracted_data)

# Example usage:
df = extract_text_from_pdfs("./pdfs/edexcel/")
df.to_csv("edexcel_raw_extracted.csv", index=False)
