from docx import Document

doc = Document(r'c:\Users\USER\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\sessions\3A86E80DA81F8145A67C15BB277DFACBC9CC930D\transfers\2026-08\NumericalReport.docx')
for i, para in enumerate(doc.paragraphs):
    print(f'[{i}] [{para.style.name}] {para.text}')
