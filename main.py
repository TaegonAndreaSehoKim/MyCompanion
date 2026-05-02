import sys
from PySide6.QtWidgets import QApplication
from ui.pet_window import PetWindow

def main():
    app = QApplication(sys.argv)
    
    # Create and show the pet window
    pet = PetWindow()
    pet.show()
    
    # Run the application loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
