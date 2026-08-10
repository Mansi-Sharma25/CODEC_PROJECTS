# Automated Resume Parser

An automated resume parsing system built with Python that extracts important candidate information from PDF resumes. The project uses **PDFPlumber** to read resume content and **Regular Expressions** to identify contact details, while keyword-based matching is used to detect skills and education-related information.

## 📌 Project Overview

The parser reads the resume, extracts its useful information, and identifies:

* Candidate Name
* Email Address
* Phone Number
* Technical Skills
* Education-related Information

The extracted information is returned in a structured format that can be further used for candidate screening or storage.

## ✨ Features

* 📄 Extracts text from PDF resumes
* 👤 Identifies the candidate's name
* 📧 Extracts email addresses
* 📱 Extracts Indian phone numbers
* 💻 Detects predefined technical skills
* 🎓 Identifies education-related keywords
* 📊 Returns extracted information in structured dictionary format
* ⚡ Simple and lightweight Python implementation

## 🛠️ Technologies Used

* **Python**
* **HTML**
* **CSS**
* **SQLite**
* **PDFPlumber** – for extracting text from PDF files
* **Regular Expressions (Regex)** – for extracting emails and phone numbers
* **Keyword Matching** – for identifying skills and education information

## 📂 Project Structure

```text
Automated-Resume-Parser/
│
├── resume_parser.py
├── resume.pdf
├── requirements.txt
└── README.md
```

> `resume.pdf` is only an example/test resume. You can replace it with any PDF resume you want to analyze.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Automated-Resume-Parser.git
```

### 2. Open the Project Folder

```bash
cd Automated-Resume-Parser
```

### 3. Install Required Library

```bash
pip install pdfplumber
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

### Example Output

```text
{
    'Name': 'Mansi Sharma',
    'E-mail': ['example@gmail.com'],
    'Phone': ['9876543210'],
    'Skills': ['Python', 'C++', 'HTML', 'CSS'],
    'Education': ['B.Tech']
}
```

## 🔍 How the Parser Works

### 1. PDF Text Extraction

PDFPlumber opens the resume PDF and extracts text from each page.

```python
with pdfplumber.open(pdf_path) as resume_file:
```

The text from all pages is combined into a single string.

### 2. Email Extraction

Regular Expressions are used to find email addresses from the extracted text.

```python
emails = re.findall(r"\w+@\w+\.\w+", all_text)
```

### 3. Phone Number Extraction

The parser searches for Indian mobile numbers, including formats with optional `+91`, spaces, or hyphens.

### 4. Name Extraction

The first line of the extracted resume text is considered the candidate's name.

```python
lines = all_text.split('\n')
name = lines[0]
```

### 5. Skills Detection

The parser checks the extracted resume text against a predefined list of technical skills such as:

* Python
* C++
* Java
* SQL
* Flask
* Django
* HTML
* CSS
* JavaScript

If a skill is found in the resume, it is added to the extracted skills list.

### 6. Education Detection

The parser searches for education-related keywords such as:

* B.Tech
* B.E.
* M.Tech
* MCA
* BCA
* Bachelor
* Master

The detected keywords are stored in the education section of the output.

## 📋 Extracted Information

| Information | Extraction Method            |
| ----------- | ---------------------------- |
| Name        | First line of extracted text |
| Email       | Regular Expression           |
| Phone       | Regular Expression           |
| Skills      | Keyword Matching             |
| Education   | Keyword Matching             |

## 🎯 Project Outcome

The project demonstrates how resume data can be automatically extracted and organized using Python. It can serve as a basic foundation for an automated resume screening system where candidate information can later be stored, searched, and analyzed.

## 🚀 Future Improvements

The project can be extended with:

* Support for DOC/DOCX resumes
* More advanced skill extraction
* NLP-based resume analysis using spaCy
* Web interface using Flask
* Database integration using PostgreSQL or SQLite
* Searchable candidate database
* Improved name and education extraction
* Resume ranking based on required skills

## 👩‍💻 Author

**Mansi Sharma**

This project was developed as a part of **Codec Python-Developer Internship.** 

