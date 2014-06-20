plot3(x,y,z);
axis vis3d

fps = 60; sec = 10;

vidObj = VideoWriter('plotrotation.avi');
vidObj.Quality = 100;
vidObj.FrameRate = fps;

open(vidObj);
for i=1:fps*sec
  camorbit(0.9,-0.1);
  writeVideo(vidObj,getframe(gcf));
end
close(vidObj);