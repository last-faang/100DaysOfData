SELECT DISTINCT Content.title
FROM TVProgram
LEFT JOIN Content
    USING (content_id)
WHERE SUBSTRING(TVProgram.program_date::TEXT, 1, 7) = '2020-06'
  AND Content.Kids_content = 'Y'
  AND Content.content_type = 'Movies';
