# --- 📑 CABEÇALHO TÉCNICO: MICHAEL MULERO INSPEÇÕES ---
def cabecalho_classificacao(cnpj, codigo_manual, atividade):
    st.markdown(f"""
        <div style="border: 2px solid #00FF00; padding: 20px; border-radius: 10px; background-color: #0E1117;">
            <h1 style="color: #00FF00; margin-bottom: 0;">🛡️ MICHAEL MULERO INSPEÇÕES</h1>
            <p style="font-size: 1.2em; color: white;"><b>RELATÓRIO TÉCNICO DE INSPEÇÃO DE RISCO V1</b></p>
            <hr style="border-color: #00FF00;">
            <table style="width: 100%; color: white;">
                <tr>
                    <td><b>CNPJ:</b> {cnpj}</td>
                    <td><b>CÓDIGO DO RISCO:</b> {codigo_manual}</td>
                </tr>
                <tr>
                    <td><b>ATIVIDADE:</b> {atividade}</td>
                    <td><b>LOCALIDADE:</b> Ibiporã, PR</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

# --- INTEGRAÇÃO NO SISTEMA ---
# Exemplo puxando do seu manual de códigos
with st.container():
    cabecalho_classificacao(
        cnpj="00.000.000/0001-00", 
        codigo_manual="IND-AL-05 (Industrial Alimentício)", 
        atividade="Produção e Envase de Óleos Vegetais"
    )

st.divider()
st.info("💡 **Davi Informa:** Classificação conforme Manual de Riscos Sênior. Normativos aplicáveis: NR-10, NR-13 e NBR-5410.")
