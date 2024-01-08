from pathlib import Path
import streamlit as st
from PIL import Image
import os

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
curriculum_file = current_dir / "assets" / "Thiago_Regueira-CV.pdf"
foto = current_dir / "assets" / "profile-pic (5).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Thiago Regueira"
PAGE_ICON = ":wave:"
NAME = "Thiago Regueira"
DESCRIPTION = """
Engenheiro e Analista de Dados | Desenvolvedor Web 
"""
EMAIL = "thiago.regueira@yahoo.com.br"

PROJECTS = {
    "🏅 Dashboard de Vendas - Por ano": "https://vendas-imersao.streamlit.app/",
    "🏅 Estudo sobre suicídios no Brasil - 2014 a 2018": "https://estudo-suicidios-2014-2018.streamlit.app/",
    "🏅 Análise de Turnover - Desafio Escola preditiva.ai": "https://turnover.streamlit.app/",
    "🏅 Remover fundo de foto - Baseado no notebook da Fernanda Santos @f3loc": "https://remover-fundo-foto.streamlit.app/",
}


# --- PAGE STREAMLIT SETTINGS ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF and PROFILE PICTURE ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(curriculum_file, "rb") as pdf_file:
    pdf_bytes = pdf_file.read()


profile_pic = Image.open(foto)


# --- BODY SETTINGS ---
col1, col2 = st.columns([1, 2], gap="large")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(
        '<p style="text-align: justify; font-size: 16px">{DESCRIPTION}</p>'.format(
            DESCRIPTION=DESCRIPTION
        ),
        unsafe_allow_html=True,
    )
    st.download_button(
        label="📄 Download CV",
        data=pdf_bytes,
        file_name=curriculum_file.name,
        mime="application/octet-stream",
    )

    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
col3, col4 = st.columns(2)
with col3:
    st.write(
        "[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/thiagoregueira/)"
    )
with col4:
    st.write(
        "[![GitHub](https://img.shields.io/badge/-GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/thiagoregueira)"
    )


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.write("<h2>🌎Experiências e Qualificações</h2>", unsafe_allow_html=True)
st.write("---")
st.write(
    """<p class="tab" style="text-align: justify;">
Como atual estudante de Engenharia de Dados, almejo uma sólida formação acadêmica em Engenharia de Dados/PUC-Minas, aliada a uma paixão incansável por tecnologia e pelo mundo dos dados. Minha trajetória profissional, notadamente como Gerente Personalizado no Banco do Brasil, forneceu uma base robusta em liderança e tomada de decisões estratégicas. Essa experiência, somada aos cinco anos como Escriturário, onde desenvolvi habilidades exemplares de comunicação e resolução de problemas, consolidou minha capacidade de oferecer soluções personalizadas a clientes diversos.</p>
        """,
    unsafe_allow_html=True,
)


# --- EDUCATION ---
st.write("#")
st.write("<h2>🎓Formação Acadêmica</h2>", unsafe_allow_html=True)
st.write("---")

st.write("""<h4>Engenharia de Dados | PUC-Minas</h4>""", unsafe_allow_html=True)
st.write("08/2023 - 12/2025" + " | " + "Graduando")
st.write("#")
st.write("#")
st.write("<h4>Tecnologia em Gestão Ambiental | UNINASSAU</h4>", unsafe_allow_html=True)
st.write("08/2020 - 12/2022" + " | " + "Graduado")


# --- WORK HISTORY ---
st.write("#")
st.write("<h2>💼Histórico de Trabalho</h2>", unsafe_allow_html=True)
st.write("---")

# --- JOB 1
st.write("#")
st.write(
    """<h4>👨‍💻 Gerente de Relacionamento | Banco do Brasil</h4>""",
    unsafe_allow_html=True,
)
st.write("08/2014 - 02/2021")
st.write(
    """
<li style="text-align: justify;">✅ Realizei diversas análises de planilhas e relatórios a fim de preparar as melhores ofertas aos vários perfis de clientes;</li>
<li style="text-align: justify;">✅ Sempre estabeleci uma ótima comunicação e relacionamento com os clientes;</li>
<li style="text-align: justify;">✅ Liderei, gerenciei equipes e analisei indicadores de desempenho e eficiência;</li>
<li style="text-align: justify;">✅ Desenvolvi novos negócios com os clientes existentes e busquei ativamente novas oportunidades de vendas de acordo com seu perfil;</li>
<li style="text-align: justify;">✅ Analisei relatórios e planilhas de clientes com perfil de recuperação de crédito para propor a melhor forma de negociação;</li>
""",
    unsafe_allow_html=True,
)


# --- JOB 2
st.write("#")
st.write("#")
st.write("<h4>👷", "Escriturário | Banco do Brasil S.A</h4>", unsafe_allow_html=True)
st.write("03/2011 - 08/2014")
st.write(
    """
<li style="text-align: justify;">✅ Prestei vários atendimentos tanto presenciais como teleatendimento;</li>
<li style="text-align: justify;">✅Ofereci e vendi produtos e serviços através do atendimento presencial e teleatendimento;</li>
<li style="text-align: justify;">✅ Realizei novos cadastros e atualizei os já existentes;</li>
<li style="text-align: justify;">✅ Realizei retenção e recuperação de clientes;</li>
<li style="text-align: justify;">✅ Renegociei e recuperei clientes inadimplentes;</li>
""",
    unsafe_allow_html=True,
)


# --- Projects & Accomplishments ---
st.write("#")
st.write("<h2>🏆Projetos e Conquistas</h2>", unsafe_allow_html=True)
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- CERTIFICATIONS ---
st.write("#")
st.write("<h2>📓Cursos e Certificações</h2>", unsafe_allow_html=True)
st.write("---")

with st.expander("📚Lista Completa - Clique aqui!"):
    diretorio_certificados = os.path.join(current_dir, "images")

    certificacoes = {
        "FIC INGLÊS BÁSICO: NÍVEL INSTRUMENTAL I, IFMG": os.path.join(
            diretorio_certificados, "FIC_INGLES_BASICO_NIVEL_INSTRUMENTAL_I_IFMG.pdf"
        ),
        "Oracle Cloud Infrastructure AI Certified Foundations Associate, Oracle": os.path.join(
            diretorio_certificados,
            "Oracle Cloud Infrastructure AI Certified Foundations Associate, Oracle.pdf",
        ),
        "Oracle Cloud Infrastructure Certified Foundations Associate, Oracle": os.path.join(
            diretorio_certificados,
            "Oracle Cloud Infrastructure Certified Foundations Associate, Oracle.pdf",
        ),
        "Oracle Cloud Data Management Certified Foundations Associate, Oracle": os.path.join(
            diretorio_certificados,
            "Oracle Cloud Data Management Certified Foundations Associate, Oracle.pdf",
        ),
        "FUNDAMENTOS DE ANALYTICS, Escola Preditiva": os.path.join(
            diretorio_certificados, "FUNDAMENTOS DE ANALYTICS, Escola Preditiva.pdf"
        ),
        "EXCEL PARA ANÁLISE DE DADOS, Escola Preditiva": os.path.join(
            diretorio_certificados, "EXCEL PARA ANÁLISE DE DADOS, Escola Preditiva.pdf"
        ),
        "DATA ANALYTICS, Escola Preditiva": os.path.join(
            diretorio_certificados, "DATA ANALYTICS, Escola Preditiva.pdf"
        ),
        "FORMAÇÃO EM ENGENHARIA DE DADOS, UNI1500": os.path.join(
            diretorio_certificados, "FORMAÇÃO EM ENGENHARIA DE DADOS, UNI1500.pdf"
        ),
        "GOOGLE DATA ANALYTICS, Google/Coursera": os.path.join(
            diretorio_certificados, "GOOGLE DATA ANALYTICS, GoogleCoursera.pdf"
        ),
        "INTRODUÇÃO À CIÊNCIA DA COMPUTAÇÃO COM PYTHON, Universidade de São Paulo/Coursera": os.path.join(
            diretorio_certificados,
            "INTRODUÇÃO À CIÊNCIA DA COMPUTAÇÃO COM PYTHON, Universidade de São PauloCoursera.pdf",
        ),
        "LÓGICA DE PROGRAMAÇÃO COM PYTHON, Treina Recife": os.path.join(
            diretorio_certificados,
            "LÓGICA DE PROGRAMAÇÃO COM PYTHON, Treina Recife.pdf",
        ),
        "ANÁLISE DE DADOS COM PYTHON, Treina Recife": os.path.join(
            diretorio_certificados, "ANÁLISE DE DADOS COM PYTHON, Treina Recife.pdf"
        ),
        "CURSO SQL, Treina Recife": os.path.join(
            diretorio_certificados, "CURSO SQL, Treina Recife.pdf"
        ),
        "DESENVOLVIMENTO JAVA COM CLOUD AWS, Digital Innovation One": os.path.join(
            diretorio_certificados,
            "DESENVOLVIMENTO JAVA COM CLOUD AWS, Digital Innovation One.pdf",
        ),
        "BACKEND JAVA, Santander Bootcamp, Digital Innovation One": os.path.join(
            diretorio_certificados,
            "BACKEND JAVA, Santander Bootcamp, Digital Innovation One.pdf",
        ),
        "SCRUM FUNDAMENTALS CERTIFIED (SFC), ScrumStudy": os.path.join(
            diretorio_certificados, "SCRUM FUNDAMENTALS CERTIFIED (SFC), ScrumStudy.pdf"
        ),
        "FEA-dev USP Python do Básico ao Intermediário": os.path.join(
            diretorio_certificados, "FEA-dev USP Python do Básico ao Intermediário.pdf"
        ),
    }

    for nome_certificado, caminho_certificado in certificacoes.items():
        st.write(nome_certificado)  # Exibe o nome da certificação
        try:
            with open(caminho_certificado, "rb") as arquivo_pdf:
                bytes_pdf = arquivo_pdf.read()
                st.download_button(
                    label="Visualizar Certificado",
                    data=bytes_pdf,
                    file_name=os.path.basename(caminho_certificado),
                    mime="application/pdf",
                )
        except FileNotFoundError:
            st.error(f"Arquivo não encontrado: {caminho_certificado}")

# --- Soft Skills ---

soft = {
    "Empatia": 100,
    "Proatividade": 100,
    "Responsabilidade": 100,
    "Resolução de problemas": 100,
    "Organização": 100,
    "Gerenciamento de tempo": 100,
    "Atenção aos detalhes": 100,
    "Trabalho em equipa": 100,
    "Liderança": 100,
    "Comunicação": 100,
    "Adaptabilidade": 100,
    "Pensamento Analítico": 100,
}

st.sidebar.write(
    "<h1 style='text-align: center; font-size: 32px; color: #002b36;'>Competências</h1>",
    unsafe_allow_html=True,
)

# Adicionando as barras de progresso na sidebar
st.sidebar.write(
    "<h2 style='text-align: center; color: #002b36;'>Soft Skills</h2>",
    unsafe_allow_html=True,
)

for competencia, valor in soft.items():
    st.sidebar.progress(valor, text=competencia)

hard = {
    "Microsoft Excel": 90,
    "Banco de Dados Relacionais e Não Relacionais": 100,
    "SQL": 90,
    "MySQL": 90,
    "PostgreSQL": 90,
    "SQlite": 90,
    "SQL Server": 90,
    "Oracle": 80,
    "Python": 90,
    "Django": 70,
    "Flask": 70,
    "Pandas": 90,
    "Plotly": 90,
    "Streamlit": 90,
    "Estatística descritiva": 80,
    "Teste de hipóteses": 70,
    "Testes de normalidade": 70,
    "Modelagem e Análise de Dados": 80,
    "Migração de dados": 75,
    "Armazenamento de dados": 90,
    "Segurança e Privacidade de Dados": 75,
    "Power BI": 90,
    "Java": 90,
    "Spring": 80,
    "Desenvolvimento de API": 100,
    "Git/GitHub": 100,
    "AWS": 70,
    "Microsoft Azure": 80,
    "Metodologias Ágeis": 100,
    "Oracle Cloud": 75,
}

st.write("#")

st.sidebar.write(
    "<h2 style='text-align: center; color: #002b36;'>Hard Skills</h2>",
    unsafe_allow_html=True,
)

for competencia, valor in hard.items():
    st.sidebar.progress(valor, text=competencia)
