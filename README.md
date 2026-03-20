# 🎓 Student Analytics Dashboard (Tkinter Project)

A simple and interactive **Student Management & Analytics Dashboard** built using **Python Tkinter GUI**.
This application allows users to add student data, calculate performance, and visualize basic analytics like topper and lowest scorer.

---

## 🚀 Features

* ➕ Add student with marks (comma-separated)
* 🧮 Automatic calculation of:

  * Total marks
  * Average marks
  * Grade (O, E, A, B, C, D)
* 🥇 Displays Topper
* ⚠️ Displays Lowest Scorer
* 🗑️ Delete selected student
* 💾 Save data to CSV file
* 🎨 Beautiful dark-themed GUI interface

---

## 🖼️ Interface Overview

* Clean and modern UI
* Table view using Treeview
* Colorful buttons and labels
* Real-time updates

---

## 📂 Project Structure

```
student-analytics-dashboard/
│
├── main.py                # Main application file
├── students_report.csv   # Generated output file (after saving)
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/student-analytics-dashboard.git
cd student-analytics-dashboard
```

### 2️⃣ Install dependencies

No external libraries required (uses built-in Python modules)

```
pip install tkinter
```

*(Note: Tkinter usually comes pre-installed with Python)*

---

### 3️⃣ Run the application

```
python main.py
```

---

## 🧑‍💻 How to Use

1. Enter **Student Name**
2. Enter **Marks (comma separated)**
   Example: `80,90,85`
3. Click **➕ Add**
4. View data in the table
5. Select a student and click **🗑️ Delete** to remove
6. Click **💾 Save CSV** to export data

---

## 📊 Grade System

| Average Marks | Grade |
| ------------- | ----- |
| 90+           | O     |
| 80–89         | E     |
| 70–79         | A     |
| 60–69         | B     |
| 50–59         | C     |
| Below 50      | D     |

---

## 🛠️ Technologies Used

* Python 🐍
* Tkinter (GUI)
* ttk (Treeview)
* CSV module

---

## 📌 Future Improvements

* 📊 Add graphs (Matplotlib)
* 🔍 Search functionality
* ✏️ Edit student details
* 🌙 Light/Dark mode toggle
* 📁 Load CSV file support

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is open-source and free to use.
This project is licensed under the MIT License.

---

## 🙌 Author

Mridul Saha

* GitHub: https://github.com/MRIDUL11-prog

---

⭐ If you like this project, give it a star on GitHub!
