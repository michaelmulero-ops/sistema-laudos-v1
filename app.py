def gerar_pdf(projeto, localidade, data, parecer, img_orig, img_zoom, lat, lon):
    pdf = FPDF()
    pdf.add_page()
    
    # Cabeçalho Michael Mulero Inspeções
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "MICHAEL MULERO INSPEÇÕES - LAUDO TÉCNICO", ln=True, align='C')
    
    # Selo de Autenticidade GPS (Prova Forense)
    pdf.set_font("Arial", 'I', 8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, f"Selo de Localização GPS: Lat {lat} / Lon {lon}", ln=True, align='R')
    pdf.set_text_color(0, 0, 0)
    
    pdf.ln(5)
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 10, f"Cliente: {projeto} | Localidade: {localidade} | Data: {data}", ln=True, align='C')
    
    # Imagens e Parecer da Sofia
    img_orig.save("temp_orig.jpg")
    img_zoom.save("temp_zoom.jpg")
    pdf.image("temp_orig.jpg", x=10, y=55, w=90)
    pdf.image("temp_zoom.jpg", x=110, y=55, w=90)
    pdf.ln(80)
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "PARECER TÉCNICO (AGENTE IA SOFIA):", ln=True)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 10, parecer)
    
    return pdf.output(dest='S')
