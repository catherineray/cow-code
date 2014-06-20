function surfaceplot(x,y)
	tri = delaunay(x,y);
	plot(x,y,'.')

	%determine amount of triangles
	[r,c] = size(tri);
	disp(r)

	%plot with trisurf
	h = trimesh(tri, x, y, z, 'FaceAlpha', 0.6);
	alpha = 0.4
	view(15, 48)
	axis vis3d

	axis off
	l = light('Position',[-50 -15 29])
	lighting phong
	shading interp