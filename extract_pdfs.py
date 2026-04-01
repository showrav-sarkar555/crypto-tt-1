import importlib.util
import sys
from pathlib import Path

files = [
    'Lecture 1 (1).pdf',
    'Lecture 2.pdf',
    'Lecture_4.pdf',
    'Lecture_6.pdf',
    'PlayFair _Hill_Vigenère_cipher .pdf',
    'Unicity_Distance.pdf',
    'Sample Problem (1).pdf',
]

if importlib.util.find_spec('pypdf') is None:
    print('MISSING_PYPDF')
    sys.exit(2)

from pypdf import PdfReader

out = Path('extracted_text')
out.mkdir(exist_ok=True)

for name in files:
    pdf_path = Path(name)
    reader = PdfReader(str(pdf_path))
    chunks = []
    for idx, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ''
        except Exception as exc:
            text = f'[ERROR page {idx}: {exc}]'
        chunks.append(f'\n\n===== PAGE {idx} =====\n{text}')

    txt_path = out / f'{pdf_path.stem}.txt'
    txt_path.write_text(''.join(chunks), encoding='utf-8')
    print(f'{pdf_path} -> {txt_path} ({len(reader.pages)} pages)')

print('DONE')
