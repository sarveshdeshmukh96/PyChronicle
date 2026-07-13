# 🚀 PyChronicle

**PyChronicle** is an AST-Powered Time-Travel Debugger built using Python. It analyzes Python source code, records execution traces, stores execution history in SQLite, and helps developers understand how a program executes step by step.

---

# 📖 Project Overview

Debugging is an important part of software development. Traditional debuggers only show the current execution state.

PyChronicle aims to provide execution history by combining:

- Abstract Syntax Tree (AST) Analysis
- Execution Tracing
- SQLite Database Storage
- JSON Report Generation

This allows developers to inspect how variables change during execution.

---

# 🎯 Objectives

- Parse Python source code using AST
- Detect variables, functions, imports, and classes
- Trace program execution
- Store execution history
- Generate JSON analysis reports
- Provide an easy-to-use interface

---

# ✨ Features

✅ Load Python Source File

✅ Parse Abstract Syntax Tree (AST)

✅ Detect Variable Assignments

✅ Count AST Nodes

✅ Export Analysis Report to JSON

✅ Execution Tracing using `sys.settrace()`

✅ Store Execution History in SQLite

✅ View Previous Execution Sessions

---

# 🛠 Technologies Used

- Python 3.13
- AST Module
- SQLite3
- Textual
- Rich
- Loguru
- JSON

---

# 📂 Project Structure

```text
PyChronicle/
│
├── docs/
├── sample_programs/
│   └── sample.py
│
├── src/
│   ├── ast_parser.py
│   ├── controller.py
│   ├── database.py
│   ├── main.py
│   ├── tracer.py
│   ├── ui.py
│   ├── ui.tcss
│   └── utils.py
│
├── tests/
├── requirements.txt
├── README.md
└── pychronicle.db
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd PyChronicle
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Run the application

```bash
python src/main.py
```

Run the Textual UI

```bash
python src/ui.py
```

---

# 📊 Example Output

```
Execution History

Session ID : 3
File       : sample.py
Executed   : 13-07-2026

Session ID : 2
File       : sample.py
Executed   : 13-07-2026
```

---

# 💾 Database

The project automatically creates

```
pychronicle.db
```

Tables

- sessions
- events

---

# 📄 JSON Report

AST analysis is exported to

```
analysis_report.json
```

---

# 🚀 Future Enhancements

- Interactive Debugger
- Time Travel Execution
- Variable State Comparison
- Search Execution History
- CSV Export
- Multi-file Analysis
- Graphical Timeline
- Breakpoints
- Call Graph Visualization

---

# 👨‍💻 Team Members

- Sarvesh Deshmukh
- Santan Kumar
- Bheemsetti Vijayalaxmi
- Yaduraj Singh Yadav

---

# 📜 License

This project is developed for educational and internship purposes.

---

# ⭐ PyChronicle

**AST-Powered Time-Travel Debugger for Python**