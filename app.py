# 1. Instalação das ferramentas necessárias
!pip install Pillow

from PIL import Image, ImageDraw, ImageFont
import os

# 2. Configuração dos dados (Extraídos do seu PDF)
dados_risco = {
    "cliente": "SERRARIA OURO VERDE LTDA",
    "endereco": "Av. Vidal Lourenço, 505, Andirá - PR",
    "lmi_incendio": "R$ 300.000,00",
    "cobertura_vendaval": "R$ 150.000,00"
}

# 3. Função para gerar o infográfico
def gerar_infografico_tech_v1(template_path, output_name):
    try:
        # Abre a imagem base
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)
        
        # Aqui o código escreve os dados na imagem
        # (Ajustaremos as coordenadas x, y conforme seu template)
        draw.text((50, 100), f"CLIENTE: {dados_risco['cliente']}", fill="white")
        draw.text((50, 150), f"LOCAL: {dados_risco['endereco']}", fill="white")
        
        img.save(output_name)
        print(f"✅ Infográfico {output_name} gerado com sucesso!")
    except Exception as e:
        print(f"❌ Erro: Certifique-se de que o arquivo {template_path} foi carregado no Colab.")

# Executar (Troque 'template.png' pelo nome do seu arquivo carregado)
gerar_infografico_tech_v1('seu_template_original.png', 'Relatorio_Andira_Final.png')
