drop trigger IF EXISTS calculate_trip_price;
create
    trigger  calculate_trip_price
 before insert on main_trip for each row
    SET NEW . PRICE = (SELECT price FROM main_tripdefinition WHERE main_tripdefinition.id = NEW.trip_definition_id)
    * (100 - (SELECT discount FROM main_client WHERE main_client.id = NEW.client_id)) / 100;
