import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root


def f(x, data):
    y = x**(-0.5) + 0.4 - 4*np.log(data) - 2*np.log(x)
    return y


def get_plot(rho, mu, U, a, D):
    R = 2*rho*U*a/mu
    gamma = root(f, x0=0.001, args=R)
    b = (0.5*gamma.x)**0.5
    K = 10.1*a*b*U

    t = np.arange(1500)
    L = ((437*a*b*U)*t) ** 0.5

    fig, ax = plt.subplots()
    ax.plot(t, L)
    ax.set_title("Turbulent")
    ax.set_xlabel("Length of the Transition Region")
    ax.set_ylabel("Time")
    st.pyplot(fig)
