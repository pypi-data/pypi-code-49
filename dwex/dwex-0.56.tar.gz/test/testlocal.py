from testall import test_file, test_tree, test_tree_for

#test_file('\\\\sandbox\\seva\\webdata\\clarify\\derived\\An-3.20.0-y-ARMv7\\libyarxi.so')
#test_file('\\\\mac\\seva\\quincy\\4.69.8\\YarxiMin.app.dSYM')
test_tree('\\\\mac\\seva\\quincy')

# Find a file with a ranges under a CU with no low_pc
def nolopc(di):
    for CU in di.iter_CUs():
        if not 'DW_AT_low_pc' in CU.get_top_DIE().attributes:
            for die in CU.iter_DIEs():
                assert 'DW_AT_ranges' not in die.attributes

#test_tree_for('\\\\mac\\seva\\quincy', nolopc)
#test_tree_for("\\\\sandbox\\seva\\webdata\\clarify\\derived", nolopc)