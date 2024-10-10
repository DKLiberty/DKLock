# DKLock 🔐

**DKLock** is a lightweight and secure lock-screen application designed to protect your system using a PIN code. Built with Python and Tkinter, it provides an intuitive interface for setting and verifying PIN codes, ensuring that only authorized users can unlock the system.

## Features

- **PIN Code Protection**: Set up a custom PIN code to lock and unlock your system.
- **Encrypted Storage**: PIN codes are securely encrypted using SHA-256 and stored in an SQLite database.
- **Automatic Setup**: If no PIN exists, the app prompts the user to create one during the first run.
- **User-Friendly Interface**: Clean and simple interface for easy PIN entry.
- **System Shortcut Blocking**: Prevents certain system shortcuts (e.g., `Win + Tab`) to avoid bypassing the lock.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DKLock.git
   cd DKLock
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python DKLock.py
   ```

## Usage

- When you run **DKLock** for the first time, it will prompt you to set a new PIN if no database file is found.
- The PIN is securely stored and required every time you launch the application to unlock your system.
- If the wrong PIN is entered, access is denied, and the system remains locked.

## Requirements

- **Python 3.x**
- **Tkinter** (usually pre-installed with Python)
- **SQLite** (included in Python)
- Additional Python modules can be installed via `requirements.txt`.

## Security

- PIN codes are encrypted with **SHA-256** before being stored in the SQLite database for added security.
- DKLock blocks certain system shortcuts (such as `Win + Tab`) to prevent users from bypassing the lock screen.

## Future Improvements

- **Facial Recognition**: Integrate facial recognition for enhanced security.
- **Improved Security**: Additional encryption methods and multi-user support for a more robust system.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests with ideas for improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need help, feel free to open a discussion or issue. You can also connect with us in the [General Discussion](https://github.com/yourusername/DKLock/discussions) to chat with the community.
