import streamlit as str_lit
import streamlit as st

# ============================================
# CONFIGURAÇÃO DA PÁGINA E CSS
# ============================================
st.set_page_config(page_title="Reações Orgânicas Visuais", page_icon="🧪", layout="wide")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp {background-color: #f8fafc;}
    .dashboard-card {background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); margin-bottom: 1.5rem;}
    .concept-box {background: #f1f5f9; border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 1.05rem;}
    .alert-box {background: #fffbeb; border-left: 4px solid #f59e0b; padding: 1rem; border-radius: 4px; margin-bottom: 1rem;}
    .main-title {font-size: 2.2rem; font-weight: 800; color: #0f172a; text-align: center; margin-bottom: 0.2rem;}
    .subtitle {font-size: 1.1rem; color: #64748b; text-align: center; margin-bottom: 2rem;}
</style>
""", unsafe_allow_html=True)

# ============================================
# FUNÇÃO DE RENDERIZAÇÃO VIA PUBCHEM (SEM RDKIT)
# ============================================
def visualizar_reacao(smiles_reagente, texto_seta, smiles_produto, legenda_reagente, legenda_produto):
    # URLs oficiais públicas do PubChem para gerar estruturas químicas em PNG
    url_reag = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/PNG?smiles={smiles_reagente}&image_size=300x200"
    url_prod = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/PNG?smiles={smiles_produto}&image_size=300x200"

    st.markdown("<div style='background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 1rem; margin-top: 10px;'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        st.markdown(f"<div style='text-align: center;'><img src='{url_reag}' width='100%' style='background:white; border-radius:4px;'><br><b style='color:#334155;'>{legenda_reagente}</b></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align: center; margin-top: 30%; font-size: 1.05rem; color:#64748b;'><b>{texto_seta}</b><br><span style='font-size:2rem; color:#3b82f6;'>&#10142;</span></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='text-align: center;'><img src='{url_prod}' width='100%' style='background:white; border-radius:4px;'><br><b style='color:#334155;'>{legenda_produto}</b></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# TÍTULO PRINCIPAL E ABAS
# ============================================
st.markdown('<div class="main-title">🧪 Laboratório de Reações Orgânicas Visuais</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Estudo interativo unindo fórmulas químicas e projeções geométricas de ligações</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "🔄 Substituição", 
    "➕ Adição & Regras", 
    "🔥 Oxirredução", 
    "⚗️ Esterificação"
])

# ============================================
# ABA 1: REAÇÕES DE SUBSTITUIÇÃO
# ============================================
with tab1:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Reações de Substituição (Alcanos e Aromáticos)")
    
    st.markdown("""
    <div class="concept-box">
    <b>Definição:</b> Processos onde substituímos um ou mais átomos por outros[cite: 1]. Típicos de moléculas muito estáveis (pouco reativas) como alcanos e anéis benzênicos[cite: 1].
    </div>
    """, unsafe_allow_html=True)
    
    tipo_subst = st.radio("Escolha a classe do composto:", ["Alcanos (Halogenação)", "Aromáticos (Benzeno)"], horizontal=True)
    
    if tipo_subst == "Alcanos (Halogenação)":
        st.markdown("### Halogenação do Propano")
        st.markdown("Em alcanos maiores, ocorre a formação de isômeros. O hidrogênio do carbono secundário é substituído com maior facilidade[cite: 1].")
        st.latex(r"H_3C-CH_2-CH_3 + Cl_2 \xrightarrow{\text{luz/calor}} H_3C-CHCl-CH_3 + HCl")
        
        visualizar_reacao("CCC", "+ Cl₂ (Luz/Calor)", "CC(Cl)C", "Propano", "2-cloropropano (Produto Principal)")
            
    else:
        st.markdown("### Substituição Eletrofílica Aromática")
        st.markdown("O anel benzênico possui ressonância que o torna muito estável[cite: 2]. O eletrófilo ataca o anel substituindo um Hidrogênio[cite: 3].")
        
        reacao_arom = st.selectbox("Selecione a Reação no Benzeno:", ["Halogenação (Cloração)", "Nitração", "Alquilação"])
        
        if reacao_arom == "Halogenação (Cloração)":
            st.latex(r"C_6H_6 + Cl_2 \xrightarrow{AlCl_3} C_6H_5Cl + HCl")
            visualizar_reacao("c1ccccc1", "+ Cl₂ (Cat. AlCl₃)", "Clc1ccccc1", "Benzeno", "Clorobenzeno")
            
        elif reacao_arom == "Nitração":
            st.latex(r"C_6H_6 + HNO_3 \xrightarrow{H_2SO_4} C_6H_5NO_2 + H_2O")
            visualizar_reacao("c1ccccc1", "+ HNO₃ (H₂SO₄)", "O=[N+]([O-])c1ccccc1", "Benzeno", "Nitrobenzeno")
            
        elif reacao_arom == "Alquilação":
            st.latex(r"C_6H_6 + CH_3Cl \xrightarrow{AlCl_3} C_6H_5CH_3 + HCl")
            visualizar_reacao("c1ccccc1", "+ CH₃Cl (AlCl₃)", "Cc1ccccc1", "Benzeno", "Tolueno (Metilbenzeno)")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ABA 2: REAÇÕES DE ADIÇÃO
# ============================================
with tab2:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Reações de Adição em Insaturados")
    
    col_ad1, col_ad2 = st.columns([1, 1])
    
    with col_ad1:
        st.markdown("""
        <div class="alert-box">
        <b>Regra de Markovnikoff:</b> Na adição de moléculas do tipo H-B (ex: HBr, H2O) a uma dupla ligação, o átomo de Hidrogênio liga-se ao carbono da dupla que já possui <b>mais hidrogênios</b>[cite: 6].
        </div>
        """, unsafe_allow_html=True)
        st.markdown("#### Hidrohalogenação do Propeno")
        st.latex(r"H_3C-CH=CH_2 + HBr \rightarrow H_3C-CHBr-CH_3")
        
    with col_ad2:
        st.markdown("#### Teste do Bromo (Identificação visual)")
        st.markdown("Usado para identificar ligações duplas (descoramento imediato do líquido castanho do $Br_2$)[cite: 7].")
        st.latex(r"H_2C=CH_2 + Br_2 \rightarrow Br-CH_2-CH_2-Br")
        
    st.markdown("### Representações Geométricas das Adições")
    ex_adicao = st.radio("Selecione a reação geométrica:", ["Adição de HBr (Markovnikoff)", "Bromação do Eteno (Teste de Laboratório)"], horizontal=True)
    
    if ex_adicao == "Adição de HBr (Markovnikoff)":
        visualizar_reacao("C=CC", "+ HBr", "CC(Br)C", "Propeno (Carbono terminal mais hidrogenado)", "2-bromopropano")
    else:
        visualizar_reacao("C=C", "+ Br₂", "BrCCBr", "Eteno", "1,2-dibromoetano")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ABA 3: OXIDAÇÃO DE ÁLCOOIS
# ============================================
with tab3:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Processos de Oxirredução")
    
    st.markdown("""
    <div class="concept-box">
    A oxidação de carbono em compostos orgânicos é identificada pelo <b>aumento do número de ligações com oxigênio</b> (ou perda de hidrogênios)[cite: 8]. Utilizam-se oxidantes como $K_2Cr_2O_7$ ou $KMnO_4$[cite: 9].
    </div>
    """, unsafe_allow_html=True)
    
    tipo_alcool = st.selectbox("Selecione o nível de oxidação:", ["Álcool Primário (Dupla oxidação)", "Álcool Secundário (Oxidação única)"])
    
    if tipo_alcool == "Álcool Primário (Dupla oxidação)":
        st.markdown("O etanol sofre oxidação formando um aldeído, e em seguida adquire oxigênio formando ácido carboxílico[cite: 9].")
        st.latex(r"H_3C-CH_2-OH \xrightarrow{[O]} H_3C-C(=O)H \xrightarrow{[O]} H_3C-COOH")
        
        col_ox1, col_ox2 = st.columns(2)
        with col_ox1:
            visualizar_reacao("CCO", "[O] (1ª Etapa)", "CC=O", "Etanol (Álcool)", "Etanal (Aldeído)")
        with col_ox2:
            visualizar_reacao("CC=O", "[O] (2ª Etapa)", "CC(=O)O", "Etanal", "Ácido Acético/Etanoico")
            
    else:
        st.markdown("Álcoois secundários oxidam-se apenas até o estágio de cetona[cite: 9].")
        st.latex(r"H_3C-CH(OH)-CH_3 \xrightarrow{KMnO_4, H_2SO_4} H_3C-CO-CH_3 + H_2O")
        visualizar_reacao("CC(O)C", "[O]", "CC(=O)C", "Propan-2-ol", "Propanona (Cetona)")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ABA 4: ESTERIFICAÇÃO E DESIDRATAÇÃO
# ============================================
with tab4:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Síntese: Esterificação e Eliminação")
    
    reacao_sintese = st.radio("Selecione a síntese geométrica:", ["Esterificação (Ácido + Álcool)", "Desidratação Intramolecular (Formação de Dupla)"], horizontal=True)
    
    if reacao_sintese == "Esterificação (Ácido + Álcool)":
        st.markdown("""
        <div class="concept-box">
        Reação reversível formadora de fragrâncias e flavorizantes[cite: 10].<br>
        <b>Ácido Carboxílico + Álcool $\rightleftharpoons$ Éster + Água</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Síntese da Essência de Maçã (Butanoato de Metila)**[cite: 10]")
        st.latex(r"H_3C-(CH_2)_2-COOH + HO-CH_3 \xrightarrow{H^+} H_3C-(CH_2)_2-COO-CH_3 + H_2O")
        
        visualizar_reacao("CCCC(=O)O", "Catalisador Ácido (H⁺) + Metanol", "CCCC(=O)OC", "Ácido Butanoico", "Butanoato de Metila")
        
    else:
        st.markdown("""
        <div class="alert-box">
        As reações de eliminação são o inverso exato das adições, com retirada de moléculas pequenas como $H_2O$[cite: 7].
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Desidratação do Etanol sob $170^\circ C$ (Formação do Eteno)**[cite: 7]")
        st.latex(r"H_3C-CH_2-OH \xrightarrow{H_2SO_4, 170^\circ C} H_2C=CH_2 + H_2O")
        
        visualizar_reacao("CCO", "H₂SO₄ (170°C) -H₂O", "C=C", "Etanol", "Eteno (Ligação Dupla Formada)")

    st.markdown('</div>', unsafe_allow_html=True)
