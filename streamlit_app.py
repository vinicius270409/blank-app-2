import streamlit as st

st.set_page_config(page_title="Análise de Perfil", page_icon="👤")

st.title(" sistema de Análise de Desempenho Pessoal")

nome = st.text_input("nome do avaliado:")
foco = st.radio("qual sua maior habilidade hoje?", (
    "Ser Bumbum guloso maximmo", 
    "Dar", 
    "Receber",
    "todos"
))
rotina = st.text_input("quanto vc deu hoje")

if nome and foco and rotina:
    st.write("---")
    st.write(f"###  analisando dados de bumbumzinho de **{nome}**...")
    
    try:
        horas = float(rotina)
        if horas <= 2:
            status_produtividade = "Praticamente um encosto. Fez absolutamente nada relevante."
        else:
            status_produtividade = "Contando as horas que passou dando ne."
    except:
        status_produtividade = "Bumbum guloso maquisimo"

    st.error("**diagnostico:**")
    st.write(f"• **Comportamento Padrão:** {foco}.")
    st.write(f"• **Nível de Rendimento:** {status_produtividade}")
    st.write(f"• **Conclusão:** ta dano bem.")

    if st.button("Finalizar Relatório"):
        st.info("Relatório gerado. parabens, bumbumzo gulosio.")
