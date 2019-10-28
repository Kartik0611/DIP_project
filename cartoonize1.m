clear;
clc;

I=getImageUI(); % Custom built function 

[gray,grayFlag,r,c] = getGrayImageInfo(I); 

div=8;
numSteps = 256/div;
stepdown = @(pixel) pixel-mod(pixel,numSteps);

% q=zeros(r,c,ch);
% q(:,:,:) = stepdown(I(:,:,:))/255;

w=stepdown(I) ;

cannyedge=edge(gray,'canny');
edge = xor(ones(r,c),cannyedge);

cartooneffect1 = double(w)/255.*edge;
cartooneffect2 = double(w)/255;

imshowpair(I,cartooneffect2,'montage')