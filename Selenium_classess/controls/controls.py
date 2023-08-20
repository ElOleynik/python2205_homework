class Controls:
    def __init__(self, button_element):
        self.element = button_element

    def click(self):
        self.element.click()

    def is_enabled(self):
        self.element.is_enabled()

    def label_element(self, label_element):
        self.element = label_element

    def get_text(self):
        return self.element.text

    def text_box(self, text_box):
        self.element = text_box

    def send_keys(self, keys_to_send):
        self.element.send_keys(keys_to_send)
