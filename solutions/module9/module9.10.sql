SELECT path.id, path.name
FROM path, enzyme, path_enzyme
WHERE path.id = path_enzyme.path_id AND
      enzyme.id = path_enzyme.enzyme_id AND
      enzyme.sequence LIKE "%EA%"
GROUP BY path_id
HAVING COUNT(enzyme_id) >= 2
