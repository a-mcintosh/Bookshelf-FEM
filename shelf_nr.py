#  ----------------
#  -- helper function
#  -- used in building shelves
#  -- can be moved to /usr/lib/freecad/bin/.
#  ----------------
def get_shelf_nr():
  return shelf_nr_value;

def set_shelf_nr(new_shelf_nr):
  global shelf_nr_value
  shelf_nr_value = new_shelf_nr
  return;


