WITH RECURSIVE calendar AS (
    SELECT
        daterange('2020-03-01', '2020-04-01') AS left,
        daterange('2020-03-01', '2020-04-01') AS center,
        daterange('2020-03-01', '2020-04-01') AS right
    UNION
    SELECT
        CASE hotel.booking_dates && calendar.left
            WHEN TRUE THEN daterange(lower(calendar.left), lower(hotel.booking_dates * calendar.left))
            ELSE daterange(lower(calendar.right), lower(hotel.booking_dates * calendar.right))
        END AS left,
        CASE hotel.booking_dates && calendar.left
            WHEN TRUE THEN hotel.booking_dates * calendar.left
            ELSE hotel.booking_dates * calendar.right
        END AS center,
        CASE hotel.booking_dates && calendar.right
            WHEN TRUE THEN daterange(upper(hotel.booking_dates * calendar.right), upper(calendar.right))
            ELSE daterange(upper(hotel.booking_dates * calendar.left), upper(calendar.left))
        END AS right
    FROM calendar
    JOIN hotel ON
        hotel.booking_dates && daterange('2020-03-01', '2020-04-01') AND
        hotel.booking_dates <> calendar.center AND (
            hotel.booking_dates && calendar.left OR
            hotel.booking_dates && calendar.right
        )
)
SELECT *
FROM (
SELECT
    a.left AS available_dates
FROM calendar a
LEFT OUTER JOIN calendar b ON
    a.left <> b.left AND
    a.left @> b.left
GROUP BY a.left
HAVING NOT bool_or(COALESCE(a.left @> b.left, FALSE))
UNION
SELECT a.center AS available_dates
FROM calendar a
LEFT OUTER JOIN calendar b ON
    a.center <> b.center AND
    a.center @> b.center
GROUP BY a.center
HAVING NOT bool_or(COALESCE(a.center @> b.center, FALSE))
UNION
SELECT
    a.right AS available_dates
FROM calendar a
LEFT OUTER JOIN calendar b ON
    a.right <> b.right AND
    a.right @> b.right
GROUP BY a.right
HAVING NOT bool_or(COALESCE(a.right @> b.right, FALSE))
) a
WHERE NOT isempty(a.available_dates);