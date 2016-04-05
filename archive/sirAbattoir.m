% Procedure to adjust appropriate system variables when a beef cow is slaughtered

function sirAbattoir(entity)
    global numSusceptible numInfected numRecovered;
    if entity.onAbottoir == 1
        if entity.susceptible == 1
            numSusceptible = numSusceptible - 1;
        elseif entity.infected == 1
            numInfected = numInfected - 1;
        elseif entity.recovered = 1
            numRecovered = numRecovered - 1;
        end
    end
end
