import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# ========== Magic Branding CSS ==========
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&display=swap');

* {{
    font-family: 'Space Grotesk', sans-serif;
}}

/* Magic Gradient Effects */
.magic-pulse {{
    animation: gradient-pulse 8s ease infinite;
}}

@keyframes gradient-pulse {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

/* Centered Hero Section */
.hero {{
    text-align: center;
    padding: 3rem 0 2rem 0;
    background: linear-gradient(135deg, #4F46E540 0%, #06D6A020 100%);
    border-radius: 2rem;
    margin: 1rem 0;
    border: 1px solid #4F46E510;
}}

.feature-icon {{
    font-size: 2.5rem !important;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, #4F46E5 0%, #06D6A0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

/* Enhanced Upload Zone */
[data-testid="stFileUploader"] {{
    border: 3px dashed #4F46E5 !important;
    border-radius: 20px !important;
    padding: 5rem !important;
    background: rgba(79, 70, 229, 0.05) !important;
    margin: 2rem 0 !important;
    transition: all 0.3s ease !important;
}}

[data-testid="stFileUploader"]:hover {{
    background: rgba(79, 70, 229, 0.08) !important;
    transform: scale(1.005);
}}

/* Analysis Cards */
.analysis-card {{
    padding: 1.5rem;
    border-radius: 1rem;
    background: linear-gradient(135deg, #4F46E510 0%, #06D6A008 100%);
    border: 1px solid #4F46E510;
    margin: 1rem 0;
}}

.data-preview {{
    border: 1px solid #4F46E520 !important;
    border-radius: 1rem !important;
    padding: 1rem !important;
}}

/* Enhanced Table Styles */
[data-testid="stDataFrame"] {{
    border: 1px solid #4F46E520 !important;
    border-radius: 1rem !important;
    box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.1);
}}

.stDataFrame th {{
    background: linear-gradient(135deg, #4F46E5 0%, #06D6A0 100%) !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
}}

.stDataFrame tr:nth-child(even) {{
    background-color: #f8f9fa;
}}

.stDataFrame tr:hover {{
    background-color: #4F46E508 !important;
}}

.stDataFrame td, .stDataFrame th {{
    padding: 12px 15px !important;
}}

.stDataFrame td {{
    text-align: right !important;
}}

.stDataFrame td:first-child {{
    text-align: left !important;
    font-weight: 500 !important;
}}

/* Visualization Additions */
.viz-card {{
    padding: 1.5rem;
    border-radius: 1rem;
    background: linear-gradient(135deg, #4F46E508 0%, #06D6A005 100%);
    border: 1px solid #4F46E515;
    margin: 1rem 0;
    transition: all 0.3s ease;
}}

.viz-card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 4px 15px rgba(79, 70, 229, 0.1);
}}

.viz-controls {{
    background: rgba(79, 70, 229, 0.03) !important;
    border-radius: 15px !important;
    padding: 1rem !important;
    border: 1px solid #4F46E510 !important;
}}

.chart-type-card {{
    padding: 1rem;
    border-radius: 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    border: 2px solid #4F46E510;
    background: white;
}}

.chart-type-card:hover {{
    border-color: #4F46E5;
    background: #f8f9ff;
}}

.chart-type-card.active {{
    border-color: #4F46E5;
    background: linear-gradient(135deg, #4F46E510 0%, #06D6A008 100%);
}}

.color-picker {{
    width: 100% !important;
    height: 40px !important;
    border-radius: 8px !important;
    border: 2px solid #4F46E520 !important;
}}
</style>
""", unsafe_allow_html=True)

# ========== Create Tabs ==========
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🔍 Intelligent Analysis", "🧹 Automated Sanitization", "✨ Dynamic Viz"])


# ========== Home Tab ==========
with tab1:
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div class="hero">'
                        '<h1 style="font-size: 3.5rem; margin: 0;">MagicGrid</h1>'
                        '<p style="font-size: 1.3rem; color: #4F46E5; margin-top: 0.5rem;">"Drop your CSV – we’ll handle the magic"</p>'
                        '</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class="hero magic-pulse" style="background-size: 400% 400%;">
            <h3 style="margin-bottom: 2rem;">✨ Advanced Data Processing Features</h3>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
                <div style="padding: 1.5rem; border-radius: 1rem; background: rgba(255,255,255,0.1);">
                    <div class="feature-icon">🧹</div>
                    <h4>Automated Sanitization</h4>
                    <p style="font-size: 0.9rem;">One-click data cleaning & normalization</p>
                </div>
                <div style="padding: 1.5rem; border-radius: 1rem; background: rgba(255,255,255,0.1);">
                    <div class="feature-icon">🔍</div>
                    <h4>Intelligent Analysis</h4>
                    <p style="font-size: 0.9rem;">Quick Statistical Summary</p>
                </div>
                <div style="padding: 1.5rem; border-radius: 1rem; background: rgba(255,255,255,0.1);">
                    <div class="feature-icon">📈</div>
                    <h4>Dynamic Visualization</h4>
                    <p style="font-size: 0.9rem;">Auto-generated business insights</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with st.container():
        st.divider()
        upload_col, sample_col = st.columns([3, 1])
        
        with upload_col:
            uploaded_file = st.file_uploader(
                " ",
                type=["csv"],
                label_visibility="collapsed",
                help="Drag & drop your CSV file or click to browse",
            )
            if uploaded_file:
                st.session_state.df = pd.read_csv(uploaded_file)
        
        with sample_col:
            if st.button("🚀 Launch Demo", use_container_width=True, type="primary"):
                sample_data = pd.DataFrame({
                    'Date': pd.date_range(start='2023-01-01', periods=5),
                    'Revenue': [15000, 22000, 18000, 31000, 28000],
                    'Category': ['Electronics', 'Fashion', 'Home', 'Beauty', 'Sports']
                })
                st.session_state.df = sample_data
                st.toast("Demo dataset loaded successfully!", icon="✅")

# ========== Intelligent Analysis Tab ==========
with tab2:
    if 'df' not in st.session_state:
        st.warning("⚠️ Please upload data or use demo dataset from Home tab")
        st.stop()
    
    with st.container():
        st.markdown('<div class="hero">'
                    '<h2 style="margin: 0;">🔍 Intelligent Analysis</h2>'
                    '<p style="color: #4F46E5; margin-top: 0.5rem;">Data Insights Engine</p>'
                    '</div>', unsafe_allow_html=True)
        
        st.divider()
        
        # Data Health Report
        with st.container():
            st.subheader("📊 Dataset Health Report")
            cols = st.columns(4)
            metrics = [
                ("📏 Total Rows", st.session_state.df.shape[0], "#4F46E5"),
                ("📐 Total Columns", st.session_state.df.shape[1], "#06D6A0"),
                ("⚠️ Missing Values", st.session_state.df.isnull().sum().sum(), "#EF476F"),
                ("🔄 Duplicate Rows", st.session_state.df.duplicated().sum(), "#FFD166")
            ]
            
            for col, (title, value, color) in zip(cols, metrics):
                with col:
                    st.markdown(f"""
                    <div class="analysis-card" style="border-left: 4px solid {color};">
                        <div style="font-size: 0.9rem; color: {color}; margin-bottom: 0.5rem;">{title}</div>
                        <div style="font-size: 1.8rem; font-weight: 700;">{value}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Data Preview
        with st.container():
            st.subheader("🔍 Data Preview")
            st.markdown("""
            <div class="data-preview">
                <div style="font-size: 0.9rem; color: #4F46E5; margin-bottom: 1rem;">
                    First 10 rows of your dataset
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.dataframe(st.session_state.df.head(10), 
                         use_container_width=True,
                         height=300)
        
        # Data Insights Section
        with st.container():
            st.subheader("🧬 Data Insights")
            col_struct, col_desc = st.columns([0.65, 0.35], gap="large")
            
            with col_struct:
                st.markdown("#### 📋 Data Structure")
                dtype_df = pd.DataFrame({
                    'Column': st.session_state.df.columns,
                    'Type': st.session_state.df.dtypes.astype(str),
                    'Unique': st.session_state.df.nunique(),
                    'Missing %': (st.session_state.df.isnull().mean() * 100).round(2)
                })
                st.dataframe(
                    dtype_df.style.format({'Missing %': '{:.2f}%'}),
                    use_container_width=True,
                    height=400
                )

            with col_desc:
                st.markdown("#### 📐 Statistical Summary")
                desc_df = st.session_state.df.describe().reset_index().rename(columns={'index': 'Statistic'})
                st.dataframe(
                    desc_df.style.format("{:.2f}", subset=desc_df.columns[1:]),
                    use_container_width=True,
                    height=400,
                    column_config={
                        "Statistic": st.column_config.TextColumn(
                            "Metric",
                            help="Statistical measure"
                        )
                    }
                )

# ========== Automated Sanitization Tab ==========
with tab3:
    if 'df' not in st.session_state:
        st.warning("⚠️ Please upload data or use demo dataset from Home tab")
        st.stop()
    
    df = st.session_state.df.copy()
    
    with st.container():
        st.markdown('<div class="hero">'
                    '<h2 style="margin: 0;">🧹 Data Sanitization Studio</h2>'
                    '<p style="color: #4F46E5; margin-top: 0.5rem;">Professional Data Cleaning Toolkit</p>'
                    '</div>', unsafe_allow_html=True)
        
        st.divider()

        # ===== Custom Styling =====
        st.markdown("""
        <style>
            .cylindrical-pill {
                background: linear-gradient(135deg, #4F46E515 0%, #06D6A010 100%);
                border-radius: 25px;
                padding: 12px 25px;
                margin: 15px 0;
                border-left: 4px solid #4F46E5;
                border-right: 2px solid #4F46E510;
                box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.05);
            }
            .magic-btn {
                background: linear-gradient(135deg, #4F46E5 0%, #06D6A0 100%);
                color: white !important;
                border: none !important;
                padding: 12px 30px !important;
                border-radius: 12px !important;
                font-weight: 700 !important;
                transition: all 0.3s ease !important;
            }
            .magic-btn:hover {
                transform: scale(1.02);
                box-shadow: 0 5px 20px rgba(79, 70, 229, 0.3);
            }
            .st-emotion-cache-1p1nwyz {
                border: 2px solid #4F46E520 !important;
                border-radius: 15px !important;
            }
        </style>
        """, unsafe_allow_html=True)

        # ===== Missing Values =====
        with st.expander("🧼 Missing Values Treatment", expanded=True):
            st.markdown('<div class="cylindrical-pill">🚨 Missing Values Manager</div>', unsafe_allow_html=True)
            
            cols = st.columns([2, 3])
            with cols[0]:
                missing = df.isnull().sum()
                st.markdown("##### 🔍 Missing Values Report")
                st.dataframe(pd.DataFrame({
                    'Column': missing.index,
                    'Missing Count': missing.values,
                    '% Missing': (missing/len(df)*100)
                }).style.format({'% Missing': '{:.2f}%'}),
                height=250)

            with cols[1]:
                st.markdown("##### ⚙️ Treatment Engine")
                col1, col2 = st.columns(2)
                with col1:
                    column = st.selectbox("Select Column", df.columns[df.isnull().any()])
                    method = st.selectbox("Method", ["Mean", "Median", "Mode", "Custom", "Drop"])
                with col2:
                    if method == "Custom":
                        custom_val = st.text_input("Custom Value")
                    else:
                        st.empty()

                if st.button("Apply Treatment", key="missing_btn"):
                    try:
                        if method == "Mean": df[column].fillna(df[column].mean(), inplace=True)
                        elif method == "Median": df[column].fillna(df[column].median(), inplace=True)
                        elif method == "Mode": df[column].fillna(df[column].mode()[0], inplace=True)
                        elif method == "Custom": df[column].fillna(custom_val, inplace=True)
                        elif method == "Drop": df.dropna(subset=[column], inplace=True)
                        
                        st.session_state.df = df
                        st.success("✅ Treatment applied successfully!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

        # ===== Duplicates Handling =====
        with st.expander("🔄 Duplicates Management", expanded=True):
            st.markdown('<div class="cylindrical-pill">♻️ Duplicates Controller</div>', unsafe_allow_html=True)
            
            dup_count = df.duplicated().sum()
            cols = st.columns([2, 3])
            with cols[0]:
                st.markdown(f"##### 🔍 Duplicates Found: {dup_count}")
                if st.button("🔄 Remove All Duplicates", key="dup_remove"):
                    initial = len(df)
                    df.drop_duplicates(inplace=True)
                    st.session_state.df = df
                    st.success(f"✅ Removed {initial - len(df)} duplicates!")

            with cols[1]:
                st.markdown("##### 📊 Duplicates Preview")
                st.dataframe(df[df.duplicated(keep=False)].head(5), height=200)

        # ===== Data Type Conversion =====
        with st.expander("🔧 Data Type Transformer", expanded=True):
            st.markdown('<div class="cylindrical-pill">🔄 Type Conversion Gateway</div>', unsafe_allow_html=True)
            
            cols = st.columns(2)
            with cols[0]:
                column = st.selectbox("Select Column", df.columns)
                new_type = st.selectbox("New Data Type", 
                    ["String", "Integer", "Float", "DateTime", "Category"])
            
            with cols[1]:
                st.markdown("##### Current Schema")
                current_type = str(df[column].dtype)
                st.markdown(f"`{current_type}` → `{new_type.lower()}`")
                
                if st.button("Transform Column", key="dtype_btn"):
                    try:
                        type_map = {
                            "String": "object",
                            "Integer": "int",
                            "Float": "float",
                            "DateTime": "datetime64[ns]",
                            "Category": "category"
                        }
                        df[column] = df[column].astype(type_map[new_type])
                        st.session_state.df = df
                        st.success("✅ Transformation complete!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

        # ===== Column/Row Operations =====
        with st.expander("✂️ Data Pruner", expanded=True):
            st.markdown('<div class="cylindrical-pill">🌿 Precision Pruning Tool</div>', unsafe_allow_html=True)
            
            tab1, tab2 = st.tabs(["Columns", "Rows"])
            with tab1:
                cols_to_drop = st.multiselect("Select columns to prune", df.columns)
                if st.button("Drop Columns", key="col_drop"):
                    df.drop(columns=cols_to_drop, inplace=True)
                    st.session_state.df = df
                    st.success(f"✅ Removed {len(cols_to_drop)} columns")

            with tab2:
                rows_to_drop = st.text_input("Enter row indices (comma-separated)")
                if st.button("Drop Rows", key="row_drop"):
                    try:
                        indices = [int(i.strip()) for i in rows_to_drop.split(",")]
                        df.drop(index=indices, inplace=True)
                        st.session_state.df = df
                        st.success(f"✅ Removed {len(indices)} rows")
                    except:
                        st.error("⚠️ Invalid input format")

        # ===== Outlier Handling =====
        with st.expander("📏 Outlier Engineer", expanded=True):
            st.markdown('<div class="cylindrical-pill">🔎 Anomaly Detection System</div>', unsafe_allow_html=True)
            
            numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
            cols = st.columns(2)
            with cols[0]:
                column = st.selectbox("Select Numeric Column", numeric_cols)
                method = st.selectbox("Treatment Method", ["IQR", "Z-Score", "Winsorize"])
            
            with cols[1]:
                st.markdown(f"##### {column} Distribution")
                st.line_chart(df[column])

            if st.button("Treat Outliers", key="outlier_btn"):
                try:
                    if method == "IQR":
                        Q1 = df[column].quantile(0.25)
                        Q3 = df[column].quantile(0.75)
                        IQR = Q3 - Q1
                        df[column] = np.clip(df[column], Q1-1.5*IQR, Q3+1.5*IQR)
                    elif method == "Z-Score":
                        z = np.abs((df[column] - df[column].mean())/df[column].std())
                        df[column] = np.where(z > 3, df[column].median(), df[column])
                    st.session_state.df = df
                    st.success("✅ Outliers treated successfully!")
                except Exception as e:
                    st.error(f"Error: {str(e)}")

        # ===== Derived Columns =====
        with st.expander("🧪 Column Alchemist", expanded=True):
            st.markdown('<div class="cylindrical-pill">✨ Formula Wizard</div>', unsafe_allow_html=True)
            
            new_col = st.text_input("New Column Name")
            formula = st.text_area("Formula (e.g., Revenue - Cost)", height=100)
            
            if st.button("Create Column", key="derive_btn"):
                try:
                    df[new_col] = df.eval(formula)
                    st.session_state.df = df
                    st.success(f"✅ Created new column: {new_col}")
                except Exception as e:
                    st.error(f"Formula Error: {str(e)}")

        # ===== Export Section =====
        st.divider()
        with st.container():
            cols = st.columns([1, 2, 1])
            with cols[1]:
                st.markdown('<div class="cylindrical-pill" style="text-align:center;">🚀 Export Sanctum</div>', 
                          unsafe_allow_html=True)
                
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="✨ Export Clean Dataset",
                    data=csv,
                    file_name='magic_cleaned_data.csv',
                    mime='text/csv',
                    use_container_width=True,
                    key='export_btn',
                    help="Download your pristine dataset",
                    args={"class": "magic-btn"}
                )
                
                st.markdown("""
                <div style="text-align:center; margin-top:1rem; color:#4F46E5;">
                    🎉 Your data is now magic-certified! 🎉
                </div>
                """, unsafe_allow_html=True)
# ========== Dynamic Visualization Tab ==========
# ========== Dynamic Visualization Tab ==========
# ========== Dynamic Visualization Tab ==========
# ========== Dynamic Visualization Tab (Updated) ==========
# ========== Dynamic Visualization Tab (Final Robust Version) ==========
with tab4:
    if 'df' not in st.session_state:
        st.warning("⚠️ Please upload data or use demo dataset from Home tab")
        st.stop()
    
    df = st.session_state.df.copy()
    
    # Custom CSS for better appearance
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(90deg, #f6f8ff 0%, #e6eaff 100%);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    .control-panel {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4F46E5;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        margin-bottom: 1rem;
    }
    .chart-container {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }
    .analysis-card {
        background: #f8faff;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #06D6A0;
        margin-top: 1rem;
    }
    .export-button {
        background-color: #4F46E5;
        color: white;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        cursor: pointer;
        text-align: center;
        transition: all 0.3s;
    }
    .export-button:hover {
        background-color: #3730a3;
        transform: translateY(-2px);
    }
    div[data-baseweb="select"] > div {
        border-radius: 6px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="hero">'
                    '<h2 style="margin: 0;">✨ Dynamic Visualization Studio</h2>'
                    '<p style="color: #4F46E5; margin-top: 0.5rem;">AI-Powered Visual Insights</p>'
                    '</div>', unsafe_allow_html=True)
        
        
        # ===== Visualization Controls =====
        with st.container():
            cols = st.columns([1, 3], gap="large")
            
            # Control Panel
            with cols[0]:
                with st.container():
                    st.markdown('<div class="control-panel"><h4 style="margin-top: 0;">⚙️ Chart Configurator</h4></div>', unsafe_allow_html=True)
                    with st.expander("Main Configuration", expanded=True):
                        # Get available numeric and categorical columns
                        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
                        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
                        date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
                        all_cols = df.columns.tolist()
                        
                        chart_type = st.selectbox(
                            "Chart Type",
                            ["Line", "Bar", "Scatter", "Area", "Bubble", 
                             "Box", "Violin", "Heatmap", "Radar", "Pie", "Sunburst"],
                            index=0,
                            key="chart_type"
                        )
                        
                        # Help text for charts
                        chart_help = {
                            "Line": "Good for time series and trends over a continuous variable",
                            "Bar": "Compare values across categories",
                            "Scatter": "Investigate relationship between two variables",
                            "Area": "Similar to line chart but with filled area below",
                            "Bubble": "Like scatter but with third dimension as bubble size",
                            "Box": "Show distribution statistics and outliers",
                            "Violin": "Show full distribution with probability density",
                            "Heatmap": "Visualize matrix data with color intensity",
                            "Radar": "Compare multiple variables in a circular layout",
                            "Pie": "Show parts of a whole (use sparingly)",
                            "Sunburst": "Show hierarchical data with nested rings"
                        }
                        
                        st.caption(f"💡 {chart_help.get(chart_type, '')}")
                        
                        # Dynamic axis options based on chart type
                        if chart_type in ["Heatmap", "Pie", "Sunburst"]:
                            x_options = categorical_cols if categorical_cols else all_cols
                            x_axis = st.selectbox(
                                "X Axis / Primary Dimension", 
                                x_options,
                                index=min(0, len(x_options)-1),
                                key="x_axis"
                            )
                            y_axis = None
                            if chart_type == "Heatmap":
                                y_options = categorical_cols if categorical_cols else all_cols
                                y_axis = st.selectbox(
                                    "Y Axis / Secondary Dimension", 
                                    y_options,
                                    index=min(1, len(y_options)-1) if len(y_options) > 1 else 0,
                                    key="y_axis"
                                )
                        else:
                            x_priority = date_cols + categorical_cols if date_cols else categorical_cols
                            x_options = x_priority if x_priority else all_cols
                            x_axis = st.selectbox(
                                "X Axis", 
                                x_options,
                                index=min(0, len(x_options)-1),
                                key="x_axis"
                            )
                            y_axis = st.selectbox(
                                "Y Axis", 
                                numeric_cols if numeric_cols else all_cols,
                                index=min(0, len(numeric_cols)-1),
                                key="y_axis"
                            )
                        
                        agg_func = st.selectbox(
                            "Aggregation",
                            ["None", "sum", "mean", "median", "count", "min", "max"],
                            index=1,
                            key="agg_func"
                        )
                        
                        group_by = st.multiselect(
                            "Group By",
                            [col for col in df.columns if col != x_axis],
                            max_selections=3,
                            key="group_by"
                        )
                        
                        color_options = ["None"] + categorical_cols
                        color_by = st.selectbox(
                            "Color Encoding",
                            color_options,
                            index=0,
                            key="color_by"
                        )
                        
                        # More intuitive color palette selection
                        palette_options = {
                            "Default Blue": "#4F46E5",
                            "Business Green": "#06D6A0",
                            "Warm Orange": "#FF9F1C",
                            "Royal Purple": "#7C3AED",
                            "Ruby Red": "#EF4444",
                            "Ocean Teal": "#0D9488",
                            "Custom": "custom"
                        }
                        
                        selected_palette = st.selectbox(
                            "Color Scheme",
                            list(palette_options.keys()),
                            index=0,
                            key="color_scheme"
                        )
                        
                        color_palette = palette_options[selected_palette]
                        if selected_palette == "Custom":
                            color_palette = st.color_picker(
                                "Pick a Custom Color",
                                value="#4F46E5",
                                key="color_picker"
                            )
                    
                    with st.expander("Advanced Settings", expanded=True):
                        log_scale_options = st.columns(2)
                        with log_scale_options[0]:
                            log_y = st.checkbox("Log Y Scale", key="log_y") if chart_type not in ["Pie", "Radar", "Sunburst"] else None
                        with log_scale_options[1]:
                            log_x = st.checkbox("Log X Scale", key="log_x") if chart_type in ["Scatter", "Bubble"] else None
                        
                        trend_line = st.checkbox("Show Trend Line", key="trend_line") if chart_type in ["Scatter", "Line"] else None
                        
                        animation_frame = None
                        if chart_type in ["Scatter", "Bubble", "Line", "Bar"]:
                            animation_frame = st.selectbox(
                                "Animate Over",
                                ["None"] + date_cols + categorical_cols,
                                index=0,
                                key="animation_frame"
                            )
                        
                        normalize = st.selectbox(
                            "Normalization",
                            ["None", "Min-Max", "Z-Score"],
                            key="normalize"
                        ) if chart_type not in ["Pie", "Radar", "Sunburst"] else None
                        
                        # Filter data range
                        if x_axis and x_axis in numeric_cols + date_cols:
                            with st.expander("Filter Data Range", expanded=False):
                                if x_axis in date_cols:
                                    min_date = df[x_axis].min().date()
                                    max_date = df[x_axis].max().date()
                                    date_range = st.date_input(
                                        f"Filter {x_axis} Range",
                                        value=(min_date, max_date),
                                        min_value=min_date,
                                        max_value=max_date,
                                        key="date_range"
                                    )
                                else:
                                    min_val = float(df[x_axis].min())
                                    max_val = float(df[x_axis].max())
                                    value_range = st.slider(
                                        f"Filter {x_axis} Range",
                                        min_value=min_val,
                                        max_value=max_val,
                                        value=(min_val, max_val),
                                        key="value_range"
                                    )
                    
                    # New section for annotations
                    with st.expander("Chart Annotations", expanded=False):
                        show_title = st.checkbox("Show Title", value=True, key="show_title")
                        if show_title:
                            chart_title = st.text_input("Chart Title", value=f"{chart_type} Chart of {y_axis if y_axis else x_axis}", key="chart_title")
                        
                        show_annotations = st.checkbox("Show Data Point Labels", value=False, key="show_annotations")
                        if show_annotations:
                            annotation_column = st.selectbox(
                                "Label Column",
                                df.columns.tolist(),
                                index=0,
                                key="annotation_column"
                            )
            
            # Visualization Canvas
            with cols[1]:
                st.markdown('<div class="chart-container"><h4 style="margin-top: 0;">📊 Visualization Canvas</h4></div>', unsafe_allow_html=True)
                
                try:
                    # Data Processing
                    plot_df = df.copy()
                    
                    # Apply date range filter if applicable
                    if x_axis in date_cols and 'date_range' in st.session_state:
                        min_date, max_date = st.session_state.date_range
                        plot_df = plot_df[(plot_df[x_axis].dt.date >= min_date) & (plot_df[x_axis].dt.date <= max_date)]
                    
                    # Apply value range filter if applicable
                    if x_axis in numeric_cols and 'value_range' in st.session_state:
                        min_val, max_val = st.session_state.value_range
                        plot_df = plot_df[(plot_df[x_axis] >= min_val) & (plot_df[x_axis] <= max_val)]
                    
                    # Validate columns exist
                    required_cols = [x_axis]
                    if y_axis: required_cols.append(y_axis)
                    if color_by != "None": required_cols.append(color_by)
                    if animation_frame and animation_frame != "None": required_cols.append(animation_frame)
                    
                    missing_cols = [col for col in required_cols if col not in plot_df.columns]
                    if missing_cols:
                        raise ValueError(f"Missing columns: {', '.join(missing_cols)}")

                    # Apply normalization if needed
                    if normalize and normalize != "None" and y_axis:
                        try:
                            if normalize == "Min-Max":
                                plot_df[y_axis] = (plot_df[y_axis] - plot_df[y_axis].min()) / (plot_df[y_axis].max() - plot_df[y_axis].min())
                            elif normalize == "Z-Score":
                                plot_df[y_axis] = (plot_df[y_axis] - plot_df[y_axis].mean()) / plot_df[y_axis].std()
                        except Exception as e:
                            st.warning(f"Normalization failed: {str(e)}")

                    # Handle aggregation
                    if agg_func != "None" and y_axis and chart_type not in ["Scatter", "Bubble", "Box", "Violin"]:
                        try:
                            if group_by:
                                # Ensure x_axis is included in group_by if needed
                                if x_axis not in group_by and x_axis in plot_df.columns:
                                    group_by = [x_axis] + group_by
                                
                                plot_df = plot_df.groupby(group_by, as_index=False).agg({y_axis: agg_func})
                            else:
                                # If no group_by, use x_axis as default grouping
                                if x_axis in plot_df.columns:
                                    st.info(f"Aggregating by unique {x_axis} values")
                                    plot_df = plot_df.groupby(x_axis, as_index=False).agg({y_axis: agg_func})
                                else:
                                    raise ValueError("Cannot aggregate without Group By or valid X-Axis")
                        except Exception as e:
                            raise ValueError(f"Aggregation failed: {str(e)}")

                    # Create visualization based on chart type
                    fig = None
                    
                    # Define common parameters
                    common_params = {
                        "color": color_by if color_by != "None" else None,
                        "color_discrete_sequence": [color_palette],
                        "template": "plotly_white",
                        "title": chart_title if show_title else None,
                        "animation_frame": animation_frame if animation_frame != "None" else None,
                        "labels": {col: col.replace("_", " ").title() for col in plot_df.columns},
                        "hover_data": required_cols
                    }
                    
                    if chart_type == "Line":
                        fig = px.line(
                            plot_df, 
                            x=x_axis, 
                            y=y_axis,
                            line_group=group_by[0] if group_by else None,
                            log_y=log_y,
                            **common_params
                        )
                        if trend_line:
                            fig.add_trace(px.scatter(plot_df, x=x_axis, y=y_axis, trendline="lowess").data[1])
                    
                    elif chart_type == "Bar":
                        fig = px.bar(
                            plot_df, 
                            x=x_axis, 
                            y=y_axis,
                            barmode="group" if group_by else "relative",
                            log_y=log_y,
                            **common_params
                        )
                    
                    elif chart_type == "Scatter":
                        fig = px.scatter(
                            plot_df, 
                            x=x_axis, 
                            y=y_axis,
                            size=group_by[0] if group_by else None,
                            log_x=log_x,
                            log_y=log_y,
                            trendline="lowess" if trend_line else None,
                            **common_params
                        )
                    
                    elif chart_type == "Area":
                        fig = px.area(
                            plot_df,
                            x=x_axis,
                            y=y_axis,
                            log_y=log_y,
                            **common_params
                        )
                    
                    elif chart_type == "Bubble":
                        # Need a size variable for bubble chart
                        size_var = group_by[0] if group_by else (numeric_cols[0] if numeric_cols and numeric_cols[0] != x_axis and numeric_cols[0] != y_axis else None)
                        if size_var:
                            fig = px.scatter(
                                plot_df,
                                x=x_axis,
                                y=y_axis,
                                size=size_var,
                                size_max=30,
                                log_x=log_x,
                                log_y=log_y,
                                **common_params
                            )
                        else:
                            raise ValueError("Bubble chart requires a numeric column for size")
                    
                    elif chart_type == "Box":
                        fig = px.box(
                            plot_df,
                            x=x_axis,
                            y=y_axis,
                            **common_params
                        )
                    
                    elif chart_type == "Violin":
                        fig = px.violin(
                            plot_df,
                            x=x_axis,
                            y=y_axis,
                            box=True,
                            **common_params
                        )
                    
                    elif chart_type == "Heatmap":
                        # Prepare data for heatmap - needs aggregation
                        if y_axis:
                            heatmap_df = plot_df.pivot_table(
                                values=numeric_cols[0] if numeric_cols else None,
                                index=y_axis,
                                columns=x_axis,
                                aggfunc=agg_func if agg_func != "None" else "count"
                            )
                            fig = px.imshow(
                                heatmap_df,
                                color_continuous_scale=px.colors.sequential.Blues,
                                **{k: v for k, v in common_params.items() if k not in ['color', 'animation_frame']}
                            )
                        else:
                            raise ValueError("Heatmap requires Y-Axis selection")
                    
                    elif chart_type == "Radar":
                        # For radar chart, use categorical for theta and numeric for r
                        if categorical_cols and numeric_cols:
                            fig = px.line_polar(
                                plot_df,
                                r=y_axis,
                                theta=x_axis,
                                line_close=True,
                                **common_params
                            )
                        else:
                            raise ValueError("Radar chart requires categorical and numeric columns")
                    
                    elif chart_type == "Pie":
                        fig = px.pie(
                            plot_df,
                            names=x_axis,
                            values=group_by[0] if group_by else y_axis if y_axis else None,
                            hole=0.3,
                            **common_params
                        )
                    
                    elif chart_type == "Sunburst":
                        # For sunburst we need path columns
                        path = [x_axis]
                        if group_by:
                            path.extend(group_by)
                        
                        fig = px.sunburst(
                            plot_df,
                            path=path,
                            values=y_axis if y_axis else None,
                            **common_params
                        )
                    
                    # Final validation that fig was created
                    if fig is None:
                        raise ValueError("Could not generate visualization with current settings")
                    
                    # Add annotations if requested
                    if show_annotations and chart_type in ["Scatter", "Bubble", "Line", "Bar"]:
                        for i, point in enumerate(plot_df.iloc[:min(20, len(plot_df))].iterrows()):  # Limit to 20 annotations
                            point_data = point[1]
                            if x_axis in point_data and y_axis in point_data and annotation_column in point_data:
                                fig.add_annotation(
                                    x=point_data[x_axis],
                                    y=point_data[y_axis],
                                    text=str(point_data[annotation_column]),
                                    showarrow=True,
                                    arrowhead=2,
                                    arrowsize=1,
                                    arrowwidth=1,
                                    arrowcolor="#636363",
                                    ax=0,
                                    ay=-30,
                                    font=dict(size=10, color="#4F46E5")
                                )
                    
                    # Style enhancements
                    fig.update_layout(
                        plot_bgcolor='rgba(250,250,255,0.95)',
                        paper_bgcolor='rgba(255,255,255,0.5)',
                        font={'family': 'Arial, sans-serif', 'color': '#2D3748', 'size': 12},
                        margin=dict(t=50 if show_title else 30, b=40, l=40, r=20),
                        hoverlabel=dict(
                            bgcolor="white",
                            font_size=12,
                            font_family="Arial, sans-serif"
                        ),
                        legend=dict(
                            bordercolor="rgba(0,0,0,0.1)",
                            borderwidth=1,
                            orientation="h" if chart_type not in ["Pie", "Sunburst"] else "v"
                        ),
                        xaxis=dict(
                            title_font=dict(size=14),
                            gridcolor='rgba(211, 211, 211, 0.3)',
                            showline=True,
                            linecolor='rgba(211, 211, 211, 0.5)',
                        ),
                        yaxis=dict(
                            title_font=dict(size=14),
                            gridcolor='rgba(211, 211, 211, 0.3)',
                            showline=True,
                            linecolor='rgba(211, 211, 211, 0.5)',
                        )
                    )
                    
                    # Add watermark
                    fig.add_annotation(
                        text="DataViz Studio",
                        x=0.5,
                        y=0.5,
                        xref="paper",
                        yref="paper",
                        showarrow=False,
                        font=dict(size=30, color="rgba(211, 211, 211, 0.2)"),
                        textangle=-30
                    )
                    
                    # Display the figure
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Show insights if chart was created successfully
                    with st.expander("🔍 Chart Insights", expanded=False):
                        insights_cols = st.columns([3, 2])
                        
                        with insights_cols[0]:
                            st.markdown("#### Statistical Insights")
                            if y_axis and y_axis in numeric_cols:
                                stats_df = pd.DataFrame({
                                    "Metric": ["Mean", "Median", "Min", "Max", "Std Dev"],
                                    "Value": [
                                        f"{plot_df[y_axis].mean():.2f}",
                                        f"{plot_df[y_axis].median():.2f}",
                                        f"{plot_df[y_axis].min():.2f}",
                                        f"{plot_df[y_axis].max():.2f}",
                                        f"{plot_df[y_axis].std():.2f}"
                                    ]
                                })
                                st.dataframe(stats_df, hide_index=True, use_container_width=True)
                            else:
                                st.info("Select a numeric Y-axis to see statistical insights")
                        
                        with insights_cols[1]:
                            st.markdown("#### Data Sample")
                            st.dataframe(plot_df.head(5), use_container_width=True)
                
                except Exception as e:
                    st.error(f"""
                    **🚨 Visualization Error**
                    ```python
                    {str(e)}
                    ```
                    **Troubleshooting Steps:**
                    1. Verify all selected columns exist in your data
                    2. Check that numeric columns contain valid numbers
                    3. Try different aggregation or grouping combinations
                    4. For pie charts, ensure your X-Axis has limited unique values
                    5. Reset to default settings and try again
                    """)
                    
                    # Show raw data for debugging
                    with st.expander("🔍 View Raw Data for Selected Columns"):
                        try:
                            st.dataframe(plot_df[required_cols].head(10), use_container_width=True)
                        except:
                            st.dataframe(df.head(10), use_container_width=True)
                    
                    st.stop()

        # ===== Visualization Tools =====
        with st.container():
            st.markdown("---")
            cols = st.columns([1, 1, 2])
            
            with cols[0]:
                st.markdown("#### 🎨 Style Presets")
                preset_cols = st.columns(3)
                with preset_cols[0]:
                    corporate = st.button("Corporate", use_container_width=True)
                    if corporate:
                        color_palette = "#4F46E5"
                with preset_cols[1]:
                    vibrant = st.button("Vibrant", use_container_width=True)
                    if vibrant:
                        color_palette = "#06D6A0"
                with preset_cols[2]:
                    pastel = st.button("Pastel", use_container_width=True)
                    if pastel:
                        color_palette = "#FFD166"
            
            with cols[1]:
                st.markdown("#### 📤 Export")
                if fig:  # Only show export if figure exists
                    btn_cols = st.columns(2)
                    with btn_cols[0]:
                        # Export as PNG
                        buffer = BytesIO()
                        fig.write_image(file=buffer, format="png", scale=2)
                        st.download_button(
                            label="📷 Download PNG",
                            data=buffer,
                            file_name=f"{chart_type.lower()}_{x_axis}_{y_axis if y_axis else ''}.png",
                            mime="image/png",
                            use_container_width=True
                        )
                    
                    with btn_cols[1]:
                        # Export data
                        csv = plot_df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📦 Export Data",
                            data=csv,
                            file_name=f"vis_data_{x_axis}_{y_axis if y_axis else ''}.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                        
                   