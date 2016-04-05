function inFarm(entity)
    if entity.weight < 600
        entity.weight = entity.weight + rand()*0.50 + 0.25;
        if rand() < 0.5
            entity.x = entity.x + 1;
        else
            entity.y = entity.y + 1;
        end
        
    end
end
