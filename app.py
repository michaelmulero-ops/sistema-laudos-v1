from PIL import Image, ImageDraw

# 1. Criar um fundo de teste (simulando seu template)
img = Image.new('RGB', (800, 400), color = (0, 31, 63)) # Azul escuro padrão
draw = ImageDraw.Draw(img)

# 2. Dados da Serraria Ouro Verde (Andirá)
texto_cabecalho = "MICHAEL MULERO INSPECOES - TECH V1"
cliente = "CLIENTE: SERRARIA OURO VERDE LTDA"
local = "LOCAL: AV. VIDAL LOURENCO, 505 - ANDIRA/PR"
lmi = "LMI INCENDIO: R$ 300.000,00"

# 3. Desenhar no "papel"
draw.text((20, 20), texto_cabecalho, fill=(255, 255, 255))
draw.text((20, 100), cliente, fill=(255, 255, 0)) # Amarelo para destaque
draw.text((20, 140), local, fill=(255, 255, 255))
draw.text((20, 180), lmi, fill=(255, 255, 255))

# 4. Salvar e mostrar
img.save('teste_sistema_v1.png')
print("✅ Programa operacional! Imagem 'teste_sistema_v1.png' gerada na pasta ao lado.")
