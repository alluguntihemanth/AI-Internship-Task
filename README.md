# 📚 **AI Internship Task: PDF Processing Pipeline**  

---

## 🌟 **About the Project**  
The Task focuses on creating a **PDF Processing Pipeline** that handles PDF files for summarization and keyword extraction. Designed to efficiently manage PDF documents, this project utilizes custom algorithms and MongoDB for data storage and retrieval.

---

## ✨ **Key Features**  
- **PDF Parsing**: Extracts text from various PDF formats.  
- **Custom Summarization**: Generates concise summaries from extracted text.  
- **Keyword Extraction**: Identifies and retrieves important keywords from the documents.  
- **MongoDB Integration**: Stores processed data for easy access and retrieval.  
- **Test Suite**: Includes a set of sample PDFs to validate functionality.

---

## ⚙️ **Tech Stack**  
| **Technology**      | **Purpose**                               |  
|---------------------|-------------------------------------------|  
| **Python**          | Main programming language for development |  
| **MongoDB**         | Database for storing processed data       |  
| **Custom Scripts**   | Scripts for PDF handling, summarization, and keyword extraction |  

---

## 📁 **Directory Structure**  
D:/ai-intern-task/  
│  
├── main.py                      # Main script to run the pipeline  
├── requirements.txt             # Dependencies required for the project  
│  
├── utils/                       # Utility functions and scripts  
│   ├── __pycache__/             # Cache for compiled Python files (can be ignored)  
│   ├── db_manager.py            # MongoDB integration and JSON updates  
│   ├── keyword_extractor.py      # Custom keyword extraction logic  
│   ├── pdf_handler.py           # Handles PDF parsing and text extraction  
│   └── summary_extractor.py      # Custom summarization logic  
│  
├── tests/                       # Directory for test-related files  
│   ├── __pycache__/             # Cache for compiled Python files (can be ignored)  
│   ├── sample_pdfs/            # Sample PDF files for testing  
│   └── test_pipeline.py         # Test script for the pipeline  
│  
└── .gitignore                   # Specifies files and directories to ignore in Git  
---

## 🚀 **Run the Application**  
1. **Prerequisites**  
   - Install [Python](https://www.python.org/downloads/).  
   - Install the required packages:  
     ```bash
     pip install -r requirements.txt
     ```

2. **Launch the Application**  
   - Navigate to the project directory:  
     ```bash
     cd D:/ai-intern-task
     ```
   - Run the main script:  
     ```bash
     python main.py
     ```

---

## 💬 **How It Works**  
1. **PDF Input**: Users provide PDF files for processing.  
2. **Text Extraction**: The pipeline extracts text from the PDFs.  
3. **Summarization and Keywords**: It generates summaries and extracts keywords from the text.  
4. **Data Storage**: Processed data is stored in MongoDB for easy retrieval.

---

## 📄 **License**  
This project is licensed under the **Apache 2.0 License**. See the [LICENSE](LICENSE) file for details.  

---

## 📧 **Contact**  
For any queries, reach out to:  
**Email**: hemanthallugunti@gmail.com  
**LinkedIn**: [Hemanth Reddy Allugunti](https://www.linkedin.com/in/hemanth-reddy-allugunti-883b36216/)  

---

Happy PDF processing! 📄✨
