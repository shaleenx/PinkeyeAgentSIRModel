function cattleScheduler(entity)
    if entity.onFarm == 1 & entity.weight < 600 then
        // call sir
        // call inFarm
    elseif entity.onFarm == 1 then
        // call sir
        // call farm2sale
    elseif entity.weight < 900 & entity.inSaleBarn == 1 then
        // call sir
        // call inSalebarn1
    elseif entity.onStocker == 1 then
        // call sir
        // call inStocker
    elseif entity.weight >= 900 & entity.inSaleBarn == 1 then
        // call sir
        // call inSalebarn2
    elseif entity.onFeedlot == 1 then
        // call sir
        // call inFeedlot
    elseif entity.inAbattoir == 1 then
        // call sirAbattoir
        
        entity.east = 1;
        entity.west = 0;
        
        entity.processed = 1;
        entity.infected = 0;
        entity.susceptible = 0;
        entity.recovered = 0;
    end
endfunction
