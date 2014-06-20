format compact
set(gcf,'Menubar','none','Name','Spheres', ...
 'NumberTitle','off','Position',[10,350,400,300], ...
 'Color',[0 0 0]);

h = axes('Position',[0 0 1 1]);

%Draws sphere
[X Y Z]=sphere(20);
C = Z^2 + Y^2;
hs = surf(X, Y, Z, C);

%sets wireframe to visible
set(hs,'EdgeColor',[0.5 0.5 0.5]);

%Alters transparency of sphere
alpha('color');
alphamap('rampdown');

%Sets lighting of sphere
camlight right;
lighting phong
hidden off
axis equal

%Create writerObj
writerObj = VideoWriter('sphere.avi');  
open(writerObj)

%Animated movie of the rotation of the 3D globe
oh=findobj(gca,'type','surface');
%Spins about z axis.
for i = 1:36
axis off;
rotate(oh,[0 0 1],10);
M(i) = getframe(gca);
frame = getframe;
writeVideo(writerObj,frame);
end
%Spins about y axis.
for i = 1:36
axis off;
rotate(oh,[0 1 0],10);
M(i) = getframe(gca);
frame = getframe;
writeVideo(writerObj,frame);
end
%Spins about x axis.
for i = 1:36
axis off;
rotate(oh,[1 0 0],10);
M(i) = getframe(gca);
frame = getframe;
writeVideo(writerObj,frame);
end

close(writerObj);