from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297

    def header(self):
        # Custom logo and positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        self.image('Scantech_Logo.png', 0, 0, 210)
        self.set_font('Arial', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(60, 1, 'Sales report', 0, 0, 'R')
        self.ln(20)

    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def page_body(self, images):
        # Determine how many plots there are per page and set positions
        # and margins accordingly
        if len(images) == 3:
            self.image(images[0], 15, 45, self.WIDTH - 30)
            self.image(images[1], 15, self.WIDTH / 2 + 15, self.WIDTH - 30)
            self.image(images[2], 15, self.WIDTH / 2 + 90, self.WIDTH - 30)
        elif len(images) == 2:
            self.image(images[0], 15, 45, self.WIDTH - 30)
            self.image(images[1], 15, self.WIDTH / 2 + 15, self.WIDTH - 30)
        else:
            self.image(images[0], 15, 45, self.WIDTH - 30)

    def print_page(self, images):
        # Generates the report
        self.add_page()
        self.page_body(images)

    def output_table_to_pdf(self, df):
        # A cell is a rectangular area, possibly framed, which contains some text
        # Set the width and height of cell
        table_cell_width = 25
        table_cell_height = 6
        # Select a font as Arial, bold, 8
        self.set_font('Arial', 'B', 8)

        # Loop over to print column names
        cols = df.columns
        for col in cols:
            self.cell(table_cell_width, table_cell_height, col, align='C', border=1)
        # Line break
        self.ln(table_cell_height)
        # Select a font as Arial, regular, 10
        self.set_font('Arial', '', 10)
        # Loop over to print each data in the table
        for row in df.itertuples():
            for col in cols:
                value = str(getattr(row, col))
                self.cell(table_cell_width, table_cell_height, value, align='C', border=1)
            self.ln(table_cell_height)