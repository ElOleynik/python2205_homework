from .base import Base


class Garage(Base):
    def __init__(self):
        super().__init__()

    def get_text_from_empty_garage(self):
        return self.garage_page.empty_garage_label().get_text()
