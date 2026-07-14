# 🚀 PyChronicle

> **AST-Powered Time-Travel Debugger for Python**

PyChronicle is a Python-based debugging and code analysis tool that combines **Abstract Syntax Tree (AST) Analysis**, **Execution Tracing**, **SQLite Storage**, and **JSON Report Generation** to help developers understand how Python programs execute step by step.

---

## 📌 Project Status

**Status:** 🟢 Active Development

### Current Features

- ✅ AST Analysis
- ✅ Interactive CLI
- ✅ Execution Tracing
- ✅ SQLite Database
- ✅ JSON Report Export
- ✅ Execution History

---

# 📖 Project Overview

Debugging complex Python applications can be difficult.

PyChronicle simplifies debugging by analyzing source code using Python's built-in **AST module**, tracing program execution, storing execution history in **SQLite**, and generating structured **JSON reports** for further analysis.

The project provides developers with a better understanding of program structure and execution flow.

---

# 🎯 Objectives

- Parse Python source code using AST
- Detect variables, functions, classes, and imports
- Count AST nodes
- Trace program execution
- Store execution history
- Export analysis reports as JSON
- Provide an interactive command-line interface

---

# ✨ Features

- 📂 Load Python Source Files
- 🌳 Parse Abstract Syntax Tree (AST)
- 📊 Count AST Nodes
- 🔍 Detect Variable Assignments
- ⚙️ Execution Tracing using `sys.settrace()`
- 💾 Store Execution History in SQLite
- 📄 Export Analysis as JSON
- 🖥 Interactive Command Line Interface
- ✅ Error Handling & Input Validation

---

# 🏗 Architecture

```text
Python Source File
        │
        ▼
   AST Parser
        │
        ▼
Execution Tracer
        │
        ▼
SQLite Database
        │
        ▼
JSON Report
        │
        ▼
Interactive CLI
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| AST | Static Code Analysis |
| SQLite3 | Database |
| JSON | Report Generation |
| pathlib | File Handling |
| Rich | CLI Output |
| Textual | Terminal UI |
| Loguru | Logging |

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
git clone https://github.com/<username>/PyChronicle.git
```

Navigate to the project directory

```bash
cd PyChronicle
```

Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Run CLI

```bash
python src/main.py
```

Run Textual UI

```bash
python src/ui.py
```

---

# 🔄 Workflow

```text
Load Python File
        │
        ▼
Parse AST
        │
        ▼
Analyze Source Code
        │
        ▼
Trace Execution
        │
        ▼
Store in SQLite
        │
        ▼
Generate JSON Report
```

---

# 🔍 AST Analysis Supports

- Variables
- Functions
- Classes
- Imports
- Loops
- If Statements
- Assignments
- Expressions
- Try / Except Blocks

---

# 📊 Sample Output

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

# 📄 Sample JSON Report

```json
{
  "file": "sample.py",
  "total_nodes": 84,
  "assignments": 12,
  "functions": 3,
  "classes": 1
}
```

---

# 💾 Database

PyChronicle automatically creates

```
pychronicle.db
```

Database Tables

- sessions
- events

---

# 📦 Dependencies

- ast
- sqlite3
- pathlib
- json
- rich
- textual
- loguru

---

# 🛣 Roadmap

- ✅ AST Parser
- ✅ AST Node Counting
- ✅ Variable Detection
- ✅ Execution Tracer
- ✅ SQLite Storage
- ✅ JSON Export
- ✅ Interactive CLI
- ⏳ Breakpoints
- ⏳ Time Travel Replay
- ⏳ Graph Visualization
- ⏳ GUI Dashboard
- ⏳ Multi-file Analysis

---

# 🚀 Future Enhancements

- Interactive Debugger
- Breakpoint Support
- Time Travel Replay
- Variable State Comparison
- CSV/PDF Report Export
- Call Graph Visualization
- GUI Dashboard
- Multi-file Analysis
- Improved Logging
- Increased Unit Test Coverage

---

# 🤝 Team Contributions

## Sarvesh Deshmukh

- Project Architecture
- Controller Design
- Utilities
- Textual UI Development

## Santan Kumar

- AST Parser
- Interactive CLI
- JSON Report Generation
- Project Documentation
- Merge Conflict Resolution

## Yaduraj Singh Yadav

- SQLite Database
- Database Integration

## Bheemsetti Vijayalaxmi

- Execution Tracer
- Trace Management

---

# 👨‍💻 Team Members

- Sarvesh Deshmukh
- Santan Kumar
- Yaduraj Singh Yadav
- Bheemsetti Vijayalaxmi

---

# 📜 License

This project is developed for educational and internship purposes.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy Coding! 🚀