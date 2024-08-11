from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import pyqrcode
from fpdf import FPDF


class PDFCV(FPDF):
    def header(self):
        # Resim ekleme
        if self.image_path:
            self.image(self.image_path, 10, 8, 33)
        # QR kod ekleme
        self.image("mywebsite.png", 50, 8, 33)
        self.ln(40)  # Resimle metin arasında biraz boşluk bırakıyoruz

    def footer(self):
        pass

    def generate_cv(self, name, email, phone, address, skills, work_experience, education, about_me, image_path):
        self.image_path = image_path
        self.add_page()
        self.ln(10)

        # Displaying the name
        self.set_font("Arial", "B", 26)
        self.cell(0, 15, name, border=0, ln=1, align="C")
        self.ln(10)

        # Contact Information
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Contact Information", border=0, ln=1, align="L")
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, f"Email: {email}\nPhone: {phone}\nAddress: {address}", border=0, align="L")
        self.ln(5)

        # Skills Section
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Skills", border=0, ln=1, align="L")
        self.set_font("Arial", "", 10)
        for skill in skills:
            self.cell(0, 7, f"- {skill}", border=0, ln=1, align="L")
        self.ln(5)

        # Work Experience
        self.set_font("Arial", "B", 12)
        self.multi_cell(0, 10, "Work Experience", new_x="LMARGIN", new_y="NEXT", align="L")

        # Adding work experience
        self.set_font("Arial", "", 10)
        for experience in work_experience:
            self.multi_cell(0, 7, f"{experience['title']}: {experience['description']}",
                      new_x="LMARGIN", new_y="NEXT", align="J")
        self.ln(10)

        # Education
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT", align="L")

        # Adding education information
        self.set_font("Arial", "", 10)
        for education_item in education:
            self.multi_cell(0, 7, f"{education_item['degree']}: {education_item['university']}",
                      new_x="LMARGIN", new_y="NEXT", align="J")
        self.ln(10)

        # About Me Section
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "About Me", border=0, ln=1, align="L")
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 7, about_me, border=0, align="J")

        # Save the PDF
        clean_name = ''.join(name.split())
        self.output(f"{clean_name}CV.pdf")


def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()
    skills = entry_skills.get("1.0", END).strip().split("\n")
    work_experience = []
    education = []

    work_experience_lines = entry_experience.get("1.0", END).strip().split("\n")
    for line in work_experience_lines:
        if ":" in line:
            title, description = line.split(":", 1)
            work_experience.append({"title": title.strip(), "description": description.strip()})
    education_lines = entry_education.get("1.0", END).strip().split("\n")
    for line in education_lines:
        if ":" in line:
            degree, university = line.split(":", 1)
            education.append({"degree": degree.strip(), "university": university.strip()})

    about_me = entry_about_me.get("1.0", END).strip()

    # Create QR Code
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not email or not phone or not address or not skills or not education or not work_experience:
        messagebox.showerror("Error", "Please fill in all the details")
        return

    cv = PDFCV()
    cv.generate_cv(name, email, phone, address, skills, work_experience, education, about_me, image_path)
    messagebox.showinfo("Success", "Your CV has been generated successfully!")


def add_placeholder(text_widget, placeholder):
    text_widget.insert("1.0", placeholder)
    text_widget.bind("<FocusIn>", lambda event: clear_placeholder(event, placeholder))
    text_widget.bind("<FocusOut>", lambda event: restore_placeholder(event, placeholder))

def clear_placeholder(event, placeholder):
    widget = event.widget
    if widget.get("1.0", "end-1c") == placeholder:
        widget.delete("1.0", END)
        widget.config(fg="black")

def restore_placeholder(event, placeholder):
    widget = event.widget
    if not widget.get("1.0", "end-1c"):
        widget.insert("1.0", placeholder)
        widget.config(fg="grey")


def select_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if image_path:
        image = Image.open(image_path)
        image.thumbnail((100, 100))
        img = ImageTk.PhotoImage(image)
        lbl_image.config(image=img)
        lbl_image.image = img

window = Tk()
window.title("CV Generator")
window.configure(bg="#f0f0f0")

# Adding a scrollbar
canvas = Canvas(window, bg="#f0f0f0")
scroll_y = Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#f0f0f0")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

title_label = Label(scrollable_frame, text="CV Generator", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333")
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 15))

# Name
label_name = Label(scrollable_frame, text="Name:", font=("Helvetica", 9), bg="#f0f0f0")
label_name.grid(row=1, column=0, padx=10, pady=3, sticky="e")
entry_name = Entry(scrollable_frame, width=40)
entry_name.grid(row=1, column=1, padx=10, pady=3)

# Email
label_email = Label(scrollable_frame, text="Email:", font=("Helvetica", 9), bg="#f0f0f0")
label_email.grid(row=2, column=0, padx=10, pady=3, sticky="e")
entry_email = Entry(scrollable_frame, width=40)
entry_email.grid(row=2, column=1, padx=10, pady=3)

# Phone
label_phone = Label(scrollable_frame, text="Phone:", font=("Helvetica", 9), bg="#f0f0f0")
label_phone.grid(row=3, column=0, padx=10, pady=3, sticky="e")
entry_phone = Entry(scrollable_frame, width=40)
entry_phone.grid(row=3, column=1, padx=10, pady=3)

# Address
label_address = Label(scrollable_frame, text="Address:", font=("Helvetica", 9), bg="#f0f0f0")
label_address.grid(row=4, column=0, padx=10, pady=3, sticky="e")
entry_address = Entry(scrollable_frame, width=40)
entry_address.grid(row=4, column=1, padx=10, pady=3)

# Website
label_website = Label(scrollable_frame, text="Website:", font=("Helvetica", 9), bg="#f0f0f0")
label_website.grid(row=5, column=0, padx=10, pady=3, sticky="e")
entry_website = Entry(scrollable_frame, width=40)
entry_website.grid(row=5, column=1, padx=10, pady=3)

# Profile Image
label_image = Label(scrollable_frame, text="Profile Image:", font=("Helvetica", 9), bg="#f0f0f0")
label_image.grid(row=6, column=0, padx=10, pady=8, sticky="ne")
btn_image = Button(scrollable_frame, text="Select Image", command=select_image)
btn_image.grid(row=6, column=1, padx=10, pady=8, sticky="w")
lbl_image = Label(scrollable_frame, bg="#f0f0f0")
lbl_image.grid(row=7, column=1, padx=10, pady=8, sticky="w")

# Skills
label_skills = Label(scrollable_frame, text="Skills:", font=("Helvetica", 9), bg="#f0f0f0")
label_skills.grid(row=8, column=0, padx=10, pady=8, sticky="ne")
entry_skills = Text(scrollable_frame, height=10, width=40, font=("Helvetica", 9), fg="grey")
entry_skills.grid(row=8, column=1, padx=10, pady=8)
add_placeholder(entry_skills, "Enter one skill per line (e.g., Python, Data Analysis)")

# Education
label_education = Label(scrollable_frame, text="Education:", font=("Helvetica", 9), bg="#f0f0f0")
label_education.grid(row=9, column=0, padx=10, pady=8, sticky="ne")
entry_education = Text(scrollable_frame, height=10, width=40, font=("Helvetica", 9), fg="grey")
entry_education.grid(row=9, column=1, padx=10, pady=8)
add_placeholder(entry_education, "Degree: University\n(e.g., BSc: XYZ University)")

# Experience
label_experience = Label(scrollable_frame, text="Experience:", font=("Helvetica", 9), bg="#f0f0f0")
label_experience.grid(row=10, column=0, padx=10, pady=8, sticky="ne")
entry_experience = Text(scrollable_frame, height=10, width=40, font=("Helvetica", 9), fg="grey")
entry_experience.grid(row=10, column=1, padx=10, pady=8)
add_placeholder(entry_experience, "Job Title: Description\n(e.g., Software Engineer: Developed AI applications)")

# About Me
label_about_me = Label(scrollable_frame, text="About Me:", font=("Helvetica", 9), bg="#f0f0f0")
label_about_me.grid(row=11, column=0, padx=10, pady=8, sticky="ne")
entry_about_me = Text(scrollable_frame, height=10, width=40, font=("Helvetica", 9), fg="grey")
entry_about_me.grid(row=11, column=1, padx=10, pady=8)
add_placeholder(entry_about_me, "Write a brief description about yourself...")

# Generate Button
button_generate = Button(scrollable_frame, text="Generate CV", command=generate_cv_pdf, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
button_generate.grid(row=12, column=0, columnspan=2, pady=25)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
scroll_y.pack(side=RIGHT, fill=Y)

window.mainloop()
