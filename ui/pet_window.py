import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMenu
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QMovie, QAction, QCursor, QPixmap

class PetWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. Window properties: Frameless, Always on Top, Transparent background
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 2. Setup Label for the GIF
        self.label = QLabel(self)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        
        # 3. Load GIFs and Scale them down by 50%
        self.idle_movie = self.load_scaled_movie('assets/idle.gif')
        self.petting_movie = self.load_scaled_movie('assets/petting.gif')
        self.eating_movie = self.load_scaled_movie('assets/eating.gif')
        
        self.current_movie = self.idle_movie
        self.label.setMovie(self.current_movie)
        self.current_movie.start()
        
        # Enable mouse tracking for hover events
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
        
        if self.underMouse():
            self.set_hover_cursor()
        
        # 4. Adjust window size to fit the scaled GIF
        self.label.adjustSize()
        self.resize(self.label.size())
        
        # 5. Position window at the bottom-right corner of the primary screen
        self.position_bottom_right()
        
        self.drag_start_pos = None
        self.is_interacting = False
        
        # Timer to revert to idle after petting/eating
        self.interaction_timer = QTimer(self)
        self.interaction_timer.setSingleShot(True)
        self.interaction_timer.timeout.connect(self.return_to_idle)
        
        # 6. Context Menu policy (Menu shown on left/right click release)

    def load_scaled_movie(self, path):
        movie = QMovie(path)
        # Start and jump to first frame to get size, then stop to scale
        movie.start()
        movie.setPaused(True)
        size = movie.currentImage().size()
        movie.stop()
        
        if size.width() > 0 and size.height() > 0:
            scaled_size = QSize(size.width() // 2, size.height() // 2)
            movie.setScaledSize(scaled_size)
            
        return movie

    def position_bottom_right(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        
        # Calculate bottom-right coordinates with a small margin (e.g., 50 pixels)
        margin_x = 50
        margin_y = 50
        x = screen_geometry.right() - self.width() - margin_x
        y = screen_geometry.bottom() - self.height() - margin_y
        
        self.move(x, y)

    def mousePressEvent(self, event):
        if event.button() in (Qt.MouseButton.LeftButton, Qt.MouseButton.RightButton):
            self.drag_start_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            self.has_dragged = False
            event.accept()

    def mouseMoveEvent(self, event):
        # Handle window movement during drag
        if (event.buttons() & (Qt.MouseButton.LeftButton | Qt.MouseButton.RightButton)) and getattr(self, 'drag_start_pos', None):
            self.move(event.globalPosition().toPoint() - self.drag_start_pos)
            self.has_dragged = True
            event.accept()
        elif not event.buttons():
            # Mouse moving over without buttons triggers petting
            if not self.is_interacting:
                self.start_interaction(self.petting_movie, 3000)
            event.accept()
            
    def mouseReleaseEvent(self, event):
        if event.button() in (Qt.MouseButton.LeftButton, Qt.MouseButton.RightButton):
            if not getattr(self, 'has_dragged', False):
                self.show_context_menu(event.position().toPoint())
            self.has_dragged = False
            self.drag_start_pos = None
        super().mouseReleaseEvent(event)

    def show_context_menu(self, pos):
        menu = QMenu(self)
        
        feed_action = QAction("Feed", self)
        feed_action.triggered.connect(self.feed_pet)
        menu.addAction(feed_action)
        
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        menu.addAction(quit_action)
        
        menu.exec(self.mapToGlobal(pos))
        
    def feed_pet(self):
        if not self.is_interacting:
            # Play eating animation for 4 seconds
            self.start_interaction(self.eating_movie, 4000)

    def start_interaction(self, new_movie, duration_ms):
        self.is_interacting = True
        
        self.current_movie.stop()
        
        self.current_movie = new_movie
        self.label.setMovie(self.current_movie)
        self.current_movie.start()
        
        # Enable mouse tracking for hover events
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
        
        
        # Start timer to revert back to idle state
        self.interaction_timer.start(duration_ms)
        
    def return_to_idle(self):
        self.is_interacting = False
        self.current_movie.stop()
        
        self.current_movie = self.idle_movie
        self.label.setMovie(self.current_movie)
        self.current_movie.start()
        
        # Enable mouse tracking for hover events
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)
        
        if self.underMouse():
            self.set_hover_cursor()

    def set_hover_cursor(self):
        cursor_path = 'assets/cursor_petting.png'
        if os.path.exists(cursor_path):
            custom_cursor = QCursor(QPixmap(cursor_path))
            self.setCursor(custom_cursor)
            self.label.setCursor(custom_cursor)
        else:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
            self.label.setCursor(Qt.CursorShape.PointingHandCursor)

    def enterEvent(self, event):
        if not self.is_interacting:
            self.set_hover_cursor()
        super().enterEvent(event)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.label.setCursor(Qt.CursorShape.ArrowCursor)
