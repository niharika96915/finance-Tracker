from database import Database
from category_manager import CategoryManager
from transaction_manager import TransactionManager
from visualizer import Visualizer
from gui_manager import FinanceGUI
from export_manager import ExportManager


class FinanceTracker:
    def __init__(self):
        self.db = Database()
        self.category_manager = CategoryManager(self.db)
        self.transaction_manager = TransactionManager(self.db)
        self.visualizer = Visualizer(self.db)
        self.export_manager = ExportManager(self.db)


def main():
    tracker = FinanceTracker()
    gui = FinanceGUI(tracker)
    
    # Center the window on screen
    window_width = 900
    window_height = 700
    screen_width = gui.root.winfo_screenwidth()
    screen_height = gui.root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    gui.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    gui.run()


if __name__ == "__main__":
    main()