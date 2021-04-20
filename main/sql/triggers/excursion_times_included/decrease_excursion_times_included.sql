drop trigger IF EXISTS decrease_excursion_times_included;

create trigger decrease_excursion_times_included
 after delete on main_tripdefinition_excursions for each row
   update main_excursion set times_included = times_included - 1
   where main_excursion.id = OLD.excursion_id;
