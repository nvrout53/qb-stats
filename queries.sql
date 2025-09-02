select sum(yards_gained)
from browns 
where passer_player_name = 'J.Winston' and season_type = 'REG' and sack = 0.0;


select count(*)
from browns 
where passer_player_name = 'J.Winston' and season_type = 'REG' and pass_touchdown = 1.0;

select max(cast(passing_yards as integer))
from browns
where passer_player_name = 'J.Winston' and season_type = 'REG'