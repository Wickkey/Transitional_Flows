import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root
import math


def get_plot(rho, mu, U, a, D):
    t = np.arange(1500)
    R = 2*rho*U*a/mu
    gamma = root(f, x0=0.001, args=R)
    b = (0.5*gamma.x)**0.5
    K = 10.1*a*b*U

    get_plot2d(rho, mu, U, a, D, t, R, b, K)
    get_plot3d(rho, mu, U, a, D, t, R, b, K)


def f(x, data):
    y = x**(-0.5) + 0.4 - 4*np.log(data) - 2*np.log(x)
    return y


def get_plot2d(rho, mu, U, a, D, t, R, b, K):

    L = ((437*a*b*U)*t) ** 0.5

    fig, ax = plt.subplots()
    ax.plot(t, L)
    ax.set_title("Turbulent")
    ax.set_xlabel("Length of the Transition Region")
    ax.set_ylabel("Time")
    st.pyplot(fig)


def get_plot3d(rho, mu, U, a, D, t, R, b, K):

    x = np.arange(-500, 1000)

    x1 = np.zeros((1500, 1500))
    z = np.zeros((1500, 1500))
    for i in range(1500):
        x1[i, :] = x[i] - U*t

    z = [[zvalue(x1[i, j], K, t[j]) for j in range(1500)] for i in range(1500)]
    z = np.array(z)
    # x1 = x - U*t

    # X, T = np.meshgrid(x1, t)
    # z = z_function(X, T, K)

    ax = plt.axes(projection='3d')
    fig = ax.get_figure()
    ax.plot_surface(x, t, z)
    ax.set_title("Turbulent")
    ax.set_xlabel("Distance")
    ax.set_ylabel("Time")
    ax.set_zlabel("C/C0")
    st.pyplot(fig)


def zvalue(X, K, T):
    return 1/2 - (1/2)*math.erf(0.5*X*((K*T)**-0.5))
