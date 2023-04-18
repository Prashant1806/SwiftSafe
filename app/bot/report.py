from fpdf import FPDF, HTMLMixin

class PDFReport(FPDF, HTMLMixin):
    def __init__(self):
        super().__init__()
        self.add_page()

    def add_screenshot(self, screenshot_path):
        self.image(screenshot_path, x=self.get_x(), y=self.get_y(), w=200)
        self.ln(10)

    def add_text(self, text):
        self.multi_cell(0, 10, txt=text)
        self.ln()

    def generate_report(self, screenshots, text):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Fake Instagram Account Report', 0, 1, 'C')
        self.ln(10)

        self.set_font('Arial', '', 12)
        for screenshot in screenshots:
            self.add_screenshot(screenshot)
        self.ln()

        self.set_font('Arial', '', 12)
        self.add_text(text)
        self.ln()

        self.output('report.pdf', 'F')
