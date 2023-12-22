from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel, QSpinBox, QSlider, QHBoxLayout, QCheckBox, QFileDialog, QScrollArea
from PyQt5.QtCore import Qt


class AppWindow(QMainWindow):
    def __init__(self, submit_callback, save_callback):
        super().__init__()
        self.setWindowTitle("PyQt Interface - OpenAI Chat")
        # self.setGeometry(100, 100, 600, 350)
        self.setGeometry(100, 100, 800, 600)

        # Store the submit_callback function
        self.submit_callback = submit_callback
        self.save_callback = save_callback
        
        # Create layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)  # Add some margins around the layout
        layout.setSpacing(10)  # Add spacing between widgets

        # Create widgets for input and submit
        self.input_line = QLineEdit(self)
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.on_submit_click)

        # Add a Save to .docx button
        self.save_button = QPushButton('Save to .docx', self)
        self.save_button.clicked.connect(self.on_save_click)

        # Create widgets and layout for max_tokens
        self.max_tokens_checkbox = QCheckBox("Specify Max Tokens", self)
        self.max_tokens_checkbox.stateChanged.connect(self.max_tokens_checkbox_changed)
        self.max_tokens_spin = QSpinBox(self)
        self.max_tokens_spin.setMinimum(1)
        self.max_tokens_spin.setMaximum(9999)
        self.max_tokens_spin.setValue(100)
        self.max_tokens_spin.setEnabled(False)  # Disabled by default
        max_tokens_layout = QHBoxLayout()
        max_tokens_layout.addWidget(self.max_tokens_checkbox)
        max_tokens_layout.addWidget(self.max_tokens_spin)

        # Create widgets and layout for temperature
        self.temperature_checkbox = QCheckBox("Specify Temperature", self)
        self.temperature_checkbox.stateChanged.connect(self.temperature_checkbox_changed)
        self.temperature_slider = QSlider(Qt.Horizontal, self)
        self.temperature_slider.setMinimum(0)
        self.temperature_slider.setMaximum(200)
        self.temperature_slider.setValue(70)
        self.temperature_slider.setTickPosition(QSlider.TicksBelow)
        self.temperature_slider.setTickInterval(10)
        self.temperature_slider.setEnabled(False)  # Disabled by default
        self.temperature_value_label = QLabel("0.7", self)  # Display initial value
        self.temperature_slider.valueChanged.connect(self.update_temperature_label)
        temperature_layout = QHBoxLayout()
        temperature_layout.addWidget(self.temperature_checkbox)
        temperature_layout.addWidget(self.temperature_slider)
        temperature_layout.addWidget(self.temperature_value_label)

        # Ensure consistent height for controls
        self.max_tokens_spin.setFixedHeight(25)
        self.temperature_slider.setFixedHeight(25)
        self.temperature_value_label.setFixedHeight(25)
        self.temperature_checkbox.setFixedHeight(25)
        self.max_tokens_checkbox.setFixedHeight(25)

        # Output label
        self.output_label = QLabel("Enter your question and press submit.", self)
        self.output_label.setWordWrap(True)  # Enable word wrap

        # Scroll Area for output label
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        layout_scroll_area = QVBoxLayout(self.scroll_area_widget_contents)
        layout_scroll_area.addWidget(self.output_label)
        
        # Add widgets to layout
        layout.addWidget(self.input_line)
        layout.addLayout(max_tokens_layout)
        layout.addLayout(temperature_layout)
        # layout.addWidget(self.submit_button)
        # layout.addWidget(self.scroll_area)

        # Create a horizontal layout for the buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()  # Add a stretchable space before the buttons (pushes them to center)
        buttons_layout.addWidget(self.submit_button)  # Add submit button
        buttons_layout.addWidget(self.save_button)  # Add save button
        buttons_layout.addStretch()  # Add a stretchable space after the buttons (pushes them to center)
       
        # Add the buttons layout to the main layout
        layout.addLayout(buttons_layout)
        layout.addWidget(self.scroll_area)

        # Set the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # layout.addWidget(self.save_button)

    def on_submit_click(self):
        user_input = self.input_line.text()
        max_tokens = self.max_tokens_spin.value() if self.max_tokens_checkbox.isChecked() else None
        temperature = self.temperature_slider.value() / 100.0 if self.temperature_checkbox.isChecked() else None
        self.submit_callback(user_input, max_tokens, temperature)

    def max_tokens_checkbox_changed(self, state):
        self.max_tokens_spin.setEnabled(state == Qt.Checked)

    def temperature_checkbox_changed(self, state):
        self.temperature_slider.setEnabled(state == Qt.Checked)

    def update_temperature_label(self, value):
        self.temperature_value_label.setText(f"{value / 100:.2f}")
    
    def on_save_click(self):
        # This method will be called when the Save button is clicked.
        # Emit a signal or directly call a method in the main.py to handle saving.
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Response", "", "Word Documents (*.docx)")
        if file_path:
            self.save_callback(file_path)
