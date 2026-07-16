# PyChronicle

An AST-Powered Time-Travel Debugger built using Python.

<<<<<<< HEAD
## Project Description
=======
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-orange)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)

PyChronicle is a Python-based debugging and code analysis tool that combines **Abstract Syntax Tree (AST) Analysis**, **Execution Tracing**, **SQLite Storage**, and **JSON Report Generation** to help developers understand how Python programs execute step by step.
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

PyChronicle is a developer tool that records the execution history of Python programs. It uses Python's `ast` module and `sys.settrace` to capture variable changes during execution, stores them in SQLite, and allows developers to inspect past program states through a terminal-based interface.

<<<<<<< HEAD
## Technologies
- Python
- AST (`ast`)
- `sys.settrace`
- SQLite
- Textual CSS
- Typer
=======
# 📑 Table of Contents

- Project Status
- Project Overview
- Why PyChronicle?
- Objectives
- Features
- Architecture
- Technologies Used
- Project Structure
- Installation
- Running the Project
- Workflow
- AST Analysis
- Sample Output
- Sample JSON Report
- Database
- Dependencies
- Development
- Roadmap
- Future Enhancements
- Team Contributions
- Team Members
- Contributing
- Acknowledgements
- License
- Contact
- Support

---

# 📌 Project Status
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

## Team
- Sarvesh Deshmukh
- Santan Kumar
- Bheemsetti Vijayalaxmi
- Yaduraj Singh Yadav

<<<<<<< HEAD
## Status
🚧 Internship Project - Under Development

## Recent Updates
=======
## Current Features

- ✅ AST Analysis
- ✅ Interactive CLI
- ✅ Execution Tracing
- ✅ SQLite Database
- ✅ JSON Report Export
- ✅ Execution History
- ✅ Structured Logging
- ✅ Modular Architecture
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

- Added AST Explorer
- Added assignment detection
- Added AST node statistics
- Improved project development workflow

## Development Status

<<<<<<< HEAD
- Development environment setup completed.
- Project dependencies installed successfully.
- Ready to start implementation.

## Features

- AST Explorer
- Variable Assignment Detection
- AST Node Counter
- JSON Report Export
- Interactive CLI
=======
Debugging Python applications can become difficult as projects grow in size and complexity.

PyChronicle simplifies this process by combining **static code analysis** with **runtime execution tracing**. It parses Python source code using the built-in **AST module**, records execution history using **SQLite**, generates structured **JSON reports**, and provides both a **Command Line Interface (CLI)** and a **Textual Terminal UI** for interacting with analysis results.

The goal is to help developers understand both the **structure** and **behavior** of Python programs without relying solely on traditional debugging methods.

---

# 💡 Why PyChronicle?

Unlike traditional debuggers that only inspect runtime execution, PyChronicle combines **AST-based static analysis** with **execution tracing**, giving developers a complete picture of how their code is written and how it behaves during execution.

It is especially useful for:

- Learning Python internals
- Debugging complex programs
- Static code analysis
- Educational purposes
- Software engineering projects
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

## Usage

Run the project:

<<<<<<< HEAD
```bash
python src/main.py
=======
- Parse Python source code using AST
- Detect variables, functions, classes, and imports
- Count AST nodes
- Trace program execution
- Store execution history in SQLite
- Export structured JSON reports
- Provide an interactive debugging interface
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

## Project Structure

<<<<<<< HEAD
PyChronicle/
│── sample_programs/
│── src/
=======
# ✨ Features

- 📂 Load Python Source Files
- 🌳 Parse Abstract Syntax Tree (AST)
- 📊 Count AST Nodes
- 🔍 Detect Variable Assignments
- 🔍 Detect Functions and Classes
- 🔄 Execution Tracing using `sys.settrace()`
- 💾 Store Execution History in SQLite
- 📄 JSON Report Generation
- 🖥 Interactive Command Line Interface
- 🎨 Textual Terminal UI
- 📝 Centralized Logging
- ⚠ Error Handling & Input Validation
- 🧩 Modular Project Architecture

---

# 🏗 Architecture

```text
                Python Source File
                        │
                        ▼
                 AST Parsing Engine
                        │
                        ▼
               Static Code Analysis
                        │
                        ▼
               Execution Tracing
                        │
                        ▼
                SQLite Database
                        │
                        ▼
               JSON Report Generator
                        │
                        ▼
          Interactive CLI / Textual UI
```

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| AST | Static Code Analysis |
| SQLite3 | Database Storage |
| JSON | Report Generation |
| pathlib | File Handling |
| Rich | CLI Interface |
| Textual | Terminal UI |
| Loguru | Logging |

---

# 📂 Project Structure

```text
PyChronicle/
│
├── docs/
│
├── sample_programs/
│   └── sample.py
│
├── src/
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)
│   ├── ast_parser.py
│   ├── database.py
│   ├── logger.py
│   ├── main.py
│   ├── tracer.py
│   ├── ui.py
│   └── utils.py
<<<<<<< HEAD
=======
│
├── tests/
├── outputs/
├── requirements.txt
├── README.md
└── pychronicle.db
```
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

## Installation

<<<<<<< HEAD
=======
# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<username>/PyChronicle.git
```

Navigate to the project

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
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)
pip install -r requirements.txt

## JSON Output

The parser can export analysis results as:

<<<<<<< HEAD
- analysis_report.json
=======
Run the CLI
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)

The report contains:

<<<<<<< HEAD
- Total AST nodes
- Variable assignments
- Analysis summary
=======
Run the Textual UI

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
        │
        ▼
Interactive CLI / Textual UI
```

---

# 🔍 AST Analysis Supports

- Variables
- Functions
- Classes
- Imports
- Loops
- Conditional Statements
- Assignments
- Expressions
- Try / Except Blocks
- Binary Operations

---

# 📊 Sample Output

```text
======================================================
Execution History
======================================================

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
  "classes": 1,
  "imports": 4
}
```

---

# 💾 Database

PyChronicle automatically creates:

```text
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

# 🧪 Development

Run tests

```bash
pytest
```

Format code

```bash
black .
```

Lint

```bash
flake8
```

---

# 🛣 Roadmap

- ✅ AST Parser
- ✅ AST Node Counting
- ✅ Variable Detection
- ✅ Function Detection
- ✅ Execution Tracer
- ✅ SQLite Storage
- ✅ JSON Export
- ✅ Interactive CLI
- ✅ Textual UI
- ✅ Logging
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
- CSV Export
- PDF Report Export
- Call Graph Visualization
- GUI Dashboard
- Multi-file Analysis
- Performance Optimization
- Plugin Support
- Improved Unit Testing

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
- Centralized Logging
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

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

git checkout -b feature/new-feature

git commit -m "feat: add new feature"

git push origin feature/new-feature
```

Then create a Pull Request.

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers behind:

- Python
- AST Module
- Rich
- Textual
- Loguru
- SQLite

---

# 📜 License

This project is licensed under the **MIT License**.

See the LICENSE file for more information.

---

# 📬 Contact

**Santan Kumar**

GitHub: https://github.com/Santan-kumar01

LinkedIn: https://www.linkedin.com/in/your-linkedin

Email: your-email@example.com

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork the project
- 🐞 Report Issues
- 💡 Suggest New Features
- 🤝 Contribute

---

<div align="center">

### 🚀 Happy Coding with PyChronicle!

**Built with ❤️ using Python**

</div>
>>>>>>> 560e6b7 (docs(readme): revamp README with comprehensive project documentation)
