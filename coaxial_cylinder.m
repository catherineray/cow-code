Y=-5:5;
theta=linspace(0,2*pi,40);
[Y,theta]=meshgrid(Y,theta);

r = 1.5
% calculate x and z
X=r*cos(theta);
Z=r*sin(theta);

hs = surf(X,Y,Z)

set(hs,'EdgeColor','None', ...
        'FaceColor', [0.5 0.5 0.5], 'FaceLighting', 'phong');
alpha(0.7);

hold on
camlight right;

r = 0.5
% recalculate x and z
X=r*cos(theta);
Z=r*sin(theta);

hs = surf(X,Y,Z)

axis equal

set(hs,'EdgeColor','None', ...
        'FaceColor', [0.5 0.5 0.5], 'FaceLighting', 'phong');
alpha(0.7);

axis off
camlight right;
lighting gouraud
view(140, 24)

% white background
set(gcf,'color','white')