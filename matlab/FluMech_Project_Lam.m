
clc; clear all; close all; clearvars; format short g; format compact;

% Parameters
u0 = 20; a = 0.5; D = 5;
U = (1/2)*u0;
k = ((a*u0)^2)/(192*D);

x1 = zeros(3001,3001);
x = 0 : 1 : 3000;
t = 0 : 1 : 3000;
for i = 1:3001
    x1(i,:) = x(i) - U*t;
end

% Concentration Profile
for i = 1 : 3001
    for j = 1 : 3001
        if x1(i,j)<=0
            z(i,j) = 1/2 + (1/2)*erf(0.5*x1(i,j)*((k*t(j))^-0.5));
        else
            z(i,j) = 1/2 - (1/2)*erf(0.5*x1(i,j)*((k*t(j))^-0.5));
        end
    end
end


figure('units','normalized','outerposition',[0 0 1 1])
surf(x, t, z)
xlabel('Distance','FontSize',14); ylabel('Time','FontSize',14); zlabel('C/C0','FontSize',14);
grid on

% Length of transition region
L = 3.62*((k.*t).^0.5);

figure('units','normalized','outerposition',[0 0 1 1])
plot(t,L)
xlabel('Time','FontSize',14); ylabel('Length of the Transition Region','FontSize',14)
grid on