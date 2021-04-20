drop trigger IF EXISTS increase_excursion_times_visited;

create trigger increase_excursion_times_visited
 after insert on main_trip for each row
   update main_excursion set times_visited = times_visited + 1
   where main_excursion.id IN (
     SELECT excursion_id FROM main_tripdefinition_excursions
     WHERE main_tripdefinition_excursions.tripdefinition_id =
       (SELECT id FROM main_tripdefinition WHERE
         id = NEW.trip_definition_id)
   );
