import streamlit as st
import pandas as pd
from API import list_sites, list_forms, list_form_submissions

# Page config
st.set_page_config(
    page_title="Roast n' ROll | Streamlit App",
    page_icon='assets/favicon.png',
    layout='wide')

def get_form_id_and_name(form_list):
    form_data = []
    for form in form_list:
        form_id = form["id"]
        form_name = form["name"]
        form_data.append({"form_id": form_id, "form_name": form_name})
    return pd.DataFrame(form_data)

def convert_submissiosn_to_df(submissions):
    df = pd.DataFrame(submissions)
    normalized_data = pd.json_normalize(df['data'])
    result_df = df[['number']].join(normalized_data)
    return result_df.set_index('number').drop(columns=['user_agent', 'referrer'])

sites = list_sites()

if sites:
    for site in sites:
        st.write(f"Site Name: {site['name']}, URL: {site['url']}")
        forms = list_forms(site['site_id'])

        df = get_form_id_and_name(forms)
        form_id = st.sidebar.selectbox('Select form:', df)

        submissions = convert_submissiosn_to_df(list_form_submissions(form_id))
        st.dataframe(submissions, use_container_width=True)
else:
    st.write("No sites found.")