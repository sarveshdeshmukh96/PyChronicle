# 🚀 PyChronicle

> **An AST-Powered Time-Travel Debugger for Python**

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-orange)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

---

## 📖 Overview

**PyChronicle** is an AST-powered Python debugging and code analysis tool that combines **Static Code Analysis** with **Runtime Execution Tracing**.

The project helps developers understand how Python code executes by analyzing its **Abstract Syntax Tree (AST)**, tracing execution, storing runtime history in **SQLite**, and generating structured **JSON reports**.

---

# ✨ Features

- 🌳 Abstract Syntax Tree (AST) Parsing
- 🔍 Variable Assignment Detection
- 📊 AST Node Counting
- 🧠 Function & Class Detection
- 🔄 Runtime Execution Tracing
- 💾 SQLite Database Integration
- 📄 JSON Report Generation
- 🖥 Interactive Command Line Interface (CLI)
- 🎨 Textual Terminal User Interface
- 📝 Centralized Logging
- ⚠ Error Handling
- 📂 Modular Project Architecture

---

# 🏗 Architecture

```text
             Python Source Code
                     │
                     ▼
              AST Parser Engine
                     │
                     ▼
          Static Code Analysis
                     │
                     ▼
            Execution Tracer
                     │
                     ▼
              SQLite Database
                     │
                     ▼
          JSON Report Generator
                     │
                     ▼
          CLI / Textual Interface
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13 | Programming Language |
| AST | Static Code Analysis |
| SQLite | Database |
| JSON | Report Export |
| Rich | CLI Interface |
| Textual | Terminal UI |
| Loguru | Logging |

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
git clone https://github.com/sarveshdeshmukh96/PyChronicle.git
```

Move into the project

```bash
cd PyChronicle
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

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
Store Results
        │
        ▼
Generate JSON Report
        │
        ▼
Display via CLI / UI
```

---

# 📊 Supported AST Analysis

- Variables
- Functions
- Classes
- Imports
- Loops
- Conditional Statements
- Assignments
- Expressions
- Binary Operations
- Try / Except Blocks

---

# 📄 Sample JSON Output

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

PyChronicle stores execution history inside SQLite.

Database Tables

- sessions
- events

---

# 📦 Dependencies

- ast
- sqlite3
- json
- pathlib
- rich
- textual
- loguru

---

# 🧪 Development

Run Tests

```bash
pytest
```

Format Code

```bash
black .
```

Lint

```bash
flake8
```

---

# 🗺 Roadmap

- ✅ AST Parsing
- ✅ Variable Detection
- ✅ Function Detection
- ✅ AST Statistics
- ✅ Runtime Tracing
- ✅ SQLite Integration
- ✅ JSON Reports
- ✅ Interactive CLI
- ✅ Textual UI
- ✅ Logging
- ⏳ Time Travel Replay
- ⏳ Breakpoints
- ⏳ Graph Visualization
- ⏳ GUI Dashboard
- ⏳ Multi-file Analysis

---

# 🚀 Future Enhancements

- Interactive Debugger
- Breakpoint Support
- GUI Dashboard
- Performance Improvements
- Plugin Support
- PDF Report Export
- CSV Report Export
- Multi-file Analysis
- Call Graph Visualization

---

# 👥 Team

| Member | Contribution |
|---------|--------------|
| Sarvesh Deshmukh | Project Architecture, UI, Utilities |
| Santan Kumar | AST Parser, CLI, JSON Reports, Documentation |
| Yaduraj Singh Yadav | SQLite Database |
| Bheemsetti Vijayalaxmi | Execution Tracing |

---

# 🤝 Contributing

Contributions are welcome.

```bash
git checkout -b feature/new-feature

git commit -m "feat: add new feature"

git push origin feature/new-feature
```

Then create a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🙏 Acknowledgements

Special thanks to the Python open-source community and the maintainers of:

- Python
- AST
- Rich
- Textual
- SQLite
- Loguru

---

# 📬 Contact

**Santan Kumar**

- GitHub: https://github.com/Santan-kumar01
- LinkedIn: https://www.linkedin.com/in/santan-kumar/
- Email: santank108@gmail.com

---

<div align="center">

## ⭐ If you like this project, don't forget to Star the repository!

**Built with ❤️ using Python**

</div>