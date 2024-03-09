%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                     DGIST - OOP - NBody Simulator
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Instructions:
% 1) Modify only the variables under the VARIABLES header to avoid
% complications.
% 2)Create you .txt file following the structure:
% Body0,tick0,XPosition,Yposition
% Body1,tick0,XPosition,Yposition
% Body2,tick0,XPosition,Yposition
% Body0,tick1,XPosition,Yposition
% Body1,tick1,XPosition,Yposition
% Body2,tick1,XPosition,Yposition
% Etc......
% If your file does not follow the previos format it won't work
% 3) You should place your .txt file in the same folder as this .m script
clc, close all;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                              VARIABLES
fileID = 'Example2.txt';
NBodies = 3;
SimulationStep = 1; %If the simulation is too slow, you can increase this variable in multiples of NBodies.
Bodysize = 10; %Changes marker size, make larger to see bigger objects.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                             PLOT CONFIGURATION
XYCoordinates = csvread(fileID,0,2);
[NIterations,Col] = size(XYCoordinates);
figure;
hold on;
%In this loop we create a marker for each body in the simulation
for i=1:NBodies
    OBJ(i) = plot(XYCoordinates(i,1),XYCoordinates(i,2),'wo','MarkerSize',...
        Bodysize,'MarkerFaceColor','w');
end
%We obtain the max and min to determine the axis, the variables MinAxis and
%MaxAxis are aboth vectors.
MinAxis = min(XYCoordinates);
MaxAxis = max(XYCoordinates);
axis([min(MinAxis) max(MaxAxis) min(MinAxis) max(MaxAxis)]);
axis off
set(gcf, 'color','k')

for i=NBodies:SimulationStep:NIterations
    for j=1:NBodies
        OBJ(j).XData = XYCoordinates(i+j,1);
        OBJ(j).YData = XYCoordinates(i+j,2);
    end
    drawnow
end