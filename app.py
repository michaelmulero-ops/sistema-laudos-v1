# Módulo de Captura Automática - Tech V1
import google_gemini_vision as gv

def processar_inspecao_live(video_stream):
    # O Gemini analisa o vídeo e identifica pontos críticos
    riscos_detectados = gv.analisar_frames(video_stream, "inspecao_seguros")
    
    for item in riscos_detectados:
        print(f"Equipamento: {item.nome}")
        print(f"Estado: {item.condicao}")
        # Salva automaticamente na pasta do seu relatório
        item.save_photo(f"vistoria_andira_{item.id}.jpg")

# Iniciando o modo mãos livres
processar_inspecao_live(camera_celular)
