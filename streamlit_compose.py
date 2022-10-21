import streamlit as st
from model_training_service import Code


pred = Code()


@st.cache
def process_prompt(completion_kwargs, topic):
    return pred.model_prediction(completion_kwargs=completion_kwargs, topic=topic)

def intro(api_key):
    # Setting up the Title
    st.title("Ekstraktor informacji medycznych z tekstu wspomagany przez GPT-3")

    st.write("")

    st.image("extr.jpeg", use_column_width=True, caption='.')




    st.write("---")

    st.write(f"""
    ### Disclaimer
 
    """)

    st.write('''
    You can read about these models in the links provided:
    
    GPT-3:
    https://en.wikipedia.org/wiki/GPT-3

    ''')



def func1(api_key):
    with st.form("form1"):
            st.subheader("1. Wyekstrahuj informacje z tekstu")

            opis_badania = st.text_input('Wprowadz opis badania: ',
                                      value='',
                                      help='')
            engine = st.radio('Engine',
                ('text-davinci-002', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))
            temp = st.slider('Temperature:', min_value=0., max_value=1., step=0.05)
            max_len = st.slider('Max tokens:', min_value=0, max_value=4096 if 'davinci' in engine else 2048,
                                step=8, value=64)
            if st.form_submit_button('Find the title'):
                completion_kwargs = {
                    "opis_badania": (opis_badania,),
                    "engine": engine,
                    "temperature": temp,
                    "max_tokens": max_len,
                    "api_key": api_key
                }
                st.write('**Wyekstrahowane informacje**')
                st.write(f"""---""")
                with st.spinner(text='In progress'):
                    report_text = process_prompt(completion_kwargs, "opis_badania")
                    st.markdown(report_text)
                    st.success('Done')
