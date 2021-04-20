drop trigger IF EXISTS set_today_as_sell_date;

DELIMITER $$

create trigger set_today_as_sell_date before insert on main_trip for each row
IF ( ISNULL(NEW.sell_date) ) THEN
 SET NEW.sell_date=CURDATE();
END IF;
$$

delimiter ;
