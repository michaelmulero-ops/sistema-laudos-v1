def gerar_croqui_nivel_1(imagem):
    """Sofia: Gera o croqui técnico com perspectiva de frente à rua"""
    img = imagem.convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    # 1. Definição da Linha de Base (Calçada/Rua)
    draw.line([(0, 3*h//4), (w, 3*h//4)], fill=(200, 200, 200), width=5)
    
    # 2. Marcação de Fachada Frontal (Ignorando Norte Magnético)
    # Foco total na perspectiva do inspetor de frente para o imóvel
    draw.rectangle([w//4, h//3, 3*w//4, 3*h//4], outline=(0, 255, 0), width=6)
    
    # 3. HUD de Medição Técnica
    draw.text((w//4, h//3 - 40), "NÍVEL 1: CROQUI DE LOCALIZAÇÃO FRONTAL", fill=(0, 255, 0))
    draw.text((w//2, 3*h//4 + 10), "LOGRADOURO PÚBLICO - VISTA PRINCIPAL", fill=(255, 255, 255))
    
    return img
