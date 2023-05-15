SELECT *
  FROM [Netflix].[dbo].[netflix1$]

  -- Checking for Dupes and Nulls (No Dupes, but 24 Title Nulls)
  SELECT show_id, COUNT(*)
  FROM [Netflix].[dbo].[netflix1$]
  GROUP BY show_id;
	
SELECT
COUNT(CASE WHEN show_id IS NULL THEN 1 END) AS showid_nulls,
COUNT(CASE WHEN type IS NULL THEN 1 END) AS type_nulls,
COUNT(CASE WHEN title IS NULL THEN 1 END) AS title_nulls,
COUNT(CASE WHEN director IS NULL THEN 1 END) AS director_nulls,
COUNT(CASE WHEN country IS NULL THEN 1 END) AS country_nulls,
COUNT(CASE WHEN date_added IS NULL THEN 1 END) AS date_addes_nulls,
COUNT(CASE WHEN release_year IS NULL THEN 1 END) AS release_year_nulls,
COUNT(CASE WHEN rating IS NULL THEN 1 END) AS rating_nulls,
COUNT(CASE WHEN duration IS NULL THEN 1 END) AS duration_nulls,
COUNT(CASE WHEN listed_in IS NULL THEN 1 END) AS listed_in_nulls
FROM [Netflix].[dbo].[netflix1$];

SELECT *
FROM [Netflix].[dbo].[netflix1$]
WHERE title IS NULL;

DELETE FROM [Netflix].[dbo].[netflix1$] 
WHERE title IS NULL

--- Relooking at data
SELECT TOP 50 *
FROM [Netflix].[dbo].[netflix1$]


-- Renaming country setting

UPDATE [Netflix].[dbo].[netflix1$]
SET country = 'Unidentified'
WHERE country = 'Not Given';

-- Dropping Director and date_added
ALTER TABLE [Netflix].[dbo].[netflix1$] 
DROP COLUMN Director;

ALTER TABLE [Netflix].[dbo].[netflix1$] 
DROP COLUMN date_added;

ALTER TABLE [Netflix].[dbo].[netflix1$] 
DROP COLUMN duration;

--renaming listed_in to genre
EXEC sp_rename 'Netflix.dbo.netflix1$.listed_in', 'genre', 'COLUMN';

--simplify to only include first genre type
UPDATE [Netflix].[dbo].[netflix1$]
SET genre = LEFT(genre, CHARINDEX(',', genre + ',') - 1)
WHERE CHARINDEX(',', genre) > 0;



SELECT *
FROM [Netflix].[dbo].[netflix1$];
