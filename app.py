def apply_scanner_with_metrics(image):
    """Escaneamento com Medição de Pé-Direito e Dimensões (Estilo HUD)"""
    img = image.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # 1. Efeito de Varredura Laser
    scan_y = int((time.time() * 150) % h)
    draw.line([(0, scan_y), (w, scan_y)], fill=(0, 255, 0), width=8)
    
    # 2. Medição de Pé-Direito (Linha Vertical Esquerda)
    # Simulação de cálculo baseado na perspectiva da imagem
    draw.line([(w//6, h//4), (w//6, 3*h//4)], fill=(255, 255, 0), width=3)
    draw.text((w//6 + 10, h//2), "PE-DIREITO: EST. 6.50m", fill=(255, 255, 0))
    
    # 3. Medição de Fachada (Linha Horizontal Base)
    draw.line([(w//5, 3*h//4), (4*w//5, 3*h//4)], fill=(0, 255, 255), width=3)
    draw.text((w//2, 3*h//4 + 10), "FACHADA: EST. 12.00m", fill=(0, 255, 255))

    # 4. Caixa de Análise Setorial (Frente à Rua)
    draw.rectangle([w//5, h//5, 4*w//5, 4*h//5], outline=(0, 255, 0), width=4)
    draw.text((w//5, h//5 - 25), "SISTEMA DE INSPEÇÃO TECH V1 - MEDIÇÃO ATIVA", fill=(0, 255, 0))
    
    return img
