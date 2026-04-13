import sys
import subprocess
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QVBoxLayout
)

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenModelica Runner")
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.label1 = QLabel("Select Executable:")
        self.path_input = QLineEdit()
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_file)

        self.label2 = QLabel("Start Time:")
        self.start_input = QLineEdit()

        self.label3 = QLabel("Stop Time:")
        self.stop_input = QLineEdit()

        self.run_btn = QPushButton("Run Simulation")
        self.run_btn.clicked.connect(self.run_simulation)

        layout.addWidget(self.label1)
        layout.addWidget(self.path_input)
        layout.addWidget(self.browse_btn)
        layout.addWidget(self.label2)
        layout.addWidget(self.start_input)
        layout.addWidget(self.label3)
        layout.addWidget(self.stop_input)
        layout.addWidget(self.run_btn)

        self.setLayout(layout)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName()
        self.path_input.setText(file_path)

    def run_simulation(self):
        exe = self.path_input.text()
        start = self.start_input.text()
        stop = self.stop_input.text()

        try:
            # 🔥 VALIDATION
            if not start.isdigit() or not stop.isdigit():
                print("Start/Stop must be integers")
                return

            start = int(start)
            stop = int(stop)

            if not (0 <= start < stop < 5):
                print("Condition failed: 0 <= start < stop < 5")
                return

            exe_folder = os.path.dirname(exe)

            command = [
                exe,
                f"-startTime={start}",
                f"-stopTime={stop}",
                "-outputFormat=mat"
            ]

            print("Running:", command)

            subprocess.run(command, cwd=exe_folder)

            print("Simulation completed ✅")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())