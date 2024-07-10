SELECT name AS results
FROM (
    SELECT
        Users.name AS name,
        MovieRating.user_id
    FROM MovieRating
    LEFT JOIN Users
        ON MovieRating.user_id = Users.user_id
    GROUP BY 
        Users.name,
        MovieRating.user_id
    ORDER BY COUNT(*) DESC, Users.name
    LIMIT 1
)
UNION ALL
SELECT name AS results
FROM (
    SELECT
        Movies.title AS name,
        Movies.movie_id
    FROM MovieRating
    LEFT JOIN Movies
        ON MovieRating.movie_id = Movies.movie_id
    WHERE created_at >= '2020-02-01'
      AND created_at < '2020-03-01'
    GROUP BY 
        Movies.movie_id,
        Movies.title
    ORDER BY AVG(MovieRating.rating) DESC, Movies.title
    LIMIT 1
);
