% Jacob Gampa
% CMPSC 497 HW #1

n = input("Enter the number of resistors please ");
sum = 0;
for i = 1:n
    r = input("Enter resistance ");
    sum = sum + 1/r;
end
fprintf("Total resistance = %.2f ohms \n", sum)