import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import json
from datetime import datetime
from typing import Dict, List, Tuple

class GeradorLegendaTSIB:
    """
    Gerador de legendas e notas explicativas para laudos TSIB
    Implementa cores dinâmicas (verde para bônus, vermelho para agravamento)
    """
    
    def __init__(self):
        self.cor_bonus = '#1D9E75'  # Verde TSIB
        self.cor_agravamento = '#DC2626'  # Vermelho penalização
        self.cor_neutro = '#6B7280'  # Cinza neutro
        self.fonte_legenda = 'monospace'
        self.tamanho_fonte = 9
        
    def gerar_legenda_checklist(self, fig, ax, unidade_data: Dict) -> None:
        """
        Renderiza checklist dinâmico no rodapé do laudo.
        Símbolos adaptam automaticamente baseado em penalizações.
        
        Args:
            fig: Figure matplotlib
            ax: Axes matplotlib
            unidade_data: Dicionário com dados da unidade
        """
        
        y_pos = 0.02
        x_start = 0.05
        espaco_x = 0.15
        
        # Título da legenda
        ax.text(x_start, y_pos + 0.08, "LEGENDA DE CONFORMIDADE", 
                fontsize=self.tamanho_fonte + 2, weight='bold',
                transform=ax.transAxes, family=self.fonte_legenda)
        
        # Extrai penalizações da Camada 3
        penalizacoes = unidade_data.get("camada_3_penalizacoes", [])
        itens_checklist = [
            ("divisao_total_telhado", "Divisão Telhado", "Art. 5º(a)"),
            ("valvulas_retentoras_inflamaveis", "Válvulas Inflamáveis", "Art. 5º(b)"),
            ("hidrante_interno", "Hidrante Interno", "Art. 5º(c)"),
        ]
        
        col_idx = 0
        for campo, label, artigo in itens_checklist:
            x_pos = x_start + (col_idx % 5) * espaco_x
            y_atual = y_pos + (0.05 if col_idx >= 5 else 0)
            
            # Verifica se há penalização para este campo
            tem_penalizacao = any(p["deficiencia"] == campo for p in penalizacoes)
            
            # Símbolo e cor dinâmicos
            if unidade_data.get(campo, False) and not tem_penalizacao:
                simbolo = "✓"
                cor = self.cor_bonus
                status = "OK"
            elif tem_penalizacao:
                simbolo = "!"
                cor = self.cor_agravamento
                status = "AGR"
            else:
                simbolo = "○"
                cor = self.cor_neutro
                status = "N/A"
            
            # Renderiza item
            ax.text(x_pos, y_atual, f"[{simbolo}] {label}", 
                    fontsize=self.tamanho_fonte,
                    color=cor, weight='bold',
                    transform=ax.transAxes, family=self.fonte_legenda)
            
            ax.text(x_pos + 0.08, y_atual - 0.015, f"{artigo}", 
                    fontsize=self.tamanho_fonte - 1,
                    color=cor, style='italic',
                    transform=ax.transAxes, family=self.fonte_legenda)
            
            col_idx += 1
    
    def gerar_bloco_notas_tsib(self, fig, ax, unidade_data: Dict, 
                               condominio_data: Dict) -> None:
        """
        Renderiza bloco de notas TSIB com cores dinâmicas.
        Verde para bônus, vermelho para agravamento.
        
        Args:
            fig: Figure matplotlib
            ax: Axes matplotlib
            unidade_data: Dados da unidade
            condominio_data: Dados do condomínio
        """
        
        penalizacoes = unidade_data.get("camada_3_penalizacoes", [])
        taxa_agravamento = unidade_data.get("taxa_agravamento", 0)
        
        # Define cor do bloco baseado em agravamento
        if taxa_agravamento > 0:
            cor_fundo = self.cor_agravamento
            titulo_bloco = "⚠️ AGRAVAMENTO APLICADO"
        else:
            cor_fundo = self.cor_bonus
            titulo_bloco = "✓ SEM PENALIZAÇÕES"
        
        # Cria caixa com fundo colorido
        box = FancyBboxPatch((0.05, 0.75), 0.9, 0.15,
                            boxstyle="round,pad=0.01",
                            transform=ax.transAxes,
                            facecolor=cor_fundo, alpha=0.2,
                            edgecolor=cor_fundo, linewidth=2)
        ax.add_patch(box)
        
        # Título
        ax.text(0.08, 0.87, titulo_bloco,
                fontsize=self.tamanho_fonte + 2, weight='bold',
                color=cor_fundo, transform=ax.transAxes,
                family=self.fonte_legenda)
        
        # Conteúdo
        y_content = 0.82
        if penalizacoes:
            for pen in penalizacoes:
                texto = f"• {pen['deficiencia']}: {pen['justificativa']}"
                ax.text(0.08, y_content, texto,
                        fontsize=self.tamanho_fonte,
                        color=cor_fundo, transform=ax.transAxes,
                        family=self.fonte_legenda, wrap=True)
                y_content -= 0.04
        else:
            ax.text(0.08, y_content, "Unidade em conformidade total com TSIB",
                    fontsize=self.tamanho_fonte,
                    color=cor_fundo, transform=ax.transAxes,
                    family=self.fonte_legenda, style='italic')
    
    def gerar_sumario_executivo(self, condominio_data: Dict, 
                                unidades_data: List[Dict]) -> str:
        """
        Gera texto de sumário executivo com estatísticas agregadas.
        
        Args:
            condominio_data: Dados do condomínio
            unidades_data: Lista de dados das unidades
            
        Returns:
            String formatada com sumário
        """
        
        total_unidades = len(unidades_data)
        unidades_com_agravamento = sum(1 for u in unidades_data if u.get("taxa_agravamento", 0) > 0)
        unidades_conformes = total_unidades - unidades_com_agravamento
        
        agravamento_medio = sum(u.get("taxa_agravamento", 0) for u in unidades_data) / total_unidades if total_unidades > 0 else 0
        
        premio_total_base = sum(u.get("premio_base_anual", 0) for u in unidades_data)
        premio_total_final = sum(u.get("premio_final", 0) for u in unidades_data)
        impacto_financeiro = premio_total_final - premio_total_base
        
        sumario = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║           SUMÁRIO EXECUTIVO - CONDOMÍNIO HORIZONTAL        ║
╚═══════════════════════════════════════════════════════════════════════════╝

📋 CONDOMÍNIO: {condominio_data['nome']}
   CNPJ: {condominio_data['cnpj']}
   Endereço: {condominio_data['endereco']}
   Data Vistoria: {condominio_data['data_vistoria']}

📊 ESTATÍSTICAS GERAIS:
   Total de unidades: {total_unidades}
   ✓ Unidades conformes: {unidades_conformes} ({100*unidades_conformes/total_unidades:.1f}%)
   ⚠️  Unidades com agravamento: {unidades_com_agravamento} ({100*unidades_com_agravamento/total_unidades:.1f}%)
   Agravamento médio: {agravamento_medio:.2f}%

💰 IMPACTO FINANCEIRO:
   Prêmio base total: R$ {premio_total_base:,.2f}
   Prêmio final total: R$ {premio_total_final:,.2f}
   Impacto: R$ {impacto_financeiro:,.2f} ({100*impacto_financeiro/premio_total_base:+.2f}%)

🧭 GEORREFERENCIAMENTO:
   Latitude: {condominio_data['latitude_condominio']}
   Longitude: {condominio_data['longitude_condominio']}
   Precisão: {condominio_data['camada_1_geometria'].get('coordenadas_precisao_m', 'N/A')} metros

✍️  INSPETOR: {condominio_data['inspetor']}
   Matrícula: {condominio_data['matricula_inspetor']}

"""
        return sumario


def main():
    """Teste do gerador de legendas"""
    
    # Carrega dados de exemplo
    with open('dados_jh_palhano.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    gerador = GeradorLegendaTSIB()
    
    # Gera sumário executivo
    sumario = gerador.gerar_sumario_executivo(dados['condominio'], dados['unidades'])
    print(sumario)
    
    # Testa legenda para primeira unidade
    fig, ax = plt.subplots(figsize=(12, 8))
    gerador.gerar_bloco_notas_tsib(fig, ax, dados['unidades'][0], dados['condominio'])
    gerador.gerar_legenda_checklist(fig, ax, dados['unidades'][0])
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('legenda_tsib_teste.png', dpi=300, bbox_inches='tight')
    print("✓ Legenda salva em: legenda_tsib_teste.png")
    plt.close()


if __name__ == "__main__":
    main()
