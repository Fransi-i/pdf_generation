from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")  # orientation = P, portrait or L, landscape
pdf.add_page()
pdf.output("firstPdf.pdf")