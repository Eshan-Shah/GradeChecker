import fitz as pdfreader

data_paths = [
    "data/ALEVEL_AQA.pdf",
    "data/ALEVEL_EDEXCEL.pdf",
    "data/ALEVEL_OCR.pdf",
    "data/GCSE_AQA.pdf",
    "data/GCSE_EDEXCEL.pdf",
    "data/GCSE_OCR.pdf"
]

def convert_to_path(level, board, filetype=".pdf"):
    path = "data/"
    path += level.upper() + '_' + board.upper() + filetype
    return path

def split_by_subject_marker(data_list, subject):
    subject = subject.lower()
    chunks = []
    current_chunk = []

    for item in data_list:
        if subject in item.lower():
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = [] 
        else:
            current_chunk.append(item)

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def extract_gcse_aqa_data(path, subject):
    doc = pdfreader.open(path)
    extracted_lines = []

    subject = subject.lower()  

    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        lines = text.splitlines()

        for i, line in enumerate(lines):
            if subject in line.lower():
                extracted_lines.append(line)
                extracted_lines += lines[i+1:i+6]  # next few lines likely contain data

    # Extract first relevant chunk after filtering
    subject_chunks = split_by_subject_marker(extracted_lines, subject)
    if not subject_chunks:
        return None  # or raise an exception / return empty dict
    
    boundaries = subject_chunks[0]

    # Clean and cast to integers
    clean_values = [int(val) for val in boundaries if val.isdigit()]
    
    if not clean_values or len(clean_values) < 2:
        return None  # not enough data

    max_mark = clean_values[0]
    grade_marks = clean_values[1:]

    # GCSE grades 9 to (9 - len(grade_marks) + 1)
    start_grade = 9
    grades = {}

    for i, mark in enumerate(grade_marks):
        grade = start_grade - i
        grades[grade] = mark / max_mark

    return grades


    

    
