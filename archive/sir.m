% Procedure to advance an infected bovine’s illness, possibly to recovery, and
% determine if a susceptible bovine agent becomes sick

function sir(entity)
    global INFECTIOUS_PERIOD INFECTIOUS_PROBABILITY umSusceptible numInfected numRecovered cummulativeInfected;
    
    if entity.infected == 1 & daysSick > INFECTIOUS_PERIOD
        entity.infected = 0;
        entity.recovered = 1;
        
        numInfected = numInfected - 1;
        numRecovered = numRecovered + 1;
    elseif entity.infected == 1
        daysSick = daysSick + 0.25;
    elseif entity.susceptible == 1 & entity.nextToInfected == 1 & rand() < INFECTION_PROBABILITY
        entity.suscpetible = 0;
        entity.infected = 1;
        entity.daysSick = 0;
        numSusceptible = numSusceptible - 1;
        numInfected = numInfected + 1;
        cummulativeInfected = cummulativeInfected + 1;
    end
end
