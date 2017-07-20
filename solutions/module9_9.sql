UPDATE enzyme SET name = 'Cytochrome P450 1A2' WHERE id = 'P05177';
UPDATE enzyme SET name = 'Arylamine N-acetyltransferase 1' WHERE id = 'P18440';
UPDATE enzyme SET name = 'Hypoxanthine-guanine phosphoribosyltransferase' WHERE id = 'P00492';

UPDATE path_enzyme SET position = 1 WHERE enzyme_id = 'P05177' and path_id = 'hsa00232';
UPDATE path_enzyme SET position = 2 WHERE enzyme_id = 'P18440' and path_id = 'hsa00232';
UPDATE path_enzyme SET position = 1 WHERE enzyme_id = 'P18440' and path_id = 'hsa00983';
UPDATE path_enzyme SET position = 2 WHERE enzyme_id = 'P00492' and path_id = 'hsa00983';