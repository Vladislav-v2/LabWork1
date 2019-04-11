--1

SELECT Employe.Sex as 'Стать', Count(*) as 'Кількість'
FROM Employe 
Group by Employe.Sex

--2
SELECT [Department].[Name] AS "Департамент", Count([Department].[Id]) AS "Кількість співробітників" 
FROM [Department] JOIN [Employe] ON [Department].[ID] = [Employe].[DepartmentID]
GROUP BY [Department].[Name]
--3
Select Employe.FName, Employe.LName, Department.Name, Position.Name
From [Department] JOIN [Employe] ON [Department].[ID] = [Employe].[DepartmentID]
join [Position] on Employe.Position=Position.Id

SELECT ctn AS "MAX"
FROM (
		select  count(*) as ctn
		From Employe
		group by Employe.DepartmentId, Employe.Position
	) AS A
	WHERE ctn = (
					SELECT max(ctn)
					FROM (
							select  count(*) as ctn
							From Employe
							group by Employe.DepartmentId, Employe.Position
						)AS B
				)