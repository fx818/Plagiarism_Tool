import streamlit as st
from plagiarism_tool import tool


section = st.sidebar.radio('Explore Different Tools from here :' , ['Plagiarism Tool','Sentiment Analysis','Playing 11'])
if section=='Plagiarism Tool':
    st.header("We are into Plagiarism Tool")
       
    x = st.text_input('Enter sentence 1 here', placeholder='Sample Text')
    y = st.text_input('Enter sentence 2 here', placeholder='sample text')
    # x = 'Sample Text'
    # y = 'sample text'
    if x=='Sample Text':
        pass
    else:
        pass

    if y=='sample text':
        pass
    else:
        pass

    # x = st.text_input('Enter sentence 1 here', placeholder='Sample Text')
    # y = st.text_input('Enter sentence 2 here', placeholder='sample text')
    st.write(x)
    st.write(y)
    # x = x.split()
    # y = y.split()
    # st.write(x)
    # st.write(y)

    z = tool(x,y)
    st.write(f'The two given sentences are {z*100:.2f}% similar')
        
    
    
    
elif section=='Sentiment Analysis':
    st.header('We are into Sentiment Analysis Tool')
    st.write('We are currently working on this project')
elif section=='Playing 11':
    st.header('We are into Predicting Playing 11')
    st.write('We are currently working on this project')
 