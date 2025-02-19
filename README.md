# resume-grader

This project is a Python-based resume parser and grader that extracts skills, experience and projects from resumes. It then compares the resume against a job description to generate a match score, similar to ATS.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yavrohatgi/resume-grader
   cd resume-grader
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Prepare Input Files
Place the job_description.txt and resume.pdf in the project folder. Feel free to update them for different jobs.

4. Run the program:
   ```bash
   python3 main.py job_description.txt resume.pdf
   ```