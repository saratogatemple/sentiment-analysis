import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.markdown("""
## Understanding Social Media Sentiments  

In a world where digital footprints echo the sentiments of society, comprehending the collective emotional undertones of social media has never been more imperative. 
Every tweet, status update, or photo shared holds a mirror to the ever-evolving public sentiment, capturing the zeitgeist of the current era. 

Our app performs nuanced sentiment analysis on social media postings. By decoding the emotional texture embedded within digital interactions, it unveils the larger narrative that often goes unnoticed in the cacophony of online chatter.
By providing a nuanced understanding of social sentiments, it encourages a more thoughtful engagement with digital communities. 
            
In a time where polarization is rampant, harnessing the ability to analyze and understand the emotional undertones of social media discourse is a step towards fostering a more inclusive and empathetic digital landscape.
Through our app, we invite you to delve into the heart of digital society, to listen, understand, and engage with the myriad voices that shape our world today.
             """)

if st.button("Analyze social media posts"):
            switch_page("Sentiment Analysis")


