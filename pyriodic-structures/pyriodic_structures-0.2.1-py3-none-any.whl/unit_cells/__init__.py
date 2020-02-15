from ..Structure import Structure

all_structures = {}

all_structures[('cF4-Cu', 225)] = Structure.from_fractional_coordinates(
    [(0, 0, 0), (0, .5, .5), (.5, 0, .5), (.5, .5, 0)],
    [0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0])

all_structures[('cI2-W', 229)] = Structure.from_fractional_coordinates(
    [(0, 0, 0), (.5, .5, .5)],
    [0, 0],
    [1, 1, 1, 0, 0, 0])

all_structures[('cP1-Po', 221)] = Structure.from_fractional_coordinates(
    [(0, 0, 0)],
    [0],
    [1, 1, 1, 0, 0, 0])

def load_standard(db):
    with db.connection as conn:
        for (name, spg), structure in all_structures.items():
            db.insert_unit_cell(name, spg, structure, conn)

            safe_name = name.replace('-', '_')
            globals()[safe_name] = structure
