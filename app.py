import streamlit as st

st.title("World Student Progression in Academic Performance from Primary School to High School")
st.markdown("## Thesis")
st.write("From primary school to the end of high school, are students getting more or less proficient in literacy and mathematics, in the Middle East, Central America, South America, Europe, Scandanavia, Oceania and Canada, comparatively?")

tab_1, tab_2, tab_3 = st.tabs(["World Graphs", "Regional Graphs", "Notes on Data"])

with tab_1:
    st.markdown("**World Student Mathematics Performance - Primary and High School**")
    st.image("world_math.png")
    st.markdown("**World Student Literacy Performance - Primary and High School**")
    st.image("world_literacy.png")

with tab_2:
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Scandanavia", "Europe", "Central America", "South America", "Middle East", "Oceania", "Canada"])
    
    with tab1:
        st.markdown("**Scandanavia Student Math Performance - Primary and High School**")
        st.image("scan_math.png")
        st.markdown("**Scandanavia Student Literacy Performance - Primary and High School**")
        st.image("scan_literacy.png")
    
    with tab2:
        st.markdown("**Europe Student Math Performance - Primary and High School**")
        st.image("eu_math.png")
        st.markdown("**Europe Student Literacy Performance - Primary and High School**")
        st.image("eu_literacy.png")

    with tab3:
        st.markdown("**Central America and Carribeans Student Math Performance - Primary and High School**")
        st.image("ca_math.png")
        st.markdown("**Central America and Carribeans Student Literacy Performance - Primary and High School**")
        st.image("ca_literacy.png")

    with tab4:
        st.markdown("**South America Student Math Performance - Primary and High School**")
        st.image("sa_math.png")
        st.markdown("**South America Student Literacy Performance - Primary and High School**")
        st.image("sa_literacy.png")

    with tab5:
        st.markdown("**Middle East Student Math Performance - Primary and High School**")
        st.image("me_math.png")
        st.markdown("**Middle East Student Literacy Performance - Primary and High School**")
        st.image("me_literacy.png")

    with tab6:
        st.markdown("**Oceania Student Math Performance - Primary and High School**")
        st.image("oc_math.png")
        st.markdown("**Oceania Student Literacy Performance - Primary and High School**")
        st.image("oc_literacy.png")

    with tab7:
        st.write("Canadian results to be seen in world graphs.")

with tab_3:
    st.markdown("### Data Source and Score Meaning")
    st.write("https://www.kaggle.com/datasets/nelgiriyewithana/world-educational-data")
    