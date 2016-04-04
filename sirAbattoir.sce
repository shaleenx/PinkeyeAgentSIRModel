//Procedure to adjust appropriate system variables when a beef cow is slaughtered

function sirAbattoir(entity)
    global numSusceptible numInfected numRecovered;
    if entity.onAbottoir == 1 then
        if entity.susceptible == 1 then
            numSusceptible = numSusceptible - 1;
        elseif entity.infected == 1 then
            numInfected = numInfected - 1;
        elseif entity.recovered = 1 then
            numRecovered = numRecovered - 1;
        end
    end
endfunction
