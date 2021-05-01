import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math  # for erf


def get_plot(U, a, D):
    t = np.arange(3000)
    get_2dplot(U, a, D, t)
    get_3dplot(U, a, D, t)


def get_2dplot(U, a, D, t):
    k = ((a*U*2)**2)/(192*D)  # coefficient of diffusion

    L = 3.62*((k*t)**0.5)

    fig, ax = plt.subplots()
    ax.plot(t, L)
    ax.set_title("Laminar")
    ax.set_xlabel("Time")
    ax.set_ylabel("Length of the Transition Region")
    st.pyplot(fig)


def get_3dplot(U, a, D, t):
    k = ((a*U*2)**2)/(192*D)

    x = np.arange(3000)
    x1 = np.zeros((3000, 3000))
    z = np.zeros((3000, 3000))
    for i in range(3000):
        x1[i, :] = x[i] - U*t

    z = [[zvalue(x1[i, j], k, t[j]) for j in range(3000)] for i in range(3000)]
    z = np.array(z)

    # for i in range(3000):
    #     for j in range(3000):
    #         z[i, j] = zvalue(x1[i, j], k, t[j])

    ax = plt.axes(projection='3d')
    fig = ax.get_figure()
    ax.plot_surface(x, t, z)
    ax.set_title("Laminar")
    ax.set_xlabel("Distance")
    ax.set_ylabel("Time")
    ax.set_zlabel("C/C0")
    st.pyplot(fig)


def zvalue(x, k, t):
    # if x <= 0:
    #     z = 1/2 + (1/2)*math.erf(0.5*x*((k*t)**(-0.5)))
    # else:
    z = 1/2 - (1/2)*math.erf(0.5*x*((k*t)**-0.5))
    return z
