import streamlit as st

st.title("World Student Progression in Academic Performance from Primary School to High School")

tab_1, tab_2, tab_3, tab_4, tab_5= st.tabs(["World Graphs", "Regional Graphs", "Notes on Data", "Thesis", "Findings Analysis"]) # creates primary tabs for each key set of information

with tab_1: # Contains images for world data
    st.markdown("**World Student Mathematics Performance - Primary and High School**")
    st.image("world_math.png")
    st.markdown("**World Student Literacy Performance - Primary and High School**")
    st.image("world_literacy.png")

with tab_2: # Contains individual regional data
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Scandanavia", "Europe", "Central America", "South America", "Middle East", "Oceania", "Canada"]) # creates taps for each central region
    
    with tab1: # Scandanavia
        st.markdown("**Scandanavia Student Math Performance - Primary and High School**")
        st.image("scan_math.png")
        st.markdown("**Scandanavia Student Literacy Performance - Primary and High School**")
        st.image("scan_literacy.png")
    
    with tab2: # Europe
        st.markdown("**Europe Student Math Performance - Primary and High School**")
        st.image("eu_math.png")
        st.markdown("**Europe Student Literacy Performance - Primary and High School**")
        st.image("eu_literacy.png")

    with tab3: # Central America
        st.markdown("**Central America and Carribeans Student Math Performance - Primary and High School**")
        st.image("ca_math.png")
        st.markdown("**Central America and Carribeans Student Literacy Performance - Primary and High School**")
        st.image("ca_literacy.png")

    with tab4: # South America
        st.markdown("**South America Student Math Performance - Primary and High School**")
        st.image("sa_math.png")
        st.markdown("**South America Student Literacy Performance - Primary and High School**")
        st.image("sa_literacy.png")

    with tab5:# Middle East
        st.markdown("**Middle East Student Math Performance - Primary and High School**")
        st.image("me_math.png")
        st.markdown("**Middle East Student Literacy Performance - Primary and High School**")
        st.image("me_literacy.png")

    with tab6: # Oceania
        st.markdown("**Oceania Student Math Performance - Primary and High School**")
        st.image("oc_math.png")
        st.markdown("**Oceania Student Literacy Performance - Primary and High School**")
        st.image("oc_literacy.png")

    with tab7:# Canadia
        st.write("Canadian results to be seen in world graphs.")

with tab_3: # Data source and explanations
    st.markdown("### Data Source")
    st.write("https://www.kaggle.com/datasets/nelgiriyewithana/world-educational-data")
    st.write("The 'World Educational Data' dataset contains student performance scores in mathematics and literacy from primary to high school across various regions. The scores are standardized, with higher scores indicating better performance. The dataset includes data from the Middle East, Central America, South America, Europe, Scandanavia, Oceania, and Canada.")
    st.write("The dataset measures a wide range of different data, however, for the purposes of this research task, it is the literary and mathematical proficiency scores that are of particular pertinence.")
    st.markdown("### Meaning of Scores")
    st.write("The scores in the dataset are standardized, and built on the basis of various UNESCO measurements, with the aim being a comparative representation of global academic performaance. ")
    st.write("The specific numeric value of the score is representative of the percentage of students who met the minimum benchmark of academic competence in each subject area. For instance, a score of 80 in mathematics indicates 80% of students meeting the minimum mathematical proficiency within that country. ")

with tab_4: # Thesis
    st.write("From primary school to the end of high school, are students getting more or less proficient in literacy and mathematics, in the Middle East, Central America, South America, Europe, Scandanavia, Oceania and Canada, comparatively?")

with tab_5: # Findings analysis
    st.write("The research carried out in this project has served to indicate a few general trends that warrant discussion across, seperately, literacy and mathematics. Throughout the world, in literacy, there is a common downard trend from mid-primary school to the end of high school, with a mean decline of 22.65% across all regions. Although the drop is more substantial in developing countries, the trend is markedly visible all across the globe and, given the roughly even distribution of rich and poor countries, the average decline seems adequetly descriptive of the general trend.")
    st.write("In mathematics, the most pronounced pattern is not one all-encompassing and general trend, but rather the substantial distinction between the developed and developing countries. While in the developed regions, such as Europe and Scandanavia, but also the given Middle Eastern countries, mathematical proficiency remains fairly steady throughout schooling (mostly around 80-90%, but closer to 30-40% for the Middle East), the undeveloped regions of Central and South America (including the Carribeans) undergo a severe drop, between mid-primary school and the end of high school, in excess of 50%, on average.")
    st.write("Beyond the key general trends to be extracted, there remain some specific regional anomalies worthy of note. Particularly, while it is to be seen that most European countries have neglibible or minimally improved change in academic performance from early primary school to the end of high school, France's scores are shown to improve by a margin of roughly 30%. Nevertheless, outstanding instances such as these are seldom, and it is visible that each individual region holds within it a common and generally observable trend.")
