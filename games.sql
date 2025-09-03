--First Query. Display Nintendo Games with score>8(Critic_Score or User_Score)
SELECT Name, Platform, Publisher, Developer,Critic_Score,User_Score,NA_Sales FROM GAMES
WHERE Publisher LIKE '%Nintendo%'
--I don't use IS NOT NULL, because in empty cell there is an empty string ''
AND ((Critic_Score <> '' AND Critic_Score>8)
OR (User_Score <> '' AND User_Score>8)
)
--Second Query. Display average score(including Critic and User Score) in each year
SELECT Year,
(ROUND(AVG(Critic_Score),1)+ROUND(AVG(User_Score),1))/2 AS average
FROM Games
WHERE Critic_Score <> '' OR User_Score <> ''
GROUP BY Year;
--Third Query. Display average score(including Critic and User Score) from each publisher in descending order
SELECT Publisher,
(ROUND(AVG(Critic_Score),1)+ROUND(AVG(User_Score),1))/2 AS average
FROM Games
WHERE Critic_Score <> '' OR User_Score <> ''
GROUP BY Publisher
ORDER BY average DESC
