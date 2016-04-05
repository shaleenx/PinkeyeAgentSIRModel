function inSalebarn1(entity)
    if entity.inSaleBarn == 1
        if entity.timeInSale > 8
            % move agent to west
        else
            timeInSale = timeInSale + 1;
            % call moveInSaleBarn
        end
    end
end
