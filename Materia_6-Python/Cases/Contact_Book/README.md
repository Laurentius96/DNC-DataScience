<div align="center">
  <h1>Contact Book</h1>
  <p><i>A contact management application developed in Python, demonstrating fundamental programming concepts and data manipulation.</i></p>
</div>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-technologies-used">Technologies</a> •
  <a href="#-project-structure">Project Structure</a> •
  <a href="#-how-to-run">How to Run</a> •
  <a href="#-implementation-details">Implementation Details</a> •
  <a href="#-learnings">Learnings</a> •
  <a href="#-license">License</a> •
  <a href="#-educational-resources">Educational Resources</a>
</p>

## 🔍 Overview

This project implements a complete digital contact book using Python. The application allows users to manage personal contacts through an interactive command-line interface, with features to add, view, edit, and remove contacts, as well as persist data in JSON format.

The project demonstrates fundamental programming concepts such as:
- Data collection and manipulation
- Data structures (lists and dictionaries)
- Functions and code modularization
- Data persistence with JSON
- Command-line user interface

## 🛠️ Features

- **Add contacts**: Register new contacts with name, phone, and email
- **List contacts**: View all stored contacts
- **Search contacts**: Find contacts by name or partial name
- **Edit contacts**: Update information for existing contacts
- **Remove contacts**: Delete contacts from the address book
- **Data persistence**: Save and load contacts in JSON file

## 💻 Technologies Used

- **Python**: Main programming language
- **JSON**: Format for persistent data storage
- **Libraries**:
  - `json`: For JSON file manipulation
  - `os`: For operating system operations
  - `time`: For visual effects in the interface

## 📋 Project Structure

```
Contact_Book/
├── main.ipynb      # Main notebook with application code
├── book.json       # Contact storage file
├── LICENSE.md      # Project license
└── README.md       # Project documentation
```

## 🚀 How to Run

1. Clone this repository:
   ```
   git clone https://github.com/Laurentius96/Contact_Book.git
   ```

2. Navigate to the project directory:
   ```
   cd Contact_Book
   ```

3. Run the `main.ipynb` notebook in a Jupyter environment:
   ```
   jupyter notebook main.ipynb
   ```

4. Alternatively, run the script directly:
   ```
   python -m main.py
   ```

## 📊 Implementation Details

### User Interface
The application uses a command-line interface with visual elements to improve the user experience:
- Formatted headers
- Success, error, and information messages
- Stylized contact display
- Interactive menu

### Data Management
Contacts are stored as Python dictionaries within a list, with the following structure:
```python
{
  "name": "Contact Name",
  "phone": "Contact Phone",
  "email": "Contact Email"
}
```

### Persistence
The application automatically saves contacts to a JSON file (`book.json`), allowing data to be maintained between executions.

## 🎓 Learnings

This project demonstrates the practical application of various fundamental programming concepts:
- Data structure manipulation
- Functions and code modularization
- Exception handling
- Data persistence
- Command-line user interface
- User input validation

## 📜 License

This project is part of DNC's educational curriculum and is available for learning purposes.

<details open>
<summary><b>CC BY-NC-ND 4.0 License</b></summary>

This repository is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

### What this means:

- ✅ **You can share** — You are free to copy and redistribute the material in any medium or format
- ❌ **No commercial use** — You may not use the material for commercial purposes
- ❌ **No derivatives** — You may not remix, transform, or build upon the material
- ✅ **Attribution required** — You must give appropriate credit, provide a link to the license, and indicate if changes were made

For the complete license terms, please see the [LICENSE.md](LICENSE.md) file.
</details>

## 🎓 Educational Resources

- **Python Documentation**: [python.org](https://docs.python.org/)
- **Jupyter Notebook Guide**: [jupyter.org](https://jupyter.org/documentation)
- **Data Structures Tutorial**: Additional learning materials in the notebook

---

<div align="center">
  <p><b>Developed with 💙 by <a href="https://github.com/Laurentius96">Lorenzo C. Bianchi</a> feat. DNC Educational Team</b></p>
  <p><i>Learning through practice - building real solutions with code!</i></p>
</div>
