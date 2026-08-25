import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf_quotation(client_info: dict, window_designs: list) -> io.BytesIO:
    """Generates a professional Quotation PDF buffer using ReportLab."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story = []

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#1e293b'))
    normal_style = styles['Normal']

    # Document Header
    story.append(Paragraph("<b>WIN-SQUARE QUOTATION REPORT</b>", title_style))
    story.append(Spacer(1, 10))

    # Client Info Block
    client_data = [
        [Paragraph(f"<b>Client:</b> {client_info['name']}", normal_style), Paragraph(f"<b>Quote No:</b> {client_info['quotation_no']}", normal_style)],
        [Paragraph(f"<b>Location:</b> {client_info['location']}", normal_style), Paragraph(f"<b>Date:</b> {client_info['date']}", normal_style)]
    ]
    client_table = Table(client_data, colWidths=[260, 260])
    client_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1'))
    ]))
    story.append(client_table)
    story.append(Spacer(1, 15))

    # Table Header & Data
    table_data = [["Code", "Type", "Size (W x H mm)", "Qty", "Price (INR)"]]
    total_val = 0
    
    for item in window_designs:
        item_total = item['price'] * item['qty']
        total_val += item_total
        table_data.append([
            item['code'],
            item['type'],
            f"{item['width']} x {item['height']}",
            str(item['qty']),
            f"Rs. {item_total:,.2f}"
        ])

    table_data.append(["", "", "", "Grand Total:", f"Rs. {total_val:,.2f}"])

    doc_table = Table(table_data, colWidths=[80, 150, 120, 50, 120])
    doc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2563eb')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#f1f5f9')),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
    ]))

    story.append(doc_table)
    doc.build(story)
    
    buffer.seek(0)
    return buffer
