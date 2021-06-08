import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


#image initializing
#banner = Image.open('images/banner.jpg')
#st.image(banner)

#Streamlit section
my_page = st.sidebar.radio('Sprint Navigation', ['Introduction', 'Methodology','Unsupervised Learning','Conclusion','Contributors'])

if my_page == 'Introduction':
    st.title("The boys are not alright")
    
    st.header("Context")
    
    st.markdown('Reports consistently show that Filipino boys are dropping out of school',unsafe_allow_html=False)
    
    st.header("Objective")
    
    st.markdown('Towards building a strategy to keep filipino boys in school',unsafe_allow_html=False)
    
    st.markdown('Be able to use cluster analysis in order to group schools with similar capacity metrics to determine a capacity building strategy for each specific cluster',unsafe_allow_html=False)

elif my_page == 'Methodology':
    st.title("Methodoly")
    
    st.header('Dataset')
    
    st.markdown('A group of datasets from the Department of Education that is comprised of information from 2015 about the public schools around the country including their general enrollment rates, number of SPED students and budgets allocations.',unsafe_allow_html=False)
    
    st.header('Tools')
    
    
elif my_page == 'Unsupervised Learning':
    st.title('Unsupervised Learning')
    
    st.header('K-Means Clustering')
    
    st.markdown('',unsafe_allow_html=False)
    
    st.header('Question 1')
    
    st.header('Question 2')
    
    st.header('Question 3')
    
    
elif my_page == 'Conclusion':
    st.header("Conclusion")
    
    st.markdown('We fetched the data from Spotify and cleaned it for it to be processed for ML modeling',unsafe_allow_html=False)
    
    
    st.header("Recommender")
    st.markdown('We used these features to create the Machine Learning Model to give recommendations on songs and artist collaborations. these features allow us to narrow down what the model woll be looking for in the data set.',unsafe_allow_html=False)
    
elif my_page == 'Contributors':

    st.header('The Team')
    
    st.markdown('We are proud to present our research',unsafe_allow_html=False)

    col1, col2, col3 = st.beta_columns(3)
    
    with col1:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="HORIZONTAL" data-vanity="fidel-ivan-racines-187477167" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/fidel-ivan-racines-187477167?trk=profile-badge">Fidel Ivan Racines</a></div>'''
                              ,height=350)
    
    with col2:
        st.components.v1.html('''
                              ''',height=350)
    
    with col3:
        st.components.v1.html('''
                              ''',height=350)

    col4, col5, col6 = st.beta_columns(3)

    with col4:
        st.components.v1.html('''
                              ''',height=350)
        
    with col5:
        st.components.v1.html('''
                              ''',height=350)
        
    with col6:
        st.components.v1.html('''
                              ''', height=350)
        
    st.header('The Mentor')
    
    st.markdown('Our mentor has helped and guided us through out the process of this study.',unsafe_allow_html=False)
    
    col7, col8, col9 = st.beta_columns(3)
    
    with col7:
        st.components.v1.html('''''', height=350)
        
    with col8:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
                              <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="patricknuguid" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://ph.linkedin.com/in/patricknuguid?trk=profile-badge%22%3EPatrick Nuguid</a></div>'''
                              ,height=350)
        
    with col9:
        st.components.v1.html('''''', height=350)
        
    st.header('The Organization')
    
    st.markdown('Eskwelabs is an online data upskilling school for people and teams in Southeast Asia. Who gives access opportunities in the future of work through accessible data skills that are high in-demand as the amount of data in the world increases exponentially.',unsafe_allow_html=False)
    
    st.markdown('Our mission is to give access to engaging and future-relevant skills education is then crucial to help people and teams thrive in that future. In Southeast Asia, where more than half of the population is under the age of 30, we believe data education can democratize access to meaningful careers for workers and sustainable competitiveness for companies.',unsafe_allow_html=False)
    
    st.markdown('At the same time, learning happens in all kinds of ways. Many learning environments, both in school and online, rely on lecture formats which are rarely engaging and effective for technical skills. Eskwelabs aims to enable participatory and active learning experiences so beyond acquiring in-demand skills, we can also rediscover the joy of learning and reinventing ourselves.',unsafe_allow_html=False)
