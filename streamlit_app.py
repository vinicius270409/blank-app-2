import streamlit as st

st.set_page_config(page_title="Análise de Perfil", page_icon="👤")

st.title("👤 Sistema de Análise de Desempenho Pessoal")

nome = st.text_input("Nome do avaliado:")
foco = st.radio("Qual sua maior habilidade hoje?", (
    "Sumir do grupo do WhatsApp por dias", 
    "Visualizar as mensagens e responder só na mente", 
    "Fazer planos e desistir 2 horas depois",
    "Manter o foco por no máximo 4 minutos"
))
rotina = st.text_input("Quantas horas produtivas você teve hoje?")

if nome and foco and rotina:
    st.write("---")
    st.write(f"### ⚙️ Analisando dados de **{nome}**...")
    
    try:
        horas = float(rotina)
        if horas <= 2:
            status_produtividade = "Praticamente um encosto. Fez absolutamente nada relevante."
        else:
            status_produtividade = "Contando as horas que passou fingindo que estava fazendo algo útil."
    except:
        status_produtividade = "Incapaz de quantificar a própria rotina."

    st.error("**📋 DIAGNÓSTICO DO USUÁRIO:**")
    st.write(f"• **Comportamento Padrão:** {foco}.")
    st.write(f"• **Nível de Rendimento:** {status_produtividade}")
    st.write(f"• **Conclusão:** Se o objetivo era a mediocridade, parabéns pelo excelente trabalho.")

    if st.button("Finalizar Relatório"):
        st.info("Relatório gerado. Pare de procrastinar e responda quem te mandou esse link.")
