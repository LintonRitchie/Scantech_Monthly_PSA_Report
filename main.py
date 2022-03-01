from PDF import PDF
from Report_Test import plots_per_page

pdf = PDF()

for elem in plots_per_page:
    pdf.print_page(elem)

pdf.output('SalesReport4.pdf', 'F')