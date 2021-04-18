DELIMITER $$

create PROCEDURE RandomTripDefinition()
BEGIN
select * from main_tripdefinition as r1 join
       (select ceil(rand() *
                     (SELECT MAX(id)
                        FROM main_tripdefinition)) as id)
        AS r2
 WHERE r1.id >= r2.id
 ORDER BY r1.id ASC
 LIMIT 1;
END$$

DELIMITER ;
