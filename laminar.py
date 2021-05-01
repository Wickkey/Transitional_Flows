import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def get_plot(U, a, D):
    k = ((a*U*2)**2)/(192*D)  # coefficient of diffusion

    t = np.arange(3000)
    L = 3.62*((k*t)**0.5)

    fig, ax = plt.subplots()
    ax.plot(t, L)
    ax.set_title("Laminar")
    ax.set_xlabel("Length of the Transition Region")
    ax.set_ylabel("Time")
    st.pyplot(fig)
