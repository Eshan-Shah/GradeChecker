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
