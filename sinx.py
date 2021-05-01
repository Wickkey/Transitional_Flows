import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root
import laminar
import turbulent
import SessionState

session_state = SessionState.get(checkboxed=False)

plt.style.use("fivethirtyeight")

st.title("Flow Assurance\n\n")
# st.sidebar.header("y = ####edit")
st.sidebar.subheader("Parameters (Use CGS units)")


rho = st.sidebar.number_input("   Density", min_value=0.0,
                              max_value=10000.0, value=1000.0, step=0.1)
mu = st.sidebar.number_input("   Viscosity", min_value=0.01,
                             max_value=1000.0, value=0.5, step=0.01)
U = st.sidebar.number_input("   Average Velocity", min_value=0.0,
                            max_value=100.0, value=20.0, step=0.1)
A = st.sidebar.number_input("   Pipe diameter", min_value=0.0,
                            max_value=100.0, value=0.5, step=0.1)
D = st.sidebar.number_input("   Diffusion coefficient", min_value=0.1,
                            max_value=1000.0, value=5.0, step=0.1)

a = A/2  # radius of the pipe


if st.sidebar.button("Plot") or session_state.checkboxed:
    session_state.checkboxed = True
    count = 1

    Re = rho*U*a/mu
    if Re <= 2300:
        laminar.get_plot(U, a, D)
    elif Re > 2300:
        turbulent.get_plot(rho, mu, U, a, D)
