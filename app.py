import streamlit as st

# ✅ O PRIMEIRO COMANDO STREAMLIT TEM QUE SER ESSE
st.set_page_config(page_title="Teste de Perfil Empreendedor", layout="centered")

# Interface
st.title("💡 Teste de Perfil Empreendedor")
st.markdown("Responda às perguntas abaixo para descobrir seu perfil empreendedor e receber dicas personalizadas!")

# Perguntas e variáveis
perguntas = {
    "Você se considera uma pessoa **proativa**?": "proatividade",
    "Você costuma **planejar suas ações** antes de executá-las?": "planejamento",
    "Você lida bem com **riscos e incertezas**?": "tolerancia_ao_risco",
    "Você tem facilidade em **inovar** ou propor novas ideias?": "inovacao",
    "Você insiste mesmo quando algo parece **difícil**?": "persistencia"
}

respostas = {}

st.markdown("---")

# Sliders sem valor padrão
for pergunta, chave in perguntas.items():
    respostas[chave] = st.slider(pergunta, 1, 5, key=chave)

st.markdown("---")

# Botão de resultado
if st.button("🎯 Ver meu perfil"):
    if all(respostas.values()):
        total = sum(respostas.values())

        if total >= 22:
            perfil = "Visionária"
            descricao = "Você enxerga além do óbvio, busca oportunidades e ama inovação!"
            dicas = [
                "Participe de eventos de startups e inovação",
                "Colabore com pessoas mais analíticas para equilibrar sua visão",
                "Transforme ideias em projetos práticos"
            ]
        elif 17 <= total < 22:
            perfil = "Planejadora"
            descricao = "Você prefere agir com estratégia e organização. Gosta de saber onde pisa antes de decidir."
            dicas = [
                "Pratique tomadas de decisão mais rápidas",
                "Use ferramentas como Kanban ou Trello",
                "Busque situações que estimulem flexibilidade"
            ]
        else:
            perfil = "Executora"
            descricao = "Você gosta de colocar a mão na massa! Aprende fazendo e tem energia para agir."
            dicas = [
                "Invista em planejamento de médio/longo prazo",
                "Trabalhe sua tolerância a erros",
                "Estude fundamentos de gestão"
            ]

        st.subheader(f"🔍 Seu perfil: **{perfil}**")
        st.write(descricao)

        st.markdown("### 📌 Dicas para você:")
        for dica in dicas:
            st.markdown(f"- {dica}")
    else:
        st.warning("⚠️ Por favor, responda todas as perguntas antes de ver o resultado.")
