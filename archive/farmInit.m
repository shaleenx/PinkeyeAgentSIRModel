function farmInit(farmNo, farmGrid)
  global INIT_CATTLE_PROBABILITY
  INIT_CATTLE_PROBABILITY = 0.3
  
  calves = [];
  
  for i=1:size(farmGrid, 1)
    for j=1:size(farmGrid, 2)
      if(rand < INIT_CATTLE_PROBABILITY)
        calves = [calves, cattleInit(i, j, 1)];
      end
    end
  end
  
end