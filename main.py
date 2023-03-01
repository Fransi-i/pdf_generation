from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")     # orientation = P, portrait or L, landscape
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("files/topics.csv")

def draw_lines(pdf, nr_of_lines):
    for x in range(0,nr_of_lines):
        pdf.line(x1=10, y1=22 + (x * 10), x2=200, y2=22 + (x * 10))               # tekent een lijn, x en y coordinaten van linksboven

for index, row in df.iterrows():
    pdf.add_page()                                      # create an empty page for each row in the dataframe
    pdf.set_font(family="Times", size=24)
    pdf.set_text_color(100, 100, 100)                   #grey
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
                                                        # w = width, if zero then until end of page
                                                        # border = 1 then cell has border
                                                        # h=heigth
                                                        # ln = breakline. With 1 the next cell is nextline
                                                        # ln = 0 then no nextline
    draw_lines(pdf, 27)

    pdf.ln(266)                                         # goes down 260 mm
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)                   #grey
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for i in range(1,int(row["Pages"]) ):
        pdf.add_page()
        draw_lines(pdf,27)    
        pdf.ln(278)                                         # goes down 278 mm
        #pdf.set_font(family="Times", style="I", size=8)
        #pdf.set_text_color(180, 180, 180)                   #grey
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)


pdf.output("files/firstPdf.pdf")                              # write to file