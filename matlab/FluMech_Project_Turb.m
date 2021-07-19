
clc; clear all; close all; clearvars; format short g; format compact;

% Parameters
global a R U
a = 0.5; U = 100; rho = 1000; mu = 0.5; 
R = 2*rho*U*a/mu;
t = 0 : 1 : 1500;
x = -500 : 1 : 1000;
x1 = x - U*t;
[X,T] = meshgrid(x1,t);

% Solving for K
gamma = fsolve(@(gamma) gammafun(R,gamma),[1]);
b = sqrt(0.5*gamma);
K = 10.1*a*b*U;

% Concentration profile
C = @(x1,t) 0.5 - 0.5.*erf((1/2).*x1.*((K.*t).^-0.5));


figure('units','normalized','outerposition',[0 0 1 1])
surf(x , t , C(X,T))
xlabel('Distance','FontSize',14); ylabel('Time','FontSize',14); zlabel('C/C0','FontSize',14);
grid on

% Length of the Transition Layer
L = ((437*a*b*U).*t).^0.5;

figure('units','normalized','outerposition',[0 0 1 1])
plot(t, L)
xlabel('Time','FontSize',14); ylabel('Length','FontSize',14)
grid on


function f = gammafun(R,gamma)
    global R
    f = (gamma)^-0.5 + 0.4 - 4*log(R) - 2*log(gamma);
end