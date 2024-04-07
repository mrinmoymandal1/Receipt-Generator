# Importing necessary modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Data to be displayed in tables
DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    ["07/04/2024", "Data and Analytics",
        "Lifetime", "10,999.00/-"],
    ["07/04/2024", "Power BI", "6 months", "3,999.00/-"],
    ["Sub Total", "", "", "14998.00/-"],
    ["Discount", "", "", "-998.00/-"],
    ["Total", "", "", "14000.00/-"],
]

# Creating a Base Document Template with A4 page size
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# Getting sample styles from ReportLab
styles = getSampleStyleSheet()

# Fetching the style for top-level heading (Heading1)
title_style = styles["Heading1"]

# Aligning the heading to center
title_style.alignment = 1

# Creating a paragraph with the heading text and applying the styles
title = Paragraph("pyc coder", title_style)

# Creating Table Style object and defining styles row-wise
style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.black),
        ("BACKGROUND", (0, 0), (3, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)

# Creating a table object and applying the defined style
table = Table(DATA, style=style)

# Building the final PDF by adding the title and table
pdf.build([title, table])
