import sys
import re
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_text(file_path):
    """
    Load text from a plain text file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using pdfplumber.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

def extract_job_requirements(job_desc_text):
    "Simply return the entire job description"
    return job_desc_text


def compute_similarity_score(text_a, text_b):
    """
    Compute a TF-IDF cosine similarity score (0 to 100).
    """
    vectorizer = TfidfVectorizer().fit_transform([text_a, text_b])
    similarity_matrix = cosine_similarity(vectorizer[0], vectorizer[1])
    score = similarity_matrix[0][0]
    return round(score * 100, 2)

def main():
    # Usage: python main.py job_description.txt resume.pdf
    if len(sys.argv) != 3:
        print("Usage: python main.py <job_description.txt> <resume.pdf>")
        sys.exit(1)

    job_desc_file = sys.argv[1]
    resume_file = sys.argv[2]

    job_desc_text = load_text(job_desc_file)
    resume_text = extract_text_from_pdf(resume_file)
    job_requirements_text = extract_job_requirements(job_desc_text)
    match_score = compute_similarity_score(job_requirements_text, resume_text)

    #print("========== Job Requirements (Extracted) ==========")
    #print(job_requirements_text)
    #print("\n========== Resume (Extracted) ==========")
    #print(resume_text)
    print(f"Match Score: {match_score}%")

if __name__ == "__main__":
    main()