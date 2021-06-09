import streamlit as st
import streamlit.components.v1 as components
from PIL import Image


st.set_page_config(
    page_title="The Boys are not alright",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr {
            background-color:  #fdcf60  !important;
            color: white !important;
        }

        div[role="radiogroup"] > div {
            color:white !important;
            background-color: red !important;
        }

        .st-dd, .st-cb,  {
            color: white !important;
        }

        div[data-baseweb="select"] > div {
            background-color:  white  !important;
        }

        div[data-baseweb="select"] > div {
            background-color:  white  !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

image = Image.open('images/logo2.png')
st.sidebar.image(image, caption='', width=265)

st.sidebar.write('<span style="font-size:20px; color:#0c45a6"><b>THE BOYS ARE NOT ALRIGHT</b></span>',
                 unsafe_allow_html=True)

my_page = st.sidebar.radio('', ['Introduction', 'Datasets', 'Tools', 'Data Cleaning',
                                'EDA', 'Unsupervised Learning', 'Conclusion and Recommendations', 'Contributors'])

if my_page == 'Introduction':
    st.write('<span style="font-size:30px; color:#0c45a6"><b>THE BOYS ARE NOT ALRIGHT</b></span>',
             unsafe_allow_html=True)
    st.write('<span style="font-size:18px;">Reports consistently show that Filipino boys are dropping out of school.'
             ' </span><br><br>', unsafe_allow_html=True)

    col1, col2 = st.beta_columns([4, 5])
    col1.write('<span style="font-size:25px"><b>OBJECTIVE</b></span>', unsafe_allow_html=True)
    col1.write('<span style="font-size:23px"><b>Towards building a strategy to keep filipino boys in school</b></span>'
               '<br><br><span> "Be able to use cluster analysis in order to group schools with similar capacity metrics'
               ' to determine a capacity building strategy for each specific cluster"</span>', unsafe_allow_html=True)

    image = Image.open('images/context.png')
    col2.image(image, caption='', width=350)


elif my_page == 'Datasets':
    st.write('<span style="font-size:30px; color:#0c45a6"><b>DATASETS</b></span>',
             unsafe_allow_html=True)
    st.write('---------------------')

    st.write('A group of datasets from the Department of Education that is comprised of information from 2015 about the'
             ' public schools around the country including their general enrollment rates, number of SPED students and '
             'budgets allocations. ')
    st.write('<br>'
             '<table>'
             '<tr>'
             '<td><b>Dataset</b></td>'
             '<td><b>Description</b></td>'
             '<td><b>Source</b></td>'
             '</tr>'
             '<tr>'
             '<td>Enrollment</td>'
             '<td>Enrollment counts for males and females.</td>'
             '<td>Department of Education</td>'
             '</tr>'
             '<tr>'
             '<td>Rooms</td>'
             '<td>Room counts(per academic, nonstandard, unused).</td>'
             '<td>Department of Education</td>'
             '</tr>'
             '<tr>'
             '<td>MOOE</td>'
             '<td>MOOE allocated from the national budget</td>'
             '<td>Department of Education</td>'
             '</tr>'
             '<tr>'
             '<td>Teachers</td>'
             '<td>Teachers count (mobile, regular)</td>'
             '<td>Department of Education</td>'
             '</tr>'
             '<tr>'
             '<td>School locations</td>'
             '<td>Latitude-Longtitude pairs for various schools</td>'
             '<td>Department of Education</td>'
             '</tr>'
             '<tr>'
             '<td>Cities/Municipalities</td>'
             '<td>Latitude-Longtitude pairs for various schools</td>'
             '<td>Bangko Sentral ng Pilipinas, PH Open Data Portal</td>'
             '</tr>'
             '<tr>'
             '<td>PH Shapefile</td>'
             '<td>Shapefile for the entire country - to be used for mapping</td>'
             '<td>PhilGIS.org</td>'
             '</tr>'
             '<tr>'
             '<td>PH Provinces Shapefile</td>'
             '<td>Shapefile for the country divided into provinces</td>'
             '<td>PhilGIS.org</td>'
             '</tr>'
             '</table>', unsafe_allow_html=True)

elif my_page == 'Tools':
    st.write('<span style="font-size:30px; color:#0c45a6"><b>Tools: </b></span>', unsafe_allow_html=True)
    st.write('---------------------')

    col1, col2, col3 = st.beta_columns([2, 2, 2])

    col1.write('<br><br>', unsafe_allow_html=True)
    image = Image.open('images/python.png')
    col1.image(image, caption='', width=300)

    image = Image.open('images/anaconda.png')
    col2.image(image, caption='', width=300)

    image = Image.open('images/jupyter.png')
    col3.image(image, caption='', width=130)

    st.write('<br><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.beta_columns([3, 3, 3])

    image = Image.open('images/numpy.png')
    col1.image(image, caption='', width=300)

    image = Image.open('images/pandas.png')
    col2.image(image, caption='', width=300)

    image = Image.open('images/seaborn.png')
    col3.image(image, caption='', width=180)

    col1, col2, col3 = st.beta_columns([3, 3.5, 3])
    col1.write('<br><br>', unsafe_allow_html=True)
    image = Image.open('images/matplotlib.png')
    col1.image(image, caption='', width=300)

    col2.write('<br><br>', unsafe_allow_html=True)
    image = Image.open('images/scikit-learn.png')
    col2.image(image, caption='', width=300)

    col3.write('<br><br>', unsafe_allow_html=True)
    image = Image.open('images/heroku.png')
    col3.image(image, caption='', width=120)

    col1.write('<br><br>', unsafe_allow_html=True)
    image = Image.open('images/streamlit.png')
    col1.image(image, caption='', width=315)

    col2.write('<br><br><br><br>', unsafe_allow_html=True)
    image = Image.open('images/geopandas.png')
    col2.image(image, caption='', width=315)

    col3.write('<br><br>', unsafe_allow_html=True)
    image = Image.open('images/folium.png')
    col3.image(image, caption='', width=175)


elif my_page == 'Data Cleaning':
    st.write('<span style="font-size:30px; color:#0c45a6"><b>Data Cleaning: </b></span><br>', unsafe_allow_html=True)
    st.write('---------------------')

elif my_page == 'EDA':
    st.write('<span style="font-size:30px; color:#0c45a6"><b>Exploratory Data Analysis: </b></span><br>', unsafe_allow_html=True)
    st.write('---------------------')
    

elif my_page == 'Unsupervised Learning':
    st.title('Unsupervised Learning')
    
    st.header('K-Means Clustering')
    
    st.markdown('', unsafe_allow_html=False)
    
    st.header('Question 1')
    
    st.header('Question 2')
    
    st.header('Question 3')
    
    
elif my_page == 'Conclusion and Recommendations':
    col1, col2 = st.beta_columns([0.5, 4])

    image = Image.open('images/lightbulb.png')
    col1.image(image, caption='', width=50)

    col2.write('<span style="font-size:30px; color:#0c45a6"><b>Conclusion and Recommendations</b></span><br>',
               unsafe_allow_html=True)
    st.write('---------------------')

    col1, col2 = st.beta_columns([0.5, 4])

    col1.write('<span style="font-size:70px; color:#0c45a6"><b>1.</b></span>',
               unsafe_allow_html=True)

    col2.write('<span style="font-size:30px; color:#0c45a6"><b>NO ONE LEFT BEHIND!</b></span>',
               unsafe_allow_html=True)
    col2.write('Consider creating more programs for boys and girls to encourage finishing schools specifically for '
               'Cluster 1.')

    col1.write('<span style="font-size:70px; color:#0c45a6"><b>2.</b></span>',
               unsafe_allow_html=True)

    col2.write('<br><span style="font-size:30px; color:#0c45a6"><b>TAKE A LOOK BACK!</b></span>',
               unsafe_allow_html=True)
    col2.write('Review the school allocation especially those in Cluster 3.')

    col1.write('<span style="font-size:70px; color:#0c45a6"><b>3.</b></span>',
               unsafe_allow_html=True)

    col2.write('<br><span style="font-size:30px; color:#0c45a6"><b>WE CAN DO MORE!</b></span>',
               unsafe_allow_html=True)
    col2.write('Hierarchical Clustering')
    col2.write('Other datasets (e.g. for Dropout rates) ')
    

elif my_page == 'Contributors':
    col1, col2 = st.beta_columns([0.5, 4])

    image = Image.open('images/teamwork.png')
    col1.image(image, caption='', width=50)

    col2.write('<span style="font-size:30px; color:#0c45a6"><b>The Team</b></span><br>',
               unsafe_allow_html=True)
    st.write('---------------------')

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
        async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
        data-type="HORIZONTAL" data-vanity="cabenignos" data-version="v1">
        <a class="badge-base__link LI-simple-link" 
        href="https://ph.linkedin.com/in/cabenignos?trk=profile-badge"></a></div>''', height=350)

    with col2:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
        async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
        data-type="HORIZONTAL" data-vanity="christopher-louie-jay-gemida-02b083144" data-version="v1">
        <a class="badge-base__link LI-simple-link" 
        href="https://ph.linkedin.com/in/christopher-louie-jay-gemida-02b083144?trk=profile-badge"></a></div>''',
                              height=350)

    with col3:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js" 
        async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" 
        data-type="HORIZONTAL" data-vanity="fidel-ivan-racines-187477167" data-version="v1">
        <a class="badge-base__link LI-simple-link" 
        href="https://ph.linkedin.com/in/fidel-ivan-racines-187477167?trk=profile-badge"></a></div>'''
                              , height=350)

    with col1:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js"
                async defer type="text/javascript"></script>
                <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light"
                data-type="HORIZONTAL" data-vanity="jay-anthony-silverio-54ab37177" data-version="v1">
                <a class="badge-base__link LI-simple-link"
                href="https://ph.linkedin.com/in/jay-anthony-silverio-54ab37177?trk=profile-badge"></a></div>'''
                              , height=350)

    with col2:
        st.components.v1.html('''<script src="https://platform.linkedin.com/badges/js/profile.js"
                async defer type="text/javascript"></script>
                <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light"
                data-type="HORIZONTAL" data-vanity="matthew-antoine-tomas-32011773" data-version="v1">
                <a class="badge-base__link LI-simple-link"
                href="https://ph.linkedin.com/in/matthew-antoine-tomas-32011773?trk=profile-badge"></a></div>'''
                              , height=350)
        
    st.header('The Organization')
    st.markdown('Eskwelabs is an online data upskilling school for people and teams in Southeast Asia. Who gives '
                'access opportunities in the future of work through accessible data skills that are high in-demand as '
                'the amount of data in the world increases exponentially.', unsafe_allow_html=False)
    
    st.markdown('Our mission is to give access to engaging and future-relevant skills education is then crucial to help'
                ' people and teams thrive in that future. In Southeast Asia, where more than half of the population is '
                'under the age of 30, we believe data education can democratize access to meaningful careers for '
                'workers and sustainable competitiveness for companies.', unsafe_allow_html=False)
    
    st.markdown('At the same time, learning happens in all kinds of ways. Many learning environments, both in school '
                'and online, rely on lecture formats which are rarely engaging and effective for technical skills. '
                'Eskwelabs aims to enable participatory and active learning experiences so beyond acquiring in-demand '
                'skills, we can also rediscover the joy of learning and reinventing ourselves.',
                unsafe_allow_html=False)