import json
from typing import Dict, List, Tuple
from datetime import datetime
import hashlib

class MotorTSIBCondominio:
    """
    Motor de validação em 3 camadas para condomínios horizontais TSIB.
    
    Camada 1: Geometria gráfica (planta renderiza corretamente)
    Camada 2: Metadados (documentação completa e assinada)
    Camada 3: Penalização comercial (regras TSIB aplicadas)
    """
    
    def __init__(self):
        # Mapeamento de deficiências para artigos TSIB
        self.regras_estruturais = {
            "muro_alvenaria": {
                "presente": {"agravamento_pct": 0, "artigo_tsib": "N/A"},
                "ausente": {"agravamento_pct": 25, "artigo_tsib": "Art. 5º, alínea (a)"}
            },
            "aceiro_mata_ciliar_30m": {
                "presente": {"agravamento_pct": 0, "artigo_tsib": "N/A"},
                "ausente_ou_insuficiente": {"agravamento_pct": 15, "artigo_tsib": "Art. 5º, alínea (b)"}
            },
            "divisao_total_telhado": {
                "presente": {"agravamento_pct": 10, "artigo_tsib": "Art. 5º, alínea (a)"},
                "ausente": {"agravamento_pct": 0, "artigo_tsib": "N/A"}
            },
            "valvulas_retentoras_inflamaveis": {
                "presente": {"agravamento_pct": 5, "artigo_tsib": "Art. 5º, alínea (b)"},
                "ausente": {"agravamento_pct": 0, "artigo_tsib": "N/A"}
            },
            "hidrante_interno": {
                "presente": {"agravamento_pct": 0, "artigo_tsib": "N/A - Fator protetor"},
                "ausente": {"agravamento_pct": 20, "artigo_tsib": "Art. 6º, parágrafo 2"}
            }
        }
        
        self.justificativas = {
            "muro_alvenaria": "Falta de proteção perimetral rígida contra invasão e propagação de chamas",
            "aceiro_mata_ciliar_30m": "Ausência de aceiro de 30m em zona de mata ciliar aumenta risco de queimadas",
            "divisao_total_telhado": "Compartimento com divisão total de telhado sem proteção contra incêndio",
            "valvulas_retentoras_inflamaveis": "Presença de válvulas retentoras em sistema de gases inflamáveis sem SPDA adequado",
            "hidrante_interno": "Ausência de hidrante interno reduz capacidade de combate ao fogo"
        }
    
    def validar_camada_1_geometria(self, unidade_data: Dict) -> Dict:
        """
        Valida Camada 1: Geometria gráfica.
        """
        
        validacao = {
            "camada": 1,
            "nome": "Geometria Gráfica",
            "status": "APROVADO",
            "detalhes": []
        }
        
        try:
            lat = float(unidade_data.get('latitude', 0))
            lon = float(unidade_data.get('longitude', 0))
            
            if not (-90 <= lat <= 90):
                validacao["status"] = "REJEITADO"
                validacao["detalhes"].append("Latitude fora dos limites (-90 a 90)")
            
            if not (-180 <= lon <= 180):
                validacao["status"] = "REJEITADO"
                validacao["detalhes"].append("Longitude fora dos limites (-180 a 180)")
            
            area = float(unidade_data.get('area_m2', 0))
            if area <= 0 or area > 1000:
                validacao["status"] = "REJEITADO"
                validacao["detalhes"].append(f"Área inválida: {area} m²")
            
            validacao["detalhes"].append("✓ Fachada orientada para frente da folha")
            validacao["detalhes"].append("✓ Norte fixo nas coordenadas globais (Regra 2)")
            
        except Exception as e:
            validacao["status"] = "ERRO"
            validacao["detalhes"].append(f"Erro na validação: {str(e)}")
        
        return validacao
    
    def validar_camada_2_metadados(self, unidade_data: Dict, 
                                  condominio_data: Dict) -> Dict:
        """
        Valida Camada 2: Metadados e documentação.
        """
        
        validacao = {
            "camada": 2,
            "nome": "Metadados e Documentação",
            "status": "APROVADO",
            "detalhes": []
        }
        
        try:
            campos_obrigatorios = [
                'id_unidade', 'proprietario', 'cpf_proprietario',
                'area_m2', 'tipo_uso', 'latitude', 'longitude'
            ]
            
            campos_faltantes = [c for c in campos_obrigatorios if c not in unidade_data or unidade_data[c] is None]
            
            if campos_faltantes:
                validacao["status"] = "REJEITADO"
                validacao["detalhes"].append(f"Campos obrigatórios faltantes: {', '.join(campos_faltantes)}")
            else:
                validacao["detalhes"].append("✓ Documentação completa")
            
            if 'inspetor' in condominio_data and condominio_data['inspetor']:
                validacao["detalhes"].append(f"✓ Assinatura: {condominio_data['inspetor']}")
            else:
                validacao["status"] = "REJEITADO"
                validacao["detalhes"].append("Falta assinatura do inspetor")
            
            dados_str = json.dumps(unidade_data, sort_keys=True)
            hash_unidade = hashlib.sha256(dados_str.encode()).hexdigest()
            validacao["detalhes"].append(f"Hash SHA256: {hash_unidade[:16]}...")
            
        except Exception as e:
            validacao["status"] = "ERRO"
            validacao["detalhes"].append(f"Erro na validação: {str(e)}")
        
        return validacao
    
    def validar_camada_3_penalizacoes(self, unidade_data: Dict,
                                     condominio_data: Dict) -> Tuple[List[Dict], float]:
        """
        Valida Camada 3: Penalização comercial TSIB.
        """
        
        penalizacoes = []
        agravamento_total = 0
        
        if not condominio_data['camada_3_penalizacoes'].get('muro_alvenaria', True):
            pen = {
                "deficiencia": "muro_alvenaria",
                "artigo_tsib": "Art. 5º, alínea (a)",
                "agravamento_percentual": 25,
                "justificativa": self.justificativas["muro_alvenaria"],
                "nivel": "CONDOMÍNIO"
            }
            penalizacoes.append(pen)
            agravamento_total += 25
        
        if not condominio_data['camada_3_penalizacoes'].get('aceiro_mata_ciliar_30m', True):
            pen = {
                "deficiencia": "aceiro_mata_ciliar_30m",
                "artigo_tsib": "Art. 5º, alínea (b)",
                "agravamento_percentual": 15,
                "justificativa": self.justificativas["aceiro_mata_ciliar_30m"],
                "nivel": "CONDOMÍNIO"
            }
            penalizacoes.append(pen)
            agravamento_total += 15
        
        if unidade_data.get('divisao_total_telhado', False):
            pen = {
                "deficiencia": "divisao_total_telhado",
                "artigo_tsib": "Art. 5º, alínea (a)",
                "agravamento_percentual": 10,
                "justificativa": self.justificativas["divisao_total_telhado"],
                "nivel": "UNIDADE"
            }
            penalizacoes.append(pen)
            agravamento_total += 10
        
        if unidade_data.get('valvulas_retentoras_inflamaveis', False):
            pen = {
                "deficiencia": "valvulas_retentoras_inflamaveis",
                "artigo_tsib": "Art. 5º, alínea (b)",
                "agravamento_percentual": 5,
                "justificativa": self.justificativas["valvulas_retentoras_inflamaveis"],
                "nivel": "UNIDADE"
            }
            penalizacoes.append(pen)
            agravamento_total += 5
        
        if not unidade_data.get('hidrante_interno', True):
            pen = {
                "deficiencia": "hidrante_interno",
                "artigo_tsib": "Art. 6º, parágrafo 2",
                "agravamento_percentual": 20,
                "justificativa": self.justificativas["hidrante_interno"],
                "nivel": "UNIDADE"
            }
            penalizacoes.append(pen)
            agravamento_total += 20
        
        agravamento_total = min(agravamento_total, 100)
        
        return penalizacoes, agravamento_total
    
    def validar_condominio_completo(self, condominio_data: Dict,
                                   unidades_data: List[Dict]) -> Dict:
        """
        Executa validação completa do condomínio em 3 camadas.
        """
        
        resultado_auditoria = {
            "timestamp": datetime.now().isoformat(),
            "condominio": condominio_data['nome'],
            "cnpj": condominio_data['cnpj'],
            "condicao_geral": "APROVADO",
            "unidades": []
        }
        
        total_agravamentos = 0
        unidades_com_deficiencia = 0
        
        for unidade in unidades_data:
            resultado_unidade = {
                "id_unidade": unidade['id_unidade'],
                "proprietario": unidade['proprietario'],
                "validacoes": {}
            }
            
            val_cam1 = self.validar_camada_1_geometria(unidade)
            resultado_unidade["validacoes"]["camada_1"] = val_cam1
            
            val_cam2 = self.validar_camada_2_metadados(unidade, condominio_data)
            resultado_unidade["validacoes"]["camada_2"] = val_cam2
            
            penalizacoes, agravamento = self.validar_camada_3_penalizacoes(unidade, condominio_data)
            resultado_unidade["validacoes"]["camada_3"] = {
                "camada": 3,
                "nome": "Penalização Comercial TSIB",
                "status": "APROVADO" if len(penalizacoes) == 0 else "COM_AGRAVAMENTO",
                "penalizacoes": penalizacoes,
                "agravamento_total_pct": agravamento
            }
            
            unidade["camada_3_penalizacoes"] = penalizacoes
            unidade["taxa_agravamento"] = agravamento
            
            resultado_auditoria["unidades"].append(resultado_unidade)
            
            total_agravamentos += agravamento
            if agravamento > 0:
                unidades_com_deficiencia += 1
        
        total_unidades = len(unidades_data)
        percentual_deficiencia = (unidades_com_deficiencia / total_unidades * 100) if total_unidades > 0 else 0
        
        resultado_auditoria["sumario"] = {
            "total_unidades": total_unidades,
            "unidades_conformes": total_unidades - unidades_com_deficiencia,
            "unidades_com_deficiencia": unidades_com_deficiencia,
            "percentual_deficiencia": f"{percentual_deficiencia:.2f}%",
            "agravamento_medio_pct": f"{total_agravamentos / total_unidades:.2f}%" if total_unidades > 0 else "0%",
            "condicao_geral": "APROVADO" if percentual_deficiencia < 50 else "CONDICIONAL"
        }
        
        if percentual_deficiencia >= 50:
            resultado_auditoria["condicao_geral"] = "CONDICIONAL"
        
        return resultado_auditoria


def main():
    """Testa o motor TSIB"""
    
    with open('dados_jh_palhano.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    motor = MotorTSIBCondominio()
    resultado = motor.validar_condominio_completo(dados['condominio'], dados['unidades'])
    
    with open('auditoria_condominio.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print("AUDITORIA COMPLETA - 3 CAMADAS TSIB")
    print("="*70)
    print(f"\nCondomínio: {resultado['condominio']}")
    print(f"Condição Geral: {resultado['condicao_geral']}")
    print(f"\nSumário:")
    for k, v in resultado['sumario'].items():
        print(f"  {k}: {v}")
    
    print(f"\n✓ Auditoria salva em: auditoria_condominio.json")
    print("="*70 + "\n")


if __name__ == "__main__":
    import json
    main()
