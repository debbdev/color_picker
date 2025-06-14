# Enhanced Color Picker

A modern, feature-rich color picker application built with Python and Tkinter. This tool allows you to capture colors from any pixel on your screen and display them in multiple formats (HEX, RGB) with additional useful features.

## Features

- 🎨 **Real-time Color Picking**: Hover over any pixel to see its color
- 📋 **Multiple Color Formats**: Display colors in HEX and RGB formats
- 📱 **Always on Top**: Tool window that stays above other applications
- 📍 **Mouse Coordinates**: Shows current mouse position
- 🖼️ **Color Preview**: Visual preview of the selected color
- 📋 **Copy to Clipboard**: One-click copy of HEX values
- ⌨️ **Keyboard Shortcuts**: Space to start/stop, Ctrl+C to copy
- 🎯 **Smart Text Contrast**: Automatically adjusts text color for readability
- 🔄 **Click to Select**: Click any text field to select all text

## Screenshots

The application features a clean, dark interface with:

- Color preview window showing the actual color
- Mouse coordinates display
- HEX and RGB value fields with dynamic backgrounds
- Start/Stop and Copy buttons

## Installation

### Prerequisites

- Python 3.7 or higher
- Windows, macOS, or Linux

### Step 1: Clone or Download

Download all the project files:

- `Window.py` - Custom Tkinter window wrapper
- `color_picker.py` - Main color picker application
- `Printer.py` - Logging utility
- `requirements.txt` - Python dependencies
- `README.md` - This file

### Step 2: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install customtkinter pyautogui colour colorama
```

### Step 3: Run the Application

```bash
python color_picker.py
```

## Usage

### Basic Operation

1. **Start the Application**: Run `python color_picker.py`
2. **Begin Color Picking**:
   - Click the "START (Space)" button, or
   - Press the **Spacebar**
3. **Pick Colors**: Move your mouse over any pixel on screen
4. **View Results**: See the color in HEX, RGB formats with live preview
5. **Copy Values**:
   - Click "Copy HEX" button, or
   - Press **Ctrl+C**, or
   - Click any text field to select all text for manual copying
6. **Stop Picking**: Press **Spacebar** again or click "STOP (Space)"

### Keyboard Shortcuts

| Key      | Action                              |
| -------- | ----------------------------------- |
| `Space`  | Start/Stop color picking            |
| `Ctrl+C` | Copy current HEX value to clipboard |

### Features in Detail

- **Color Preview**: The top section shows a live preview of the color under your mouse
- **Mouse Coordinates**: Displays current mouse position (X, Y)
- **Dynamic Text Colors**: Text automatically becomes black or white for optimal readability
- **Visual Feedback**: Buttons change color to indicate status (red when active, green when copied)
- **Error Handling**: Graceful handling of screen capture errors

## File Structure

```
color-picker/
├── Window.py              # Custom Tkinter window wrapper
├── color_picker.py        # Main application
├── Printer.py            # Logging and console output utility
├── requirements.txt      # Python dependencies
└── README.md            # This documentation
```

## Dependencies

- **customtkinter**: Modern UI components for Tkinter
- **pyautogui**: Screen capture and mouse position detection
- **colour**: Color format conversion utilities
- **colorama**: Colored terminal output

## Troubleshooting

### Common Issues

1. **Permission Errors (macOS)**:

   ```bash
   # Grant accessibility permissions to Terminal/Python in:
   # System Preferences > Security & Privacy > Privacy > Accessibility
   ```

2. **PyAutoGUI Failsafe**:

   - Moving mouse to top-left corner triggers failsafe
   - This is a safety feature - restart the application if needed

3. **Missing Dependencies**:

   ```bash
   # Reinstall requirements
   pip install --upgrade -r requirements.txt
   ```

4. **Display Issues**:
   - Ensure your system supports screen capture
   - Try running with administrator/root privileges if needed

### Performance Notes

- The application updates every 50ms for smooth performance
- On slower systems, you can modify the interval in `Window.py` line 105

## Advanced Usage

### Customization

You can modify the application by editing:

- **Update Frequency**: Change interval timing in `Window.py`
- **Window Size**: Modify dimensions in color_picker.py `__init__`
- **Color Formats**: Add new formats by extending the `intervalFunc` method
- **UI Theme**: Customize colors and fonts throughout the application

### Integration

The modular design allows easy integration:

```python
from Window import TkWindow
from Printer import Printer

# Use TkWindow for other applications
# Use Printer for consistent logging
```

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Changelog

### Version 2.0 (Enhanced)

- Added color preview window
- Implemented copy to clipboard functionality
- Added mouse coordinate display
- Improved UI layout and design
- Added keyboard shortcuts
- Better error handling and user feedback
- Smart text contrast for readability

### Version 1.0 (Original)

- Basic color picking functionality
- HEX and RGB display
- Start/stop with spacebar
- Tool window with always-on-top
