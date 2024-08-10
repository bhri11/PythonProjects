from tkinter import *
from fpdf import FPDF
from tkinter import messagebox


window = Tk()
window.title("Invoice Generator")
window.geometry("400x400")


medicines = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 15,
    "Medicine D": 25
}
invoice_items = []
total_amount = 0.0


def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = quantity_entry.get()
    if selected_medicine and quantity.isdigit():
        quantity = int(quantity)
        price = medicines[selected_medicine]
        item_total = price * quantity
        invoice_items.append((selected_medicine, quantity, item_total))
        total_amount_entry.config(state=NORMAL)
        total_amount_entry.delete(0, END)
        total_amount_entry.insert(END, str(calculate_total()))
        total_amount_entry.config(state=DISABLED)
        update_invoice_text()
    else:
        messagebox.showwarning("Input Error", "Please enter a valid quantity and select a medicine.")


def calculate_total():
    total = 0.0
    for item in invoice_items:
        total += item[2]
    return total


def generate_invoice():
    customer_name = customer_entry.get()
    if not customer_name:
        messagebox.showwarning("Input Error", "Please enter the customer's name.")
        return

    pdf = FPDF()
    pdf.add_page()

    # PDF formatını ayarla
    pdf.set_font("Helvetica", size=16)
    pdf.cell(0, 10, text="Invoice", ln=True, align="C")

    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, text="Customer: " + customer_name, ln=True, align="L")
    pdf.ln(10)  # Boşluk bırak

    # Tablo başlıklarını ekle
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(80, 10, text="Medicine", border=1, align="C")
    pdf.cell(30, 10, text="Quantity", border=1, align="C")
    pdf.cell(30, 10, text="Price", border=1, align="C")
    pdf.cell(40, 10, text="Total", border=1, ln=True, align="C")

    # Fatura kalemlerini PDF'ye ekle
    pdf.set_font("Helvetica", size=12)
    for item in invoice_items:
        medicine_name, quantity, item_total = item
        pdf.cell(80, 10, text=medicine_name, border=1, align="L")
        pdf.cell(30, 10, text=str(quantity), border=1, align="C")
        pdf.cell(30, 10, text=str(medicines[medicine_name]), border=1, align="C")
        pdf.cell(40, 10, text=str(item_total), border=1, ln=True, align="C")

    pdf.ln(10)  # Boşluk bırak
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 10, text="Total Amount: " + str(calculate_total()), align="R")

    pdf.output("invoice.pdf")
    messagebox.showinfo("Success", "Invoice has been generated and saved as 'invoice.pdf'.")


# GUI layout
frame = Frame(window)
frame.pack(pady=10)

medicine_label = Label(frame, text="Select Medicine:")
medicine_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

medicine_listbox = Listbox(frame, selectmode=SINGLE, height=4)
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.grid(row=0, column=1, padx=10, pady=5)

quantity_label = Label(frame, text="Enter Quantity:")
quantity_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

quantity_entry = Entry(frame)
quantity_entry.grid(row=1, column=1, padx=10, pady=5)

add_button = Button(frame, text="Add Medicine", command=add_medicine, width=15)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

total_amount_label = Label(frame, text="Total Amount:")
total_amount_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

total_amount_entry = Entry(frame, state=DISABLED)
total_amount_entry.grid(row=3, column=1, padx=10, pady=5)

customer_label = Label(frame, text="Customer Name:")
customer_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

customer_entry = Entry(frame)
customer_entry.grid(row=4, column=1, padx=10, pady=5)

generate_button = Button(frame, text="Generate Invoice", command=generate_invoice, width=15)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

invoice_text = Text(window, height=10, width=50, state=DISABLED)
invoice_text.pack(pady=10)


def update_invoice_text():
    invoice_text.config(state=NORMAL)
    invoice_text.delete(1.0, END)
    for item in invoice_items:
        invoice_text.insert(END, f"Medicine: {item[0]}, Quantity: {item[1]}, Total: {item[2]}\n")
    invoice_text.config(state=DISABLED)


window.mainloop()
