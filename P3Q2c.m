
close all
clear all
clc

%As we're interested in normalised masses, m_p + m_s = 1. We know that
%m_p/m_s = 3:
m_p = 3/4;
m_s = 1/4;

%time step and iteration range:
h = 0.1;
period = 2 * pi;
t = (0 + h):h:(2*period);

%initial conditions:
x_p(1) = m_s;
x_s(1) = m_p;
v_p(1) = m_s;
v_s(1) = m_p;

%the vector:
X_p = [x_p v_p];
X_s = [x_s v_s];

for i = 1:length(t)
    pos_p(i) = X_p(1);
    vel_p(i) = X_p(2);
    pos_s(i) = X_s(1);
    vel_s(i) = X_s(2);
    X_p = RK(h,t,X_p);
    X_s = RK(h,t,X_s);
end

for i = 1:length(t)
    angle = (t(i)/period)*2*pi;
    xcomp_p(i) = pos_p(i) * cos(angle);
    ycomp_p(i) = pos_p(i) * sin(angle);
    xcomp_s(i) = pos_s(i) * cos(angle);
    ycomp_s(i) = pos_s(i) * sin(angle);
end

plot(xcomp_p,ycomp_p,'k.',xcomp_s,ycomp_s,'b.')
xlabel('x')
ylabel('y')
axis equal
