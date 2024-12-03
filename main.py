import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.express as px

# Set theme colors for Carhartt branding
primary_color = "#A67B5B"  # Carhartt tan
secondary_color = "#382D1E"  # Carhartt brown
carhartt_yellow = "#FFD700"  # Carhartt yellow

# Configure Streamlit page
st.set_page_config(
    page_title="Carhartt Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Configuring header with logo on the top left
t1, t2 = st.columns((0.1, 0.8))
t1.image("index_1.png", width=200)  # Replace 'index_1.png' with your logo file path
t2.title("Getting to Know Carhartt")
t2.markdown(
    "To get to known Carhartt and explore company insights, while demonstrating my backgorund in Data Science with AI/ML and data visualization, I built the below interactive dashboard!"
)

# Overview metrics
m1, m2, m3, m4, m5 = st.columns((1, 1, 1, 1, 1))
m1.write("")
m2.metric(label="Founded", value="1889", help="Carhartt was established in Dearborn, Michigan.")
m3.metric(label="Headquarters", value="Dearborn, MI", help="Carhartt is still based in its founding city.")
m4.metric(label="Industry", value="Workwear", help="Focuses on outdoor and industrial clothing.")
m5.write("")

# Tabs for additional insights
tab1, tab2, tab3, tab4 = st.tabs(["Q&A Tool", "About Carhartt", "Product Insights", "Industry Trends"])

# Tab 1: Q&A Tool
with tab1:
    st.subheader("Carhartt Q&A Tool")
    st.write("Ask a question about Carhartt and get an answer based on the preloaded context.")

    # Expanded Context
    context = """
    Carhartt, established in 1889 in Dearborn, Michigan, is a renowned American workwear brand. Known for its rugged design, the company produces high-quality jackets, overalls, work pants, shirts, and accessories tailored for outdoor and industrial use. Carhartt prioritizes durability, functionality, and innovation, using materials like cotton duck and canvas. 

    Carhartt emphasizes sustainability through initiatives such as:
    - The use of recycled materials and low-carbon processes.
    - Renewable energy sourcing and waste reduction efforts.
    - A 'Made in the USA' program supporting local manufacturing and jobs.

    The brand serves a diverse customer base, including construction workers, outdoor enthusiasts, and farmers, and has a global presence.
    """

    # User question input
    user_question = st.text_input("Enter your question about Carhartt:")
    if user_question:
        qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
        answer = qa_pipeline(question=user_question, context=context)
        st.write(f"**Answer:** {answer['answer']}")

# Tab 2: About Carhartt
with tab2:
    st.subheader("About Carhartt")
    st.write("""
    **Mission**: To provide durable, high-quality workwear for hardworking individuals.  
    Carhartt has been a leader in the workwear industry for over a century, recognized for its commitment to rugged designs and sustainability.
    """)
    st.subheader("Notable Initiatives")
    st.write("""
    - **Made in the USA Program**: Promotes American-made products.
    - **Sustainability Efforts**: Includes renewable energy sourcing, low-carbon materials, and recycled fibers.
    """)

# Tab 3: Product Insights
with tab3:
    st.subheader("Product Insights")

    # Mock data for product categories
    data = {
        "Category": ["Jackets", "Pants", "Overalls", "Shirts", "Accessories"],
        "Popularity (%)": [30, 25, 20, 15, 10]
    }
    df = pd.DataFrame(data)

    # Bar chart for product popularity using Plotly
    st.write("### Product Popularity")
    fig = px.bar(
        df,
        x="Category",
        y="Popularity (%)",
        color="Category",
        title="Carhartt Product Popularity",
        color_discrete_sequence=[primary_color]
    )
    fig.update_layout(
        title_font_color=primary_color,
        plot_bgcolor="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Materials Used**:  
    Carhartt emphasizes durable materials like cotton duck, canvas, and denim. Sustainability efforts have introduced recycled fibers into their lineup.
    """)

# Tab 4: Industry Trends
with tab4:
    st.subheader("Industry Trends")
    st.write("""
    The global workwear market continues to grow, driven by increased focus on safety and functionality.  
    **Key Competitors**:  
    - Dickies  
    - Wrangler  
    - Red Kap  
    """)

    # Mock data for market growth
    growth_data = pd.DataFrame({
        "Year": [2018, 2019, 2020, 2021, 2022],
        "Market Size (in Billion USD)": [10, 11, 13, 15, 16]
    })

    # Line chart for market growth using Plotly
    st.write("### Workwear Market Growth")
    fig_growth = px.line(
        growth_data,
        x="Year",
        y="Market Size (in Billion USD)",
        title="Workwear Market Growth",
        markers=True,
        line_shape="spline"
    )
    fig_growth.update_traces(line_color=primary_color)
    fig_growth.update_layout(
        title_font_color=primary_color,
        plot_bgcolor="white",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    st.plotly_chart(fig_growth, use_container_width=True)
