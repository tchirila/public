clear all; % clears memory
close all; % closes all open figures
clc;       % clears the command window

x(1) = 0;            % initial x-coordiante of particles
y(1) = 0;            % initial y-coordinate of particles
stepsize = 0.01;     % constant jump size
n = 2000;            % number of timestepts
Npart = 100000;      % number of particles
count = 0;           % used to count particles with r <= 1.2
rdelta = 0.05;       % sets the bin size
rall = 0:rdelta:1.2; % sets every bin value
rbin = 1.2/rdelta;   % calculates number of bins

for j = 1:Npart % iterates for every particle at a time
    for i = 1:n % iterates for every time-step
        angle =  2*pi*rand; % sets the random angle
        x(i+1) = x(i)+stepsize*cos(angle); % calculates the next x-coordinate of the particle
        y(i+1) = y(i)+stepsize*sin(angle); % calculates the next y-coordinate of the particle
    end
    xparticle(j) = x(i); % stores the x-coordinate of each particle
    yparticle(j) = y(i); % stores the y-coordinate of each particle
    r = sqrt((xparticle(j))^2+(yparticle(j))^2); % calculates the distance from the origin
    if r <= 1.2
        count = count+1;  % counts each successful 'if' condition met
        rvalue(count) = r; % stores particles that meet the 'if' condition
    end
end

numden = histc(rvalue, rall); % histogram count of the numerical number density.
dendis = numden./(pi*(2.*rall.*rdelta+(rdelta).^2)); % numerical density distribution

andendis = Npart/(pi*n*stepsize^2)*exp(-rall.^2/(n*stepsize^2)); % analytical den. distr.

for i = 1:length(rall)
    annumdis(i) = andendis(i)*pi*((rall(i)+rdelta)^2-rall(i)^2); % anlytical num. distr.
end

figure(4)
bar(rall, dendis) % plots the numerical density distribution
hold on; % holds current plot and all axis properties
plot(rall, andendis, 'r-') % plots the analytical density distribution
xlabel('r value, bin = 0.05'); % sets the x-axis label
ylabel('counts'); % sets the y-axis label
title('Particle Density Distribution'); % sets the title
legend('Numerical Solution', 'Analytical Solution', 'location', 'Northeast');

figure(3)
hist(rvalue, rbin) % plots the numerical number distribution
hold on; % holds current plot and all axis properties
plot(rall, annumdis, 'r-') % plots the analytical number distribution
xlabel('r value, bin = 0.05'); % sets the x-axis label
ylabel('counts'); % sets the y-axis label
title('Particle Number Distribution'); % sets the title
legend('Numerical Solution', 'Analytical Solution', 'location', 'Northeast');

figure(2)
plot(xparticle, yparticle, 'k.') % plots the generated points
xlabel('X-direction'); % sets the x-axis label
ylabel('Y-direction'); % sets the y-axis label
title('Random Walk of 2000 Particles'); % sets the title
axis equal; % fixes aspect ratio issues 

figure(1)
plot(x, y, 'k.') % plots the generated points
xlabel('X-direction'); % sets the x-axis label
ylabel('Y-direction'); % sets the y-axis label
title('Random Walk of 1 Particle'); % sets the title
axis equal; % fixes aspect ratio issues 
