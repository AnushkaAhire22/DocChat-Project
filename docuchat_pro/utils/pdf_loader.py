import fitz  # PyMuPDF

def load_and_chunk_pdfs(files):
    text_chunks = []
    for file in files:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        # Chunking into 500-word chunks
        chunks = [full_text[i:i+1000] for i in range(0, len(full_text), 1000)]
        text_chunks.extend(chunks)
    return text_chunks


# #for highliegheted pdf
# def load_and_chunk_pdfs(files):
#     all_chunks = []
#     chunk_meta = []

#     for file_index, file in enumerate(files):
#         doc = fitz.open(stream=file.read(), filetype="pdf")

#         for page_num, page in enumerate(doc):
#             text = page.get_text()
#             chunks = [text[i:i + 500] for i in range(0, len(text), 500)]

#             for chunk in chunks:
#                 all_chunks.append(chunk)
#                 chunk_meta.append({
#                     "file_index": file_index,
#                     "page_num": page_num,
#                     "chunk_text": chunk
#                 })

#     return all_chunks, chunk_meta
