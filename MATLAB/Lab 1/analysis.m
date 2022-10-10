% Jacob Gampa
% CMPSC 497 HW #1

voltages = [21.2, 19.5, 20.1, 18.3, 17.7, 15.0, 21.9, 24.7, 23.1, 20.2, 16.3, 22.8, 18.4, 23.5, 21.1];

minimum = min(voltages)
maximum = max(voltages)
average = mean(voltages)
deviation = std(voltages)
med = median(voltages)
aboveAvg = length(find(voltages > average))
valAbove = voltages(find(voltages > average))
% plot(voltages)
% title("voltages (volts)")
% xlabel("times")
% ylabel("voltages (volts)")
hist(voltages)
xlabel("voltages (volts)")
ylabel("frequency")
sorted = sort(voltages)
fprintf("Sorted Values = %.7f volts\n", sort(voltages));
fprintf("Values above average = %.7f volts\n", voltages(find(voltages > average)));
