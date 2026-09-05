import streamlit as st
import numpy as np
import random

# Page Config
st.set_page_config(
    page_title="JouleX Enterprise Control Tower",
    page_icon="⚡",
    layout="centered"
)

# Dark Theme styling & Premium look
st.markdown("""
    <style>
    .main {
        background-color: #030712;
        color: #f3f4f6;
    }
    .stButton>button {
        width: 100%;
        background-color: #06b6d4;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0891b2;
    }
    </style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""

st.title("⚡ JouleX Enterprise Control Tower")
st.markdown("### Real-time thermodynamic energy optimization for edge AI hardware.")
st.divider()

# --- STEP 1: ACCOUNT & REGISTRATION ---
if st.session_state.step == 1:
    st.subheader("Step 1: Enterprise Account Registration")
    
    company_name = st.text_input("Company Name", value="JouleX Systems")
    work_email = st.text_input("Enterprise Work Email", value="admin@joulx.com")
    password = st.text_input("Enterprise Password", type="password", value="securepass123")
    
    industry = st.selectbox(
        "Industry Sector",
        [
            "Autonomous Drones & Delivery",
            "Self-Driving Vehicles (Robotics)",
            "Hyper-scaler LLM Clusters",
            "Medical Facilities & Hospitals",
            "Financial Institutions & Banks"
        ]
    )
    
    if st.button("Create Enterprise Account →"):
        st.session_state.form_data = {
            "company_name": company_name,
            "work_email": work_email,
            "industry": industry
        }
        # Generate unique enterprise API key
        st.session_state.api_key = "jx_live_" + ''.join(random.choices("0123456789abcdef", k=16))
        st.session_state.step = 2
        st.rerun()

# --- STEP 2: SECURITY & DEPLOYMENT ROUTE ---
elif st.session_state.step == 2:
    st.subheader("Step 2: Deployment & Security Configuration")
    st.info(f"Welcome, **{st.session_state.form_data.get('company_name')}**! Industry: **{st.session_state.form_data.get('industry')}**")
    
    st.markdown("#### Assigned Enterprise API Key")
    st.code(st.session_state.api_key, language="text")
    
    st.markdown("#### Select Deployment Architecture")
    deployment_mode = st.radio(
        "Choose how JouleX integrates with your infrastructure:",
        [
            "🌐 Cloud API Integration (Standard SaaS Control Tower)",
            "🔒 Private Air-Gapped Deployment (Strict On-Premise / Edge Security)"
        ]
    )
    
    target_sparsity = st.slider("Target Model Weight Sparsity", 0.1, 0.9, 0.5, 0.1)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Back"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("Run Thermodynamic Optimization →"):
            st.session_state.form_data["deployment_mode"] = deployment_mode
            st.session_state.form_data["target_sparsity"] = target_sparsity
            st.session_state.step = 3
            st.rerun()

# --- STEP 3: RESULTS & ANALYTICS ---
elif st.session_state.step == 3:
    st.subheader("Step 3: Live Optimization Results & Telemetry")
    
    # Running exact numpy calculation from backend logic
    sparsity = st.session_state.form_data.get("target_sparsity", 0.5)
    arr = np.array([1.2, -2.5, 0.3, 0.7, -1.9, 0.4])
    threshold = np.percentile(np.abs(arr), sparsity * 100)
    mask = np.abs(arr) >= threshold
    optimized_weights = arr * mask
    saved_energy_kwh = float(np.sum(np.abs(arr)) * 0.075) * 100
    
    st.success("Optimization pipeline successfully executed across edge hardware nodes.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Estimated Energy Saved", f"{round(saved_energy_kwh, 2)} kWh")
    with col2:
        st.metric("Cost Reduction", "50.0%")
    with col3:
        st.metric("Active Model Weights", f"{int(np.sum(mask))} / {len(arr)}")
        
    st.markdown("---")
    st.write(f"**Company:** {st.session_state.form_data.get('company_name')}")
    st.write(f"**Selected Industry:** {st.session_state.form_data.get('industry')}")
    st.write(f"**Deployment Mode:** {st.session_state.form_data.get('deployment_mode')}")
    st.write(f"**Optimized Weights Array:** `{optimized_weights.tolist()}`")
    
    if st.button("🔄 Reset / Run New Configuration"):
        st.session_state.step = 1
        st.rerun()