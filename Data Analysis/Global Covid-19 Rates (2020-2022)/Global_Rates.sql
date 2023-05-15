select *
From PortofolioProject..['CovidDeaths']
order by 3,4



select location, date, total_cases, new_cases, total_deaths, population
from PortofolioProject..['CovidDeaths']
order by 1,2

-- Looking at total cases vs total deaths
select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
from PortofolioProject..['CovidDeaths']
Where Location like '%states%'
order by 1,2

-- Looking at total cases vs population
select location, date, total_cases, Population, (total_cases/population)*100 as DeathPercentage
from PortofolioProject..['CovidDeaths']
Where Location like '%states%'
order by 1,2

-- Looking at Countires with Highest Infection Rate compared to population
select location, population, max(total_cases) as HighestInfectionCount, max(total_cases/population)*100 as PercentPopulationInfected
from PortofolioProject..['CovidDeaths']
Group by location, population
order by PercentPopulationInfected desc

-- Showing countries with highest death count per population
select location, max(cast(total_deaths as int)) as TotalDeathCount
from PortofolioProject..['CovidDeaths']
where continent is not null
Group by location
order by TotalDeathCount desc

-- by continent
select continent, max(cast(total_deaths as int)) as TotalDeathCount
from PortofolioProject..['CovidDeaths']
where continent is not null
Group by continent
order by TotalDeathCount desc

select continent, max(cast(total_deaths as int)) as TotalDeathCount
from PortofolioProject..['CovidDeaths']
where continent is not null
Group by continent
order by TotalDeathCount desc

--  continents with the highest death count per population

select continent, max(cast(total_deaths as int)) as TotalDeathCount
from PortofolioProject..['CovidDeaths']
where continent is not null
Group by continent
order by TotalDeathCount desc


-- Globalize Numbers

select date, sum(new_cases) as total_cases, sum(cast(new_deaths as int)) as total_deaths, sum(cast(new_deaths as int))/sum(New_cases)*100 as DeathPercentage
from PortofolioProject..['CovidDeaths']
-- Where Location like '%states%'
where continent is not null
Group by date
order by 1,2 

select sum(new_cases) as total_cases, sum(cast(new_deaths as int)) as total_deaths, sum(cast(new_deaths as int))/sum(New_cases)*100 as DeathPercentage
from PortofolioProject..['CovidDeaths']
-- Where Location like '%states%'
where continent is not null
Group by date
order by 1,2 



-- Looking at Total Population vs Vaccinations

Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, sum(convert(bigint,vac.new_vaccinations)) over (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated --(RollingPeopleVaccinated/population)*100
from PortofolioProject..['CovidDeaths'] dea
join PortofolioProject..['CovidVaccination'] vac
on dea.date = vac.date
and dea.location = vac.location
where dea.continent is not null
order by 2,3


with Popvsvac (continent, location, date, population, New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, sum(convert(bigint,vac.new_vaccinations)) over (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated --(RollingPeopleVaccinated/population)*100
from PortofolioProject..['CovidDeaths'] dea
join PortofolioProject..['CovidVaccination'] vac
on dea.date = vac.date
and dea.location = vac.location
where dea.continent is not null
--order by 2,3
)

Select *, (RollingPeopleVaccinated/population)*100
From Popvsvac


--- Temp Table

Drop Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccination numeric,
Rollingpeoplevaccinated numeric
)

insert into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, sum(convert(bigint,vac.new_vaccinations)) over (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated --(RollingPeopleVaccinated/population)*100
from PortofolioProject..['CovidDeaths'] dea
join PortofolioProject..['CovidVaccination'] vac
on dea.date = vac.date
and dea.location = vac.location
where dea.continent is not null
--order by 2,3

Select *, (RollingPeopleVaccinated/population)*100
From #PercentPopulationVaccinated



Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations, sum(convert(bigint,vac.new_vaccinations)) over (Partition by dea.location order by dea.location, dea.date) as RollingPeopleVaccinated --(RollingPeopleVaccinated/population)*100
from PortofolioProject..['CovidDeaths'] dea
join PortofolioProject..['CovidVaccination'] vac
on dea.date = vac.date
and dea.location = vac.location
where dea.continent is not null
--order by 2,3
