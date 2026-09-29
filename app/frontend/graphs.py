import streamlit as st
from app.preprocess_data.load import load_data
from app.preprocess_data.preprocess import clean_text_data,semantic_meaning,Word_Vector
from app.preprocess_data.group_data import extract_game_features

from app.analyst import word_cloud,hist_tokens,reviews_length

import plotly.express as px

def words_meaning():
    data = load_data()
    data = clean_text_data(data)
    data = semantic_meaning(data)
    data2 = Word_Vector(data)

    return data

def main():
    data = words_meaning()

    col1,col2 = st.columns(2)

    #TOTAL
    results_word_cloud = word_cloud(data)

    with col1:
        st.pyplot(results_word_cloud['fig'])

    with col2:
        st.pyplot(results_word_cloud['fig2'])




    #BY DIV:
    results_word_cloud_game = word_cloud(data[data['classes'] == 'gameplay'])

    col_game1,col_game2 = st.columns(2)

    with col_game1:
        st.pyplot(results_word_cloud_game['fig'])

    with col_game2:
        st.pyplot(results_word_cloud_game['fig2'])

####
    results_word_cloud_gacha = word_cloud(data[data['classes'] == 'gacha'])
    
    col_gacha1,col_gacha2 = st.columns(2)

    with col_gacha1:
        st.pyplot(results_word_cloud_gacha['fig'])

    with col_gacha2:
        st.pyplot(results_word_cloud_gacha['fig2'])

####
    results_word_cloud_history = word_cloud(data[data['classes'] == 'history'])
    
    col_history1,col_history2 = st.columns(2)

    with col_history1:
        st.pyplot(results_word_cloud_history['fig'])

    with col_history1:
        st.pyplot(results_word_cloud_history['fig2'])

####
    results_word_cloud_events = word_cloud(data[data['classes'] == 'events'])
    
    col_events1,col_events2 = st.columns(2)

    with col_events1:
        st.pyplot(results_word_cloud_events['fig'])

    with col_events2:
        st.pyplot(results_word_cloud_events['fig2'])
####

    results_word_cloud_chars = word_cloud(data[data['classes'] == 'characters'])
    
    col_chars1,col_chars2 = st.columns(2)

    with col_chars1:
        st.pyplot(results_word_cloud_chars['fig'])

    with col_chars2:
        st.pyplot(results_word_cloud_chars['fig2'])

#####

    results_word_cloud_design = word_cloud(data[data['classes'] == 'design'])
    
    col_design1,col_design2 = st.columns(2)

    with col_design1:
        st.pyplot(results_word_cloud_design['fig'])

    with col_design2:
        st.pyplot(results_word_cloud_design['fig2'])




    #BY GAME 
    wuthering_waves_results = results_word_cloud[results_word_cloud['game'] == 'Wuthering Waves']
    wuthering_waves_col1,wuthering_waves_col2 = st.columns(2)

    with wuthering_waves_col1:
        st.pyplot(wuthering_waves_results['fig1'])

    with wuthering_waves_col2:
        st.pyplot(wuthering_waves_results['fig2'])

    genshin_impact_results = results_word_cloud[results_word_cloud['game'] == 'Genshin Impact']
    genshin_impact_col1,genshin_impact_col2 = st.columns(2)
    
    with genshin_impact_col1:
        st.pyplot(genshin_impact_results['fig1'])

    with genshin_impact_col2:
        st.pyplot(genshin_impact_results['fig2'])

    honkai_star_rail_results = results_word_cloud[results_word_cloud['game'] == 'Honkai Star Rail']
    honkai_star_rail_col1,honkai_star_rail_col2 = st.columns(2)

    with honkai_star_rail_col1:
        st.pyplot(honkai_star_rail_results['fig1'])

    with honkai_star_rail_col2:
        st.pyplot(honkai_star_rail_results['fig2'])


    zenless_zone_zero_results = results_word_cloud[results_word_cloud['game'] == 'Zenless Zone Zero']
    zenless_zone_zero_col1,zenless_zone_zero_col2 = st.columns(2)

    with zenless_zone_zero_col1:
        st.pyplot(zenless_zone_zero_results['fig1'])

    with zenless_zone_zero_col2:
        st.pyplot(zenless_zone_zero_results['fig2'])

    blue_archive_results = results_word_cloud[results_word_cloud['game'] == 'Blue Archive']
    blue_archive_col1,blue_archive_col2 = st.columns(2)

    with blue_archive_col1:
        st.pyplot(blue_archive_results['fig1'])

    with blue_archive_col2:
        st.pyplot(blue_archive_results['fig2'])


    st.divider()

    results_count_tokens = hist_tokens(data)
    col4,col5 = st.columns(2)

    with col4:
        st.pyplot(results_count_tokens['fig'])

    with col5:
        st.pyplot(results_count_tokens['fig2'])

    

    #BY GAME    
    wuthering_waves_results2 = results_count_tokens[results_count_tokens['game'] == 'Wuthering Waves']
    wuthering_waves2_col1,wuthering_waves2_col2 = st.columns(2)

    with wuthering_waves2_col1:
        st.pyplot(wuthering_waves_results2['fig1'])

    with wuthering_waves_col2:
        st.pyplot(wuthering_waves_results2['fig2'])

    genshin_impact_results2 = results_count_tokens[results_count_tokens['game'] == 'Genshin Impact']
    genshin_impact2_col1,genshin_impact2_col2 = st.columns(2)
    
    with genshin_impact2_col1:
        st.pyplot(genshin_impact_results2['fig1'])

    with genshin_impact2_col2:
        st.pyplot(genshin_impact_results2['fig2'])

    honkai_star_rail2_results = results_count_tokens[results_count_tokens['game'] == 'Honkai Star Rail']
    honkai_star_rail2_col1,honkai_star_rail2_col2 = st.columns(2)

    with honkai_star_rail2_col1:
        st.pyplot(honkai_star_rail2_results['fig1'])

    with honkai_star_rail2_col2:
        st.pyplot(honkai_star_rail2_results['fig2'])


    zenless_zone_zero2_results = results_count_tokens[results_count_tokens['game'] == 'Zenless Zone Zero']
    zenless_zone_zero2_col1,zenless_zone_zero2_col2 = st.columns(2)

    with zenless_zone_zero2_col1:
        st.pyplot(zenless_zone_zero2_results['fig1'])

    with zenless_zone_zero2_col2:
        st.pyplot(zenless_zone_zero2_results['fig2'])

    blue_archive2_results = results_count_tokens[results_count_tokens['game'] == 'Blue Archive']
    blue_archive2_col1,blue_archive2_col2 = st.columns(2)

    with blue_archive2_col1:
        st.pyplot(blue_archive2_results['fig1'])

    with blue_archive2_col2:
        st.pyplot(blue_archive2_results['fig2'])


    lengths = reviews_length(data)

    col_len1,col_len2 = st.columns(2)

    col_len1.metric('Word Mean Length ',lengths['word_length'].mean())
    col_len2.metirc('Sentence Mean Length ',lengths['sentence_length'].mean())

    box1 = px.box(lengths,x='game',y='word_length')
    box2 = px.box(lengths,x='game',y='sentence_length')

    st.plotly_chart(box1)
    st.plotly_chart(box2)


    df = features_weighted = Word_Vector(method='tfidf')
    st.dataframe(df.head(5))

    df_count = df.sum(axis=0)

    fig1 = px.histogram(df_count)

    st.plotly_chart(fig1)

if __name__ == 'main':
    main()
