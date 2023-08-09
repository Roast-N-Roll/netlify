import streamlit as st
import pandas as pd
from API import list_sites, list_forms, list_form_submissions

# Page config
st.set_page_config(
    page_title="Roast n' ROll | Streamlit App",
    page_icon='assets/favicon.png',
    layout='wide')

def get_form_id_and_name(form_list):
    return pd.DataFrame(form_list)

def convert_submissiosn_to_df(submissions):
    df = pd.DataFrame(submissions)
    normalized_data = pd.json_normalize(df['data'])
    result_df = df[['number']].join(normalized_data)
    return result_df.set_index('number').drop(columns=['user_agent', 'referrer'])

sites = list_sites()

if sites:
    for site in sites:
        st.write(f"Site: {site['url']}")
        forms = list_forms(site['site_id'])

        df = get_form_id_and_name(forms)
        form_id = st.sidebar.selectbox('Select form:', df['id'], index=0, format_func=lambda x: df[df['id'] == x]['name'].iloc[0])

        if form_id:
            form_name = df[df['id'] == form_id]['name'].iloc[0]
            st.subheader(f"Form Name: {form_name}")

            submissions = convert_submissiosn_to_df(list_form_submissions(form_id))
            st.dataframe(submissions, use_container_width=True)
else:
    st.write("No sites found.")