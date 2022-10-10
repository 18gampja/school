% Jacob Gampa
% CMPSC 497 HW #2
% jag6611@psu.edu 1 + 5 = 6

se = strel('rectangle', [20 20]);
original = imread('imcloseTest.png');
imshow(original);

afterOpening = imopen(original, se);
figure
% imshow(afterOpening, []);
% size(original)
% size(afterOpening)

closeOriginal = imread('imcloseTest.png');
closingSE = strel('disk', 10);
afterClosing = imclose(closeOriginal, closingSE);
size(original)
size(afterClosing)
imshow(afterClosing, []);