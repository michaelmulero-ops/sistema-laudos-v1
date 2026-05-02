def apply_hud_effect_v2(uploaded_file):
    """Cria o visual de scanner usando PIL (mais rápido e sem erros)"""
    img = Image.open(uploaded_file)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    # Desenha a linha de scanner verde do HUD
    scan_y = int((time.time() * 100) % height)
    draw.line([(0, scan_y), (width, scan_y)], fill=(0, 255, 0), width=5)
    
    # Adiciona o quadro de análise técnica (Estilo os vídeos do TikTok)
    draw.rectangle([width//4, height//4, 3*width//4, 3*height//4], outline=(0, 255, 0), width=3)
    
    return img
