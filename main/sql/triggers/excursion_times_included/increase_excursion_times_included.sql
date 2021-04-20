drop trigger IF EXISTS increase_excursion_times_included;

create trigger increase_excursion_times_included
 after insert on main_tripdefinition_excursions for each row
   update main_excursion set times_included = times_included + 1
   where main_excursion.id = NEW.excursion_id;
