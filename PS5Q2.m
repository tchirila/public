clear all; % clears memory
close all; % closes all open figures
clc;       % clears the command window

Nx = 200;            % number of x steps
mu = 0.2;            % sets mu
tau = 0.2;           % sets tau
dx = 1/(Nx-1);       % grip-spacing, equation provided by question description
dtau = mu*dx^2;      % equation provided by question description
Ntau = tau*((1/dtau)+1); % number of time steps, equation provided by question description
x = 0:dx:1;          % sets every x value
t = 0:dtau:1;        % sets every t value
U = ones(length(t), Nx); % creates a matrix of ones
U(1,:) = 1;          % inital condition, temperature is 1
U(:,length(x)) = 0;  % outer boundary condition where temperature is 0
a = 1e4;             % radius in meters
thdif = 1e-6;        % thermal diffusivity in meters^2 per seconds

for i = 2:Ntau               % the following lines calculate the diffusion
    for j = 2:(length(x)-1)
        U(i,1) = U(i-1,2);     % inner boundary condition
        U(i,j) = (1-2*mu*(1+(1/(j-1))))*U(i-1,j)+(mu*U(i-1,j-1)+(mu*(1+(2/(j-1))))*U(i-1,j+1));
    end
    
    if U(i,1) <= 0.5 % checks for half temperature
        break  % breaks the loop, the plot will start from 0.5 temperature
    end
    time = i*dtau;
    t_total = ((time*a^2)/thdif)/(3600*24*365) % total time in years
end

plot(x, U(i,:), 'r.')
ylim([0 1]);                         % sets the limit for the y-direction
xlabel('Dimensionless Radius');      % sets the x-axis label
ylabel('Dimensionless Temperature'); % sets the y-axis label
title('Temperature Distribution');   % sets the title
