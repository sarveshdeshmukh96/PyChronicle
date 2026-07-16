# 🚀 PyChronicle

> **AST-Powered Time-Travel Debugger for Python**

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-orange)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen)

PyChronicle is a Python-based debugging and code analysis tool that combines **Abstract Syntax Tree (AST) Analysis**, **Execution Tracing**, **SQLite Storage**, and **JSON Report Generation** to help developers understand how Python programs execute step by step.

---

# 📑 Table of Contents

* Project Overview
* Features
* Architecture
* Technologies
* Project Structure
* Installation
* Usage
* Workflow
* Roadmap
* Future Enhancements
* Team
* Contributing
* License

---

# 📖 Project Overview

PyChronicle is an AST-powered debugging and code analysis tool built with Python.

It combines **static code analysis** and **runtime execution tracing** to help developers understand how Python programs work internally.

The project parses Python source code using the built-in **AST module**, traces execution, stores execution history in **SQLite**, and exports analysis reports in **JSON** format.

---

# 🎯 Objectives

* Parse Python source code using AST
* Analyze program structure
* Trace execution flow
* Store execution history
* Generate JSON reports
* Provide an interactive CLI
* Simplify debugging

---

# ✨ Features

* 🌳 AST Parsing
* 📊 AST Node Counting
* 🔍 Variable Detection
* 🔍 Function Detection
* 🏛 Class Detection
* 📦 Import Analysis
* 🔄 Execution Tracing
* 💾 SQLite Storage
* 📄 JSON Report Export
* 🖥 Interactive CLI
* 🎨 Textual UI
* 📝 Centralized Logging
* ⚠ Error Handling

---

# 🏗 Architecture

```text
Python Source File
        │
        ▼
AST Parser
        │
        ▼
Static Analysis
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
CLI / Textual UI
```

---

# 🛠 Technologies Used

| Technology  | Purpose              |
| ----------- | -------------------- |
| Python 3.13 | Programming Language |
| AST         | Static Analysis      |
| SQLite3     | Database             |
| JSON        | Report Export        |
| pathlib     | File Handling        |
| Rich        | CLI                  |
| Textual     | Terminal UI          |
| Loguru      | Logging              |

---

# 📂 Project Structure

```text
PyChronicle/
│
├── docs/
├── outputs/
├── sample_programs/
│   └── sample.py
│
├── src/
│   ├── ast_parser.py
│   ├── controller.py
│   ├── database.py
│   ├── logger.py
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

Move into the project

```bash
cd PyChronicle
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Usage

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
      │
      ▼
Interactive CLI
```

---

# 📊 Sample JSON

```json
{
  "file": "sample.py",
  "total_nodes": 84,
  "functions": 3,
  "classes": 1,
  "assignments": 12
}
```

---

# 💾 Database

Automatically creates

```text
pychronicle.db
```

Tables

* sessions
* events

---

# 📦 Dependencies

* ast
* sqlite3
* pathlib
* json
* rich
* textual
* loguru

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

* ✅ AST Parser
* ✅ Execution Tracing
* ✅ SQLite Storage
* ✅ JSON Export
* ✅ Interactive CLI
* ✅ Textual UI
* ✅ Logging
* ⏳ Time Travel Replay
* ⏳ Graph Visualization
* ⏳ GUI Dashboard
* ⏳ Multi-file Analysis

---

# 🚀 Future Enhancements

* Breakpoint Support
* Interactive Debugger
* Variable State Comparison
* Call Graph Visualization
* GUI Dashboard
* CSV/PDF Export
* Plugin System
* Multi-file Analysis

---

# 🤝 Team Contributions

## Sarvesh Deshmukh

* Project Architecture
* Controller
* Textual UI

## Santan Kumar

* AST Parser
* Interactive CLI
* JSON Report Generation
* Documentation
* Logging

## Yaduraj Singh Yadav

* SQLite Database

## Bheemsetti Vijayalaxmi

* Execution Tracer

---

# 👨‍💻 Team Members

* Sarvesh Deshmukh
* Santan Kumar
* Yaduraj Singh Yadav
* Bheemsetti Vijayalaxmi

---

# 🤝 Contributing

```bash
git checkout -b feature/new-feature

git add .

git commit -m "feat: add new feature"

git push origin feature/new-feature
```

Then create a Pull Request.

---

# 🙏 Acknowledgements

Thanks to the open-source community and the developers behind:

* Python
* AST
* Rich
* Textual
* Loguru
* SQLite

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 📬 Contact

**Santan Kumar**

GitHub: https://github.com/Santan-kumar01

---

# ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the repository
* 🐛 Report Issues
* 💡 Suggest Features

---

<div align="center">

## 🚀 Happy Coding!

**Built with ❤️ using Python**

</div>
