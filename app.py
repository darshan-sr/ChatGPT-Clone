import streamlit as st
import openai

st.set_page_config(page_title='ChatGPT Clone') 

openai.api_key = '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'

hide_st_style = """
            <style>

            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.info('A ChatGPT clone along with an image generator Machine Learing model developed by Darshan  ')


tab1 , tab2 = st.tabs(['Generate Text','Generate Image'])

with tab1:
    model_engine = 'text-davinci-003'
    
    prompt = st.text_input('Enter your Promt')
    
    co1,co2 = st.columns(2)
    
    with co1:
    
      temp = st.slider('Set Temperature',min_value=0.0,max_value=1.0,step=0.1)
    
    with co2:
       st.write('')
    
    if st.button('Submit'):
        completion = openai.Completion.create(
            engine = model_engine,
            prompt = prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1,
        )
        
        response = completion.choices[0].text
        
        st.success(response)





with tab2:
    model_engine = 'image-alpha-001'
    prompt = st.text_input('Enter your Promt for image')
    
    if st.button('Generate Image'):
        response = openai.Image.create(
          prompt=prompt,
          n=1,
          size="512x512"
        )
        image_url = response['data'][0]['url']
        st.image(image_url, caption='Generated image')
        st.download_button(label='Download Image' ,data=image_url)