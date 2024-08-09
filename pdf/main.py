from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         self.image("./pdf/logo.png", 10, 8, 33)
#         self.set_font("helvetica", "B", 16)
#         self.cell(80)
#         self.cell(40, 10, "Hello world", border=3, align="C")
#         self.ln(40)
#     def footer(self):
#         self.set_y(-15)
#         self.set_font("helvetica", "I", 16) 
#         self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
        


# pdf = PDF()
# pdf.add_page()
# pdf.set_font("helvetica", "B", 16)
# for i in range(1,41):
#     pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
    


# pdf.output("sample.pdf")

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        width = self.get_string_width(self.title)+6
        self.set_x((210-width)/2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50 , 50)
        self.set_line_width(1)
        self.cell(width, 9, self.title,
                  new_x="LMARGIN", new_y="NEXT", align="C",fill=True)
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 12)
        self.set_text_color(128) 
        self.cell(0, 10, f"Page {self.page_no()}", align="C")
    
    def chapter_title(self, num, label):
        self.set_font("helvetica", "", 12)
        self.set_fill_color(200,220,255)
        self.cell(0, 6, f"Chapter {num} : {label}",
                  new_x="LMARGIN", new_y="NEXT", align="L",fill=True)
        
    
    def chapter_body(self, file_path):
        with open(file_path, "rb") as fh:
            txt = fh.read().decode("latin-1")
        self.set_font("Times", size=12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font(style="I")
        self.multi_cell(0, 5, "(End of excerpt)")
        
    
    def print_chapter(self, num, title, file_path):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(file_path)
        
    
pdf = PDF()
pdf.set_title("100 Ways to Learn Programming")
pdf.set_author("Ashutosh Pawar")
pdf.print_chapter(1, "GETTING STARTED WITH PROGRAMMING", "./pdf/para.txt")
pdf.print_chapter(2, "WHICH PROGRAMMING LANGUAGE TO LEARN", "./pdf/para.txt")
pdf.output("sample.pdf")






