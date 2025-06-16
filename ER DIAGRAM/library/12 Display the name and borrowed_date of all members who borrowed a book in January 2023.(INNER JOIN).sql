SELECT name, borrowed_date FROM members
INNER JOIN borrowings ON members.member_id = borrowings.member_id
WHERE EXTRACT(MONTH FROM borrowed_date) = 1 AND EXTRACT(YEAR FROM borrowed_date) = 2023;