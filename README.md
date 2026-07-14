# 🚀 PyChronicle

**PyChronicle** is an AST-Powered Time-Travel Debugger built using Python. It analyzes Python source code, records execution traces, stores execution history in SQLite, and helps developers understand how a program executes step by step.

---

# 🚧 Project Status

**Status:** Active Development

### Latest Features

- ✅ Interactive CLI
- ✅ AST Analysis
- ✅ Execution Tracer
- ✅ SQLite Database
- ✅ JSON Report Generation
- ✅ Execution History

---

# 📖 Project Overview

Debugging is one of the most important phases of software development.

PyChronicle combines multiple Python technologies to provide a better understanding of program execution.

The project integrates:

- Abstract Syntax Tree (AST)
- Execution Tracing
- SQLite Database
- JSON Report Generation
- Interactive CLI

This helps developers inspect how their Python code executes and how variables change over time.

---

# 🎯 Objectives

- Parse Python source code using AST
- Detect variables, functions, imports and classes
- Count AST nodes
- Execute Python programs with tracing
- Store execution history
- Generate JSON reports
- Provide an interactive command-line interface

---

# ✨ Features

- ✅ Load Python Source File
- ✅ Parse Abstract Syntax Tree
- ✅ Detect Variable Assignments
- ✅ Count AST Nodes
- ✅ Export JSON Analysis Report
- ✅ Execution Tracing using `sys.settrace()`
- ✅ SQLite Database Storage
- ✅ View Previous Execution History
- ✅ Interactive CLI
- ✅ Error Handling & Input Validation

---

# 🏗 Project Architecture

```
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

- Python 3.13
- AST
- SQLite3
- JSON
- pathlib
- Rich
- Textual
- Loguru

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

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

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

# 🔄 Project Workflow

```
Load Python File
        │
        ▼
Parse AST
        │
        ▼
Analyze Source Code
        │
        ▼
Run Execution Tracer
        │
        ▼
Save Execution History
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
- Expressions
- Try / Except
- Assignments

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

# 🚀 Future Enhancements

- Interactive Debugger
- Time Travel Replay
- Variable State Comparison
- Breakpoints
- Search Execution History
- CSV Export
- Multi-file Analysis
- Call Graph Visualization
- GUI Dashboard

---

# 🗺 Roadmap

- [x] AST Parser
- [x] AST Node Counting
- [x] Variable Detection
- [x] Execution Tracer
- [x] SQLite Storage
- [x] JSON Export
- [x] Interactive CLI
- [ ] GUI Application
- [ ] Breakpoints
- [ ] Time Travel Replay
- [ ] Graph Visualization

---

# 📈 Repository Highlights

- Python Project
- Team Collaboration
- Git & GitHub Workflow
- AST Analysis
- Execution Tracing
- SQLite Database
- JSON Export
- Interactive CLI

---

# 🤝 Team Contributions

### Sarvesh Deshmukh

- Project Architecture
- Utilities
- UI Development

### Santan Kumar

- AST Parser
- CLI Workflow
- JSON Report Generation
- Documentation
- Merge Conflict Resolution

### Yaduraj Singh Yadav

- SQLite Database

### Bheemsetti Vijayalaxmi

- Execution Tracer

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

# 📌 Known Limitations

- Currently supports Python source code analysis only.
- GUI-based debugging is under development.
- Multi-file project analysis is not yet implemented.
- Breakpoint management and time-travel replay features are planned for future releases.
- Performance optimization for large Python projects is still in progress.

---

# 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes following the project coding standards.
4. Commit your changes using meaningful commit messages.
5. Push your branch and create a Pull Request.

---

# 🙌 Acknowledgements

This project was developed as part of the **Infotact Solutions Python Development Internship**.

Special thanks to all team members for their collaboration, code reviews, testing, documentation, and continuous improvements throughout the project.

---

# 👥 Team Members

- **Sarvesh Deshmukh** — Project Architecture, Utilities, UI Development
- **Santan Kumar** — AST Parser, Interactive CLI, JSON Report Generation, Documentation, Merge Conflict Resolution
- **Yaduraj Singh Yadav** — SQLite Database Implementation
- **Bheemsetti Vijayalaxmi** — Execution Tracer Development

---

# 📬 Contact

For bug reports, feature requests, or project-related discussions, please create an issue in the GitHub repository.

---

# ⭐ Support the Project

If you found **PyChronicle** useful, please consider giving this repository a ⭐ on GitHub.

Your support motivates the team to continue improving the project.

---

**PyChronicle — AST-Powered Time-Travel Debugger for Python**