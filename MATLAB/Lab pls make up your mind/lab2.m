% Jacob
% CMPSC 497 Lab 2

im = imread('test.png');
% imshow(im);
se = [0, 0, 0, 1, 1, 0, 0, 0]

mask = [1, 2, 1];

x = imfilter(se, mask)
% imtest = imclose(im, strel);
% imshow(imtest);
% gray = rgb2gray(im);
% gray = medfilt2(gray);
% 
% BW = edge(gray, 'canny');


% Line generation provided in class
% [H, theta, rho] = hough(BW);
% 
% P = houghpeaks(H, 5, 'threshold', ceil(0.6 * max(H(:))));
% x = theta(P(:, 2));
% y = rho(P(:, 1));

% lines = houghlines(BW, theta, rho, P, 'FillGap', 5, 'MinLength', 5);

% 
% maxLen = 0;
% center = false;

% Creates divisions
% [div1, div2] = size(gray);
% 
% divFarLeft = div2 * 0.2;
% 
% divSlightLeft = div2 * 0.4
% 
% divSlightRight = div2 * 0.6
% 
% divFarRight = div2 * 0.8
% 
% figure, imshow(gray), hold on
% 
% for k = 1:length(lines)

%     This is some bonus code that just tries to draw the line in the
%     middle of two detected lines

%     if length(lines) > 1 && k ~= length(lines)
% 
%         if(abs(lines(k).point1 - lines(k + 1).point1) < 20)
%             
%             newX = (lines(k).point1 + lines(k + 1).point1) / 2;
%             newY = (lines(k).point2 + lines(k + 1).point2) / 2;
%             xy = [newX; newY];
%             center = true;
%           
%         end
% 
%     else
% 
%         if center == true
% 
%             newX = (lines(k).point1 + lines(k - 1).point1) / 2;
%             newY = (lines(k).point2 + lines(k - 1).point2) / 2;
%             xy = [newX; newY];     
% 
%         else
% 
%             xy = [lines(k).point1; lines(k).point2];
%         
%         end
% 
%     end
% 
% %   Declares turn bools
%     turnSlightRight = false;
%     turnSlightLeft = false;
%     goForward = false;
%     turnHardRight = false;
%     turnHardLeft = false;
% 
% %   Checks whether or not the bot should be turning
%     if(xy(1) < divFarLeft)
% 
%         turnHardRight = true;
% 
%     elseif(xy(1) < divSlightLeft)
% 
%         turnSlightRight = true;
% 
%     elseif(xy(1) > divFarRight)
% 
%         turnHardLeft = true;
% 
%     elseif(xy(1) > divSlightRight)
% 
%         turnSlightLeft = true;
% 
%     else
% 
%         goForward = true;
% 
%     end
% 
% %   Displays appropriate message for where the bot should turn
%     if turnSlightRight == true
%         
%         pos = [div1 / 2, div2 / 2];
%         gray = insertText(gray, pos, 'Take a slight right', 'FontSize', 15);
%         imshow(gray)
% 
% 
% 
%     elseif turnHardRight == true
%         
%         pos = [div1 / 2, div2 / 2];
%         gray = insertText(gray, pos, 'Take a hard right', 'FontSize', 15);
%         imshow(gray)
% 
%     elseif turnSlightLeft == true
% 
%         pos = [div1 / 2, div2 / 2];
%         gray = insertText(gray, pos, 'Take a slight left', 'FontSize', 15);
%         imshow(gray)
% 
%     elseif turnHardLeft == true
% 
%         pos = [div1 / 2, div2 / 2];
%         gray = insertText(gray, pos, 'Take a hard left', 'FontSize', 15);
%         imshow(gray)
% 
%     elseif goForward == true
%         
%         pos = [div1 / 2, div2 / 2];
%         gray = insertText(gray, pos, 'Go Forward', 'FontSize', 15);
%         imshow(gray)
% 
%     end
% 
% %   Plot lines
%     plot(xy(:, 1), xy(:, 2), 'LineWidth', 2, 'Color', 'green');
% 
%     plot(xy(1, 1), xy(1, 2), 'x', 'LineWidth', 2, 'Color', 'yellow');
%     plot(xy(2, 1), xy(2, 2), 'x', 'LineWidth', 2, 'Color', 'red');
% 
%     len = norm(lines(k).point1 - lines(k).point2);
% 
%     if (len > maxLen)
% 
%         maxLen = len;
%         xyLong = xy;
% 
%     end
% end