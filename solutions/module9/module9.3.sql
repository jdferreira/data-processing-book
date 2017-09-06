-- Erase the tables in case they already exist in the database
DROP TABLE IF EXISTS path;
DROP TABLE IF EXISTS enzyme;
DROP TABLE IF EXISTS path_enzyme;

-- This table will contain data about the pathways
CREATE TABLE path (
	id VARCHAR(255) PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	class VARCHAR(255) NOT NULL
);

-- This table will contain data about the enzymes
	CREATE TABLE enzyme (
	id VARCHAR(255) PRIMARY KEY,
	sequence TEXT NOT NULL
);

-- This table will associate each pathway with its enzymes
CREATE TABLE path_enzyme (
	path_id VARCHAR(255),
	enzyme_id VARCHAR(255),
	PRIMARY KEY (path_id, enzyme_id),
	FOREIGN KEY (path_id) REFERENCES path (id),
	FOREIGN KEY (enzyme_id) REFERENCES enzyme (id)
);
