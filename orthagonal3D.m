function orthogonal3d(i,j,k)
xmax = 135;
ymax = 59;
zmax = 16;

%orthogonal lines through the point (i,j,k)
Xx = 0:(xmax)/10:xmax;
Yx = j*ones(1,11);
Zx = k*ones(1,11);

Xy = i*ones(1,11);
Yy = 0:(ymax)/10:ymax;
Zy = k*ones(1,11);

Xz = i*ones(1,11);
Yz = j*ones(1,11);
Zz = 0:(zmax)/10:zmax;

plot3(Xx, Yx, Zx)
hold on
plot3(i,j,k,'ws--', 'MarkerEdgeColor', 'r', 'MarkerFaceColor', 'r')
plot3(Xy, Yy, Zy)
plot3(Xz, Yz, Zz)

%define the view
view(60,10)
daspect([2,2,1])
axis tight
end