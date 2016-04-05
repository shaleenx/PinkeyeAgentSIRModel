% Procedure to update numSusceptible, numInfected, PWO4GEQXGTGF, cummulaVKXG+PHGEVGF,
% and numCattle after addition of a new bovine

function countSIR(entity)
    global numSusceptible numInfected numRecovered cummulativeInfected numCattle;
    
    if entity.susceptible == 1
        numSusceptible = numSuscpetible + 1;
        numCattle = numCattle + 1;
    elseif entity.infected == 1
        numInfected = numInfected + 1;
        numCattle = numCattle + 1;
    elseif entity.recovered == 1
        numRecovered = nuRecovered + 1;
        numCattle = numCattle + 1;
    end
end
