from .animal_requests import (create_animal, delete_animal, get_all_animals,
                              get_single_animal, update_animal,
                              get_animal_by_location, get_animal_by_status)
from .customer_requests import (create_customer, delete_customer,
                                get_all_customers, get_single_customer,
                                update_customer, get_customers_by_email,
                                get_customers_by_name)
from .employee_requests import (create_employee, delete_employee,
                                get_all_employees, get_single_employee,
                                update_employee, get_employee_by_location)
from .location_requests import (create_location, delete_location,
                                get_all_locations, get_single_location,
                                update_location)
