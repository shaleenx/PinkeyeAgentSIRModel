% Procedure to initialize new calf with a random weight between 60 and 100 lb,
% to establish the days sick to be 0 for an infected calf, and to establish various
% category counters

function calf = cattleInit(infected)
    calf = tlist(["infected", "weight", "daysSick"]);
    calf.weight = rand()*40 + 60 + 1;
    if infected == 1 then
        calf.daysSick = 0;
        calf.infected = 1;
    else
        calf.daysSick = -1;
    end
    % countSIR
end
