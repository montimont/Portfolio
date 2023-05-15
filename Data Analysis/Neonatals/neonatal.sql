-- Originally, I had considered looking a terrorism attacks, so I cleaned up the null values with 0. However, to better showcase my data viz skills, I focused on just North America values

select [Number of executions (Amnesty International)], ISNULL([Number of executions (Amnesty International)], 0) as 'Number of Executions'
from CommonDeaths..['annual-number-of-deaths-by-caus$']
--where [Number of executions (Amnesty International)] is null

update ['annual-number-of-deaths-by-caus$']
set [Number of executions (Amnesty International)] = ISNULL([Number of executions (Amnesty International)], 0)
from CommonDeaths..['annual-number-of-deaths-by-caus$']
where [Number of executions (Amnesty International)] is null

select [Terrorism (deaths)], ISNULL([Terrorism (deaths)], 0) as 'Deaths from Terrorism'
from CommonDeaths..['annual-number-of-deaths-by-caus$']
--where [Terrorism (deaths)] is null

update ['annual-number-of-deaths-by-caus$']
set [Terrorism (deaths)] = ISNULL([Terrorism (deaths)], 0)
from CommonDeaths..['annual-number-of-deaths-by-caus$']
where [Terrorism (deaths)] is null

select *
from CommonDeaths..['annual-number-of-deaths-by-caus$']
where year = 2019
AND Code like 'USA' OR 
year = 2019 
and Code like 'MEX'
OR 
year = 2019 
and Code like 'CAN'
order by Year

-- North America Neonatal Death
select Entity, year, [Deaths - Neonatal disorders - Sex: Both - Age: All Ages (Number)] 
from CommonDeaths..['annual-number-of-deaths-by-caus$']
where year >= 2007
AND Code like 'USA' OR 
year >= 2007
and Code like 'MEX'
OR 
year >= 2007
and Code like 'CAN'
order by entity, year

select *
from CommonDeaths..['annual-number-of-deaths-by-caus$']
where code = 'USA'
order by year
