import streamlit as st

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================
st.set_page_config(
    page_title="Reações Orgânicas Interativas",
    page_icon="🧪",
    layout="wide"
)

# ============================================
# CSS PROFISSIONAL 
# ============================================
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #f8fafc;}
    .dashboard-card {background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); margin-bottom: 1.5rem;}
    .concept-box {background: #f1f5f9; border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 1.05rem;}
    .alert-box {background: #fffbeb; border-left: 4px solid #f59e0b; padding: 1rem; border-radius: 4px; margin-bottom: 1rem;}
    .success-box {background: #f0fdf4; border-left: 4px solid #10b981; padding: 1rem; border-radius: 4px;}
    .main-title {font-size: 2.4rem; font-weight: 800; color: #0f172a; text-align: center; margin-bottom: 0.2rem;}
    .subtitle {font-size: 1.1rem; color: #64748b; text-align: center; margin-bottom: 2rem;}
</style>
""", unsafe_allow_html=True)

# ============================================
# TÍTULO PRINCIPAL
# ============================================
st.markdown('<div class="main-title">🧪 Laboratório de Reações Orgânicas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Estudo interativo de Substituição, Adição, Eliminação e Oxirredução</div>', unsafe_allow_html=True)

# ============================================
# ABAS DE NAVEGAÇÃO
# ============================================
tab1, tab2, tab3, tab4 = st.tabs([
    "🔄 Substituição", 
    "➕ Adição & Regras", 
    "🔥 Oxirredução", 
    "⚗️ Esterificação & Desidratação"
])

# ============================================
# ABA 1: REAÇÕES DE SUBSTITUIÇÃO
# ============================================
with tab1:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Reações de Substituição")
    
    st.markdown("""
    <div class="concept-box">
    <b>Definição:</b> São processos químicos onde substituímos (trocamos) um ou mais átomos (ou grupos) por outros[cite: 1]. São muito características de substâncias pouco reativas, como os alcanos (derivados do petróleo) e os aromáticos[cite: 1].
    </div>
    """, unsafe_allow_html=True)
    
    tipo_subst = st.radio("Escolha a classe do composto:", ["Alcanos (Saturados)", "Aromáticos (Benzeno e Derivados)"], horizontal=True)
    
    if tipo_subst == "Alcanos (Saturados)":
        st.markdown("### Halogenação por Radicais Livres")
        st.markdown("Os alcanos só reagem em condições muito energéticas (luz ou calor)[cite: 1]. A reação com halogênios (família 7A: $F_2, Cl_2, Br_2$) ocorre por radicais livres[cite: 1].")
        
        ex_alcano = st.selectbox("Selecione o exemplo:", ["Metano (Monocloração)", "Propano (Cloração isomérica)"])
        
        if ex_alcano == "Metano (Monocloração)":
            st.latex(r"CH_4 + Cl_2 \xrightarrow{\text{luz/calor}} H_3C-Cl + HCl")
            st.caption("Ocorre uma reação de substituição de um átomo de H por um átomo de Cl[cite: 1].")
        else:
            st.latex(r"H_3C-CH_2-CH_3 + Cl_2 \xrightarrow{\text{luz}} \text{Mistura de Isômeros}")
            st.markdown("Pode resultar na substituição no carbono 1 ou no carbono 2[cite: 1]:")
            st.latex(r"\text{1-cloropropano: } H_3C-CH_2-CH_2-Cl \quad \text{ou} \quad \text{2-cloropropano: } H_3C-CHCl-CH_3")
            
    else:
        st.markdown("### Substituição Eletrofílica em Aromáticos")
        st.markdown("O anel benzênico possui ressonância (compartilhamento simultâneo de seis elétrons) que o torna muito estável e blindado[cite: 2]. O agente que ataca o anel é um eletrófilo ($E^+$), que tem afinidade por elétrons[cite: 3].")
        
        col_arom1, col_arom2 = st.columns([1, 1])
        with col_arom1:
            reacao_arom = st.selectbox("Selecione a Reação:", ["Halogenação", "Nitração", "Alquilação", "Sulfonação"])
            
            if reacao_arom == "Halogenação":
                st.markdown("**Reagente:** $X_2$ ($Cl_2$ ou $Br_2$) | **Catalisador:** $FeX_3$ ou $AlX_3$[cite: 3]")
                st.latex(r"C_6H_6 + Cl_2 \xrightarrow{AlCl_3} C_6H_5Cl \text{ (clorobenzeno)} + HCl")
            elif reacao_arom == "Nitração":
                st.markdown("**Reagente:** Ácido Nítrico ($HNO_3$) | **Catalisador:** $H_2SO_4$[cite: 3]")
                st.latex(r"C_6H_6 + HO-NO_2 \xrightarrow{H_2SO_4} C_6H_5NO_2 \text{ (nitrobenzeno)} + H_2O")
            elif reacao_arom == "Alquilação":
                st.markdown("**Reagente:** Halogeneto de Alquila ($R-X$) | **Catalisador:** $FeX_3, AlX_3$[cite: 3]")
                st.latex(r"C_6H_6 + Cl-CH_3 \xrightarrow{AlCl_3} C_6H_5CH_3 \text{ (tolueno)} + HCl")
            elif reacao_arom == "Sulfonação":
                st.markdown("**Reagente:** Ácido Sulfúrico concentrado ($H_2SO_4 / SO_3$)[cite: 3]")
                st.latex(r"C_6H_6 + HO-SO_3H \xrightarrow{\Delta} C_6H_5SO_3H \text{ (ácido benzenossulfônico)} + H_2O")
                
        with col_arom2:
            st.markdown("""
            <div class="alert-box">
            <b>Orientação de Substituintes (Dirigentes):</b><br>
            Se o anel já tiver um grupo ligado, ele direciona o próximo ataque[cite: 4]:<br>
            • <b>Ortoparadirigentes (G):</b> Cedem elétrons (ex: -OH, -CH3). O ataque ocorre nas posições <i>orto</i> e <i>para</i>[cite: 4].<br>
            • <b>Metadirigentes (G'):</b> Retiram elétrons (ex: -NO2). O ataque ocorre na posição <i>meta</i>[cite: 4].
            </div>
            """, unsafe_allow_html=True)
            if reacao_arom == "Nitração":
                st.info("Exemplo Clássico: A trinitração do Tolueno gera o explosivo TNT (Trinitrotolueno)[cite: 4].")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ABA 2: REAÇÕES DE ADIÇÃO E TESTES
# ============================================
with tab2:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Reações de Adição em Insaturados")
    
    st.markdown("""
    <div class="concept-box">
    <b>Definição:</b> Acontece em hidrocarbonetos insaturados (alcenos e alcinos). A ligação dupla ou tripla é rompida (reação de adição) para a entrada de novos átomos[cite: 5].
    </div>
    """, unsafe_allow_html=True)
    
    col_ad1, col_ad2 = st.columns([1.5, 1])
    
    with col_ad1:
        st.markdown("### Regra de Markovnikoff")
        st.markdown("""
        <div class="alert-box">
        Na adição de uma substância do tipo H-B (como HCl ou H2O) a hidrocarbonetos insaturados, o átomo de hidrogênio (H) liga-se ao carbono insaturado <b>mais hidrogenado</b>[cite: 6].
        </div>
        """, unsafe_allow_html=True)
        
        ex_adicao = st.selectbox("Simular Adição ao Propeno ($H_3C-CH=CH_2$):", ["Adição de HBr (Hidrohalogenação)", "Adição de H2O (Hidratação)"])
        
        if ex_adicao == "Adição de HBr (Hidrohalogenação)":
            st.latex(r"H_3C-CH=CH_2 + H-Br \rightarrow H_3C-CHBr-CH_3")
            st.caption("Produto Principal: 2-bromopropano (O hidrogênio vai para a extremidade CH2)[cite: 6].")
        else:
            st.latex(r"H_3C-CH=CH_2 + H-OH \xrightarrow{H_2SO_4} H_3C-CH(OH)-CH_3")
            st.caption("Produto Principal: propan-2-ol[cite: 6].")

    with col_ad2:
        st.markdown("### 🧪 Laboratório de Testes Visuais")
        st.markdown("Testes clássicos para diferenciar compostos reativos (insaturados) de compostos pouco reativos (alcanos/aromáticos)[cite: 6].")
        
        teste = st.radio("Selecione o Teste Químico:", ["Teste de Baeyer (KMnO4)", "Teste do Bromo (Br2)"])
        
        if teste == "Teste de Baeyer (KMnO4)":
            st.markdown("""
            <div class="success-box">
            <b>Reagente:</b> Permanganato de Potássio ($KMnO_4$) diluído, de forte coloração violeta[cite: 6].<br><br>
            <b>Teste Positivo (Insaturado):</b> A solução descolore (fica incolor/marrom), indicando a oxidação da dupla[cite: 6].<br>
            <b>Teste Negativo (Saturado/Aromático):</b> A solução continua violeta (não há reação)[cite: 6].
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="success-box">
            <b>Reagente:</b> Solução de Bromo ($Br_2 / CCl_4$), líquido castanho[cite: 7].<br><br>
            <b>Teste Positivo:</b> Descoramento imediato do líquido castanho ao quebrar a dupla ligação (adição do $Br_2$)[cite: 7].
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ABA 3: OXIDAÇÃO E REDUÇÃO
# ============================================
with tab3:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Oxirredução de Compostos Orgânicos")
    
    col_ox1, col_ox2 = st.columns([1, 1.5])
    
    with col_ox1:
        st.markdown("### Agentes Comuns")
        st.markdown("**Oxidantes [O]** (roubam elétrons): $K_2Cr_2O_7$, $KMnO_4$, $O_3$, $H_2O_2$[cite: 8].")
        st.markdown("**Redutores [H]** (doam elétrons): $LiAlH_4$, $NaBH_4$, $H_2$[cite: 8].")
        
        st.markdown("""
        <div class="alert-box">
        <b>Antioxidantes:</b> Compostos (como a Vitamina C e E) que doam elétrons vigorosamente. São "materiais de sacrifício" que sofrem oxidação para preservar outras células e alimentos[cite: 9].
        </div>
        """, unsafe_allow_html=True)

    with col_ox2:
        st.markdown("### Oxidação de Álcoois")
        st.markdown("O aumento de ligações com oxigênio é a principal evidência da oxidação do carbono[cite: 8].")
        
        tipo_alcool = st.selectbox("Selecione a oxidação de qual tipo de álcool?", ["Álcool Primário", "Álcool Secundário", "Álcool Terciário"])
        
        if tipo_alcool == "Álcool Primário":
            st.latex(r"\text{Etanol} \xrightarrow{[O]} \text{Etanal (Aldeído)} \xrightarrow{[O]} \text{Ácido Acético}")
            st.caption("Pode ter uma ou duas oxidações dependendo da temperatura e força do oxidante[cite: 9].")
        elif tipo_alcool == "Álcool Secundário":
            st.latex(r"\text{Propan-2-ol} \xrightarrow{KMnO_4, H_2SO_4} \text{Propanona (Cetona)}")
            st.caption("A oxidação para na cetona[cite: 9].")
        else:
            st.latex(r"\text{2-metilpropan-2-ol} \xrightarrow{[O]} \text{NÃO OCORRE REAÇÃO}")
            st.caption("Álcoois terciários são resistentes e não oxidam sob condições usuais[cite: 9].")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ABA 4: SÍNTESE (ESTERIFICAÇÃO) E ELIMINAÇÃO
# ============================================
with tab4:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("Síntese Orgânica Básica")
    
    col_e1, col_e2 = st.columns([1, 1])
    
    with col_e1:
        st.markdown("### Reação de Esterificação")
        st.markdown("""
        <div class="concept-box">
        <b>Ácido Carboxílico + Álcool $\rightleftharpoons$ Éster + Água</b><br>
        Os ésteres são compostos aromáticos famosos pelos odores agradáveis de frutas e flores[cite: 10]. A reação é reversível (a volta é chamada de hidrólise)[cite: 10].
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Exemplo: Odor de Maçã (Butanoato de metila)**[cite: 10]")
        st.latex(r"H_3C-CH_2-CH_2-COOH + HO-CH_3 \xrightarrow{H_2SO_4, \Delta} H_3C-(CH_2)_2-COO-CH_3 + H_2O")
        
        st.markdown("**Exemplo: Odor de Abacaxi (Butanoato de etila)**[cite: 10]")
        st.latex(r"H_3C-CH_2-CH_2-COOH + HO-CH_2-CH_3 \rightleftharpoons \text{Éster} + H_2O")

    with col_e2:
        st.markdown("### Reações de Eliminação (Desidratação)")
        st.markdown("Ocorrem de forma exatamente inversa às adições[cite: 7]. O ácido sulfúrico ($H_2SO_4$) atua como poderoso agente desidratante[cite: 8].")
        
        tipo_des = st.radio("Tipos de Desidratação de Álcoois:", ["Intramolecular", "Intermolecular"])
        
        if tipo_des == "Intramolecular":
            st.markdown("Ocorre dentro da mesma molécula sob temperaturas elevadas ($170^\circ C$)[cite: 7]. **Forma Alcenos.**")
            st.latex(r"H_3C-CH_2-OH \xrightarrow{170^\circ C, H_2SO_4} H_2C=CH_2 \text{ (eteno)} + H_2O")
        else:
            st.markdown("Ocorre entre duas moléculas de álcool sob temperaturas um pouco menores ($140^\circ C$)[cite: 8]. **Forma Éteres.**")
            st.latex(r"2 \times H_3C-CH_2-OH \xrightarrow{H_2SO_4} H_3C-CH_2-O-CH_2-CH_3 \text{ (éter dietílico)} + H_2O")

    st.markdown('</div>', unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 0.85rem; padding: 1rem;">
    👨‍🔬 <b>Plataforma de Química Orgânica</b> — Baseado em materiais didáticos padronizados
</div>
""", unsafe_allow_html=True)