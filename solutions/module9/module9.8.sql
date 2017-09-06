SELECT path.name, enzyme.sequence
FROM path, enzyme, path_enzyme
WHERE path.id = path_enzyme.path_id AND
      enzyme.id = path_enzyme.enzyme_id
