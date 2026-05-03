# MÓDULO DE EVIDÊNCIA VISUAL - MICHAEL MULERO INSPEÇÕES TECH V1
from PIL import Image, ImageOps, ImageDraw, ImageFont

def aplicar_estetica_reels(caminho_foto, ponto_x, ponto_y, texto_alerta="RISCO DETECTADO"):
    """
    Aplica o zoom técnico e a legenda de alto impacto estilo 'Sem Filtro'.
    """
    img = Image.open(caminho_foto).convert("RGB")
    
    # 1. CRIAR O ZOOM (Lupa Técnica)
    box = 250
    left, top = max(0, ponto_x - box), max(0, ponto_y - box)
    right, bottom = min(img.width, ponto_x + box), min(img.height, ponto_y + box)
    zoom = img.crop((left, top, right, bottom)).resize((800, 800), Image.LANCZOS)
    zoom = ImageOps.expand(zoom, border=15, fill='red') # Moldura de Alerta

    # 2. CRIAR O CANVAS DE APRESENTAÇÃO
    final = Image.new('RGB', (img.width + 850, img.height), (30, 30, 30))
    final.paste(img, (0, 0))
    final.paste(zoom, (img.width + 25, (img.height // 2) - 400))

    # 3. ADICIONAR LEGENDA ESTILO 'REELS' (Alto Contraste)
    draw = ImageDraw.Draw(final)
    # Aqui simulamos a legenda dinâmica que vimos nos links
    draw.rectangle([img.width + 25, 50, img.width + 825, 150], fill="yellow")
    draw.text((img.width + 50, 70), texto_alerta, fill="black")

    final.save("evidencia_estilizada.jpg")
    return "Foto processada com estética de alta autoridade!"

# PARA EXECUTAR:
# aplicar_estetica_reels("foto_vistoria.jpg", 1000, 500, "ANOMALIA TÉRMICA")
