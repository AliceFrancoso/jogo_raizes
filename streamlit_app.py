import streamlit as st

border_style = """
    <style>
        .border {
            border: 2px solid #cb5637; /* cor da borda */
            background-color:rgb(249, 169, 121, 0.5);
            border-shadow: 2px;
            color: #cb5637;
            border-radius: 35px; /* cantos arredondados */
            margin-left: 22px;
            text-align: center;
            width: 300px;
            box-shadow: -25px 20px 35px rgb(249, 169, 121);
            margin-bottom: 60px;
        }
    </style>
"""

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #eeffe6; /* Altera o fundo da área principal */
    }
    </style>
""", unsafe_allow_html=True)


# Adicionando CSS ao aplicativo
st.markdown(border_style, unsafe_allow_html=True)

# Conteúdo com borda
st.markdown('<div class="border"><h1>Qual é a boca?</h1></div>', unsafe_allow_html=True)

# CSS para estilo dos botões
import streamlit as st

# Adicionando o CSS com Flexbox para layout 2x2
st.markdown("""
    <style>
        .button-container {
            display: flex;
            flex-wrap: wrap; /* Permite quebra de linha */
            justify-content: center; /* Centraliza horizontalmente */
            gap: 40px; /* Espaçamento entre os botões */
        }

        .custom-button {
            background-color: #a8cc98; /* Cor de fundo */
            color: white; /* Cor do texto */
            padding: 10px 20px;
            text-align: center;
            font-size: 45px;
            border: none;
            border-radius: 5px; /* Borda arredondada */
            box-shadow: 5px 10px 10px #377639;
            cursor: pointer; /* Ponteiro de "mãozinha" */
        }

        .custom-button:hover {
            background-color: #f1e6b7; /* Cor no hover */
            color: #cb5637; /* Muda cor do texto no hover */
            box-shadow: 5px 10px 10px #cb5637;
        }

        .button-wrapper {
            flex: 1 1 calc(50% - 20px); /* 50% da largura com espaçamento */
            display: flex;
            justify-content: center; /* Centraliza os botões */
        }
    </style>
""", unsafe_allow_html=True)

# Estrutura HTML para os botões em formato de grade 2x2
st.markdown("""
    <div class="button-container">
        <div class="button-wrapper">
            <button class="custom-button">👄</button>
        </div>
        <div class="button-wrapper">
            <button class="custom-button">🖐️</button>
        </div>
        <div class="button-wrapper">
            <button class="custom-button">👁️</button>
        </div>
        <div class="button-wrapper">
            <button class="custom-button">🦶</button>
        </div>
    </div>
""", unsafe_allow_html=True)




