drop trigger IF EXISTS update_total_saved;
create
    trigger  update_total_saved
 after insert on main_trip for each row
    UPDATE main_client SET total_saved = total_saved + (SELECT
            price
        FROM
            main_tripdefinition
        WHERE
            id = NEW.trip_definition_id) - NEW.price WHERE id = NEW.client_id;
