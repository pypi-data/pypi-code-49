#!/usr/bin/python3

from kivy.uix.label import Label
from kivy.properties import ListProperty, NumericProperty, OptionProperty, BooleanProperty, StringProperty, DictProperty
from kivy.clock import Clock
from kivy.utils import get_hex_from_color

from random import uniform
from functools import partial
from inspect import getmembers

# TODO:
    # Check custom markpoints for changed indicie handelling
    # Fix wrong indicie assignment with indicie_scope='text'


class RefLabel(Label):

    shiftTable = ("lb", "bl", "tr", "rt")
    skipTable = ("bl", "tl", "tr", "br")

    def __init__(self, items=None, set_label=True, **kwargs):
        super().__init__(**kwargs)

        self._refFunctions = {}

        for item in getmembers(self):
            if item[0][:4] == "ref_":
                self._refFunctions[item[0][4:]] = item[1]

        if type(items) == list:
            self.items = items

        self.size = self.texture_size
        self.markup = True
        self.bind(on_ref_press=self.selector)

        self.filler = ' '
        self.spacer = ' '

        self.indPoint = 0
        self.lastInd = 0

        self.counters = []
        self.retainers = []

        self.rows_used = 0
        self.row_center = 0

        self.header_length = 0
        self.footer_length = 0

        self.select_length = 0

        self.reverse = self.orientation[0] == 'b' or self.orientation[3] == 'b'
        self.skip = self._getskipkey() in RefLabel.skipTable
        self.shift = self._getshiftkey() in RefLabel.shiftTable

        if set_label:
            self.init()

    def __str__(self):
        return self.refstrip(self.text)

    def __repr__(self):
        return self.text

    def _getshiftkey(self):
        return self.orientation[1] + self.orientation[4]

    def _getskipkey(self):
        return self.orientation[1] + self.orientation[3]

    def get_circle(self, indicie, count=1, fill=True):
        '''Returns a list containing indicies surrounding the given indicie.

        count   -- Distance from center indicie to include in list
        fill    -- If true, give all indicies. otherwise give outermost cirlce.
        '''

        icheck = []
        fi = indicie
        row = int(indicie / self.cols)
        col = self.cols * row
        diff = indicie - col

        for r in range(row - count, row + count + 1):
            if r >= 0:
                if r <= self.rows - 1:
                    col = self.cols * r
                    indicie = col + diff
                    for i in range(indicie - count, indicie + count + 1):
                        if i >= col:
                            if i <= (col + self.cols) - 1:
                                icheck.append(i)

        if not fill:
            if count > 1:
                for item in self.get_circle(fi, count - 1):
                    icheck.remove(item)
            else:
                icheck.remove(fi)

        return icheck

    def get_line(self, indicie, direction='top', count=0, step=None):
        '''Returns a list of indicies extending in a straight line from the given indicie.

        direction   -- Can be of top, bottom, left, right, or combination for diagonals (top-left, bottom-right)
        count       -- The amount of indicies given. 0 means all possible indicies
        step        -- Return every <step> indicie in the list 
        '''

        line = []

        if count < 0:
            return line

        if '-' in direction:
            slant = []
            i = 0

            y = direction[:direction.find('-')]
            x = direction[direction.find('-') + 1:]

            iy = self.get_line(indicie, y, count, step)
            ix = self.get_line(indicie, x, count, step)

            leny = len(iy)
            lenx = len(ix)

            if leny == 1 or lenx == 1:
                return [indicie]
            elif leny > lenx:
                iy = iy[:lenx]
            elif lenx > leny:
                ix = ix[:leny]

            for item in iy:
                slant.append((item + ix[i]) - indicie)
                i += 1

            return slant

        row = int(indicie / self.cols)
        col = self.cols * row
        if direction == 'top' or direction == 'bottom':
            diff = indicie - col
            rowCount = self.rows - (row + 1)

            if direction == 'bottom':
                line.extend(range(indicie, indicie + ((self.cols * rowCount) + diff) + 1, self.cols))

            elif direction == 'top':
                line.extend(range(diff, indicie + 1, self.cols))
                line.reverse()

        else:
            if direction == 'right':
                line.extend(range(indicie, col + self.cols))
            elif direction == 'left':
                line.extend(range(col, indicie + 1))
                line.reverse()

        if count:
            if len(line) > count:
                line = line[:count]

        if step:
            indicie = 0
            stlist = line[:]
            line.clear()
            while True:
                if indicie >= len(stlist):
                    break
                line.append(stlist[indicie])
                indicie += step



        return line

    def get_cross(self, indicie, method='t', count=0, step=None):
        '''Returns a list of indicies that form a cross outwards from the given indicie.

        method  -- Type of cross. Can be of type 't' or type 'x'
        count   -- The amount of indicies returned outwards from the given indicie
        step    -- Return every <step> indicie within the list
        '''

        cross = []
        if type(count) != tuple:
            if count >= 0:
                count = (count, count)
            else:
                return cross

        if method == 't':
            top = self.get_line(indicie, 'top', count[1], step)
            bottom = self.get_line(indicie, 'bottom', count[1], step)
            left = self.get_line(indicie, 'left', count[0], step)
            right = self.get_line(indicie, 'right', count[0], step)
        elif method == 'x':
            top = self.get_line(indicie, 'top-left', count[1], step)
            bottom = self.get_line(indicie, 'bottom-right', count[1], step)
            left = self.get_line(indicie, 'bottom-left', count[0], step)
            right = self.get_line(indicie, 'top-right', count[0], step)

        top.reverse()
        left.reverse()

        assembly = (top, left, indicie, right, bottom)

        for line in assembly:
            if type(line) == list:
                if indicie in line:
                    line.remove(indicie)
                cross.extend(line)
            else:
                cross.append(line)

        return cross

    def get_items(self, indicies):
        '''Returns a list of items from the item list at the given indicies.'''

        items = []
        for ind in indicies:
            if ind < len(self.items):
                items.append(self.refstrip(self.items[ind]))
            else:
                items.append("O/R")

        return items

    def get_max_length(self):
        '''Returns the amount of characters within the longest line of the grid (by last column of row).'''

        items = self.splicer(self.lastInd, method='single')
        if not items:
            return 0

        i = 0
        ret = 0
        count = 0

        for item in items:
            if i == self.cols:
                if count > ret:
                    ret = count
                    space = i
                count = 0
                i = 0

            count += len(self.refstrip(str(item)))
            i += 1

        if count > ret:
            ret = count
            space = i
        if self.spacer:
            ret += (len(self.spacer) * space) - 1

        return ret

    def spaces(self, count='total'):
        '''Returns the amount of spaces available on the grid.
        
        count -- Scope to be counted. Can be 'remaining', 'used', or 'total'
        '''

        total = self.rows * self.cols

        if count == 'total':
            return total
        else:
            length = len(self.splicer(self.lastInd))
            if count == 'remaining':
                return total - length
            elif count == 'used':
                return total - (total - length)

    def itemfill(self, filler, count=1, method='append'):
        '''Fill the item list with the stated filler.

        count   -- The amount of stated filler to add to the item list

        method  -- The method in which the filler is added:

                    append  - Add the filler to the end of the current list
                    prepend - Add the filler to the beginning of the current list
                    center  - Add the filler to the middle of the current list
                    stitch   - Interweave the filler through each item in the current list
        '''

        fill = []
        fill.extend((filler,) * count)

        if method == 'append':
            self.items.extend(fill)

        elif method == 'prepend':
            fill.extend(self.items)
            self.items = fill[:]

        elif method == 'center':
            ilength = len(self.items)
            cols = int(ilength / self.rows) + (ilength % self.rows != 0)
            skip = (self.cols - cols) + 1

            count = 2
            ind = 0

            while self.items:
                fill.insert(ind, self.items.pop(0))
                if count == cols:
                    count = 1
                    ind += skip
                else:
                    count += 1
                    ind += 1
            self.items = fill[:]

        elif method == 'stitch':
            i = 1
            while fill:
                if i % 2 != 0:
                    self.items.insert(i, fill.pop(0))
                i += 1

    def splicer(self, indPoint=None, lst=None, method='split', bound=True):
        '''Returns a list fitting the parameters of the set RefLabel Properties.

        indPoint    -- Indicie to start splicing the list. Negative indicie results in a reverse sort. If None, then the last used indicie

        lst         -- The list to splice. If None, then self.items

        method      -- If set to split, return items in tuple form with name and indicie. Otherwise just the name is given

        bound       -- If True, return only the amount of items that will fit within the reflabel grid.
        '''

        if not lst:
            if self.items:
                lst = self.items
            else:
                if self.default:
                    lst = ['RefLabel']
                else:
                    return []

        if indPoint == None:
            indPoint = self.indPoint

        if self.reverse:
            if indPoint == 0:
                if self.true_orientation:
                    length = len(lst)
                else:
                    length = self.spaces()
                if length > 1:
                    indPoint = -(length - 1)

        self.lastInd = indPoint
        spaces = self.spaces()

        s_ind = 0
        row_counter = 0
        s_rcount = self.cols - 1
        sk_interval = self.cols * (self.cols - 1)
        sk_length = len(lst) - 1
        point = None


        count = 0
        retList = []

        if not bound:
            spaces = len(self.items) + 1

        for i in range(spaces):
            ind = abs(indPoint)
            if method == 'split':
                if self.indicie_scope == 'items':
                    point = ind
                elif self.indicie_scope == 'text':
                    if abs(s_ind) > self.cols - 1:
                        s_rcount += self.cols
                        s_ind = 0
                        row_counter += 1
                        sk_interval += 2

                    if self.skip:
                        point = row_counter + (abs(s_ind) * self.cols)

                    if self.shift:
                        if point != None:
                            point = -(-(point) + sk_interval) + sk_length
                        else:
                            point = s_ind + s_rcount


                    if not self.skip and not self.shift:
                        point = i

                    s_ind -= 1

                retList.append((lst[ind], point))
                point = None

            else:
                retList.append(lst[ind])

            count += 1
            if self.reverse:
                if indPoint == 0: 
                    break
            else:
                if indPoint == len(lst) - 1:
                    break


            # Leave indPoint at last placed item
            if bound:
                if count != self.spaces():
                    indPoint += 1
            else:
                indPoint += 1

        if self.end_markers:
            if bound:
                up = (indPoint - (count + spaces)) + 3
                down = indPoint - 1

                nxt = None
                prev = None

                if self.reverse:
                    if abs(indPoint) != 0:
                        nxt = "[ref={}]--next--[/ref]".format("mArKeR" + str(down))

                    if abs(indPoint) + count < len(lst) - 1:
                        prev = "[ref={}]--prev--[/ref]".format("mArKeR" + str(up))

                else:
                    if indPoint != len(lst) - 1: 
                        nxt = "[ref={}]--next--[/ref]".format("mArKeR" + str(down))

                    if indPoint - count + 1 != 0:
                        prev = "[ref={}]--prev--[/ref]".format("mArKeR" + str(up)) 

                if prev:
                    retList[0] = prev
                if nxt:
                    retList[-1] = nxt

        return retList

    def referencer(self, items, reference=None):
        ''' Returns a list of referenced ([ref=) items, adding highlighting if necessary.

        items       -- List to be referenced

        reference   -- If False, do not place reference markers within the given items. If None, default to self.references


        **NOTE
        If an item already has a [ref= marker, it is left as it is. If it contains a [ref=None] marker, then all references are removed from the item.
        '''

        if reference == None:
            reference = self.references

        ret = []

        for item in items:
            if type(item) == tuple:
                text = str(item[0])
                item = str((self.refstrip(text), item[1]))
            else:
                text = str(item)
                item = str(item)

            if self.highlight:
                if item in self.selection:
                    text = "[color={}]{}[/color]".format(get_hex_from_color(self.highlight_color), text)
                else:
                    # Custom references
                    if self.isreferenced(text):
                        c = text.find('ref=') + 4
                        if text[c:text.find(']', c)] in self.selection:
                            text = "[color={}]{}[/color]".format(get_hex_from_color(self.highlight_color), text)

            if reference:
                if not self.isreferenced(text):
                    text = "[ref={}]{}[/ref]".format(self.refstrip(item), text)

            if '[ref=None]' in text:
                text = self.refstrip(text, 'ref')

            ret.append(text)

        return ret

    def textcreator(self, items):
        '''Combines a list of items into a string according to the set RefLabel Properties.'''

        def customMark(item, index):
            for pair in self.markPoints:
                if pair[0] == index:
                    if len(pair) != 2:
                        mark = pair[0]
                    else:
                        mark = pair[1]
                    return "[ref={}]{}[/ref]".format("mArKeR" + str(mark), item)
            return item

        def textsetter(rows):
            row = ""
            text = ""
            indicies = range(self.cols)


            i = 0
            for item in rows:

                if '--stop' in item:
                    if self.spacer:
                        row = row[:-(len(self.spacer))]

                    if self.row_center:
                        row = row.center(self.row_center + (len(row) - len(self.refstrip(row))))
                        row = row.rstrip(' ')

                    text += row + '\n'
                    indicies = eval(item[6:])
                    row = ''
                    i = 0
                    continue

                if self.markers:
                    if indicies:
                        item = customMark(item, indicies[i])

                i += 1
                row += item + self.spacer


            if row:
                if self.spacer:
                    row = row[:-(len(self.spacer))]
                if self.row_center:
                    row = row.center(self.row_center + (len(row) - len(self.refstrip(row))))
                    row.rstrip(' ')
                text += row + '\n'

            return text

        def rowsorter(row, indicies):
            self.rows_used += 1
            row.append("--stop{}".format(indicies))

            return row

        
        if len(items) == 0:
            return ''

        nxt = None
        indPoint = 0
        itemCount = 0

        itemInd = []
        rowList = []
        sorted_row = []

        colCount = 0
        rowCount = 1
        self.rows_used = 0

        shift = 0

        length = len(items)

        if self.ismarker(items[0]):
            string = items.pop(0)
            colCount += 1
        else:
            string = ''

        if self.ismarker(items[-1]):
            nxt = items.pop(-1)

        while indPoint != len(items) + 1:
            if colCount == self.cols:

                if self.skip:
                    indPoint -= (self.rows * (self.cols - 1)) - 1

                if self.shift:
                    rowList.reverse()

                sorted_row.extend(rowsorter(rowList, itemInd))
                rowList.clear()
                itemInd.clear()
                

                if rowCount == self.rows:
                    break

                rowCount += 1
                colCount = 0

            rowList.append(items[indPoint])
            itemInd.append(itemCount)
            itemCount += 1


            
            if self.skip:
                if colCount != self.cols - 1:
                    # ^^Overshooting by one row, messing
                    # with the while exit test:
                    indPoint += self.rows
            else:
                indPoint += 1

            if indPoint > len(items) - 1:
                break

            colCount += 1


        if rowList:
            if self.shift:
                rowList.reverse()
            sorted_row.extend(rowsorter(rowList, itemInd))

        string += textsetter(sorted_row)
        if nxt:
            if self.rows_used == self.rows:
                string = string[:-1]
            else:
                self.rows_used = self.rows

            string += nxt + '\n'

        self.row_center = 0

        return string

    def move(self, indicie, count=1, direction='left', bars=[], exc=[], mode='clobber', grouping='single', fill=None, trail=None):
        '''Move the given indicies in the stated direction.
            
            indicie     -- single indicie or list of indicies to be moved

            count       -- amount of spaces to move the indicies

            direction   -- the direction to move the indicies. Can be single (left, bottom) or compound (bottom-left, top-right)

            bars        -- list of barriers that the indicie should not move beyond

            exc         -- exclusion items that will be clobbered if mode is set to short

            mode        -- selects what happens to items at the destination if not self.filler or in exc:
                            clobber -- Overwrite the destination item
                            short   -- move the indicie to in front of the item

            grouping    -- Behaviour of items being moved:
                            single  -- each indicie is treated seperatly
                            shared  -- each indicie effects the movement of the rest of the selection
                            tshared -- for custom trails, indicies not on the trail list do not effect the rest
            
            fill        -- Item to overwrite the starting destination with. Defaults to self.filler

            trail       -- List of custom indicies to move the selection across. Overwrites direction. 
                            **Note: Any indicies not found within the trail given will remain in place.
        '''

        paths = []
        new = []
        gcut = None

        if type(indicie) != list:
            indicie = [indicie]

        for ind in indicie:

            #Get path
            if not trail:
                path = self.get_line(ind, direction, count + 1)

            else: 
                if ind in trail:
                    # Set indicie as first in path
                    place = trail.index(ind)
                    path = trail[place:] + trail[:place]

                    path = path[:count + 1]
                else:

                    if grouping == 'shared':
                        return indicie
                    else:
                        paths.append([ind])
                        continue

            items = self.get_items(path)

            # Barrier detection
            for bar in bars:

                if bar in items:
                    cut = items.index(bar)

                    path = path[:cut]
                    items = items[:cut]

            if mode == 'short': # Move to infront of item
                while items[-1] != self.filler and items[-1] not in exc:
                    if len(items) > 1:
                        del items[-1]

                path = path[:len(items)]

            if grouping == 'shared' or grouping == 'tshared': # Move all the same distance
                length = len(path)
                
                if length == 1: # No movement
                    return indicie

                if gcut == None or gcut > length:
                    gcut = length

            paths.append(path[:])


        for path in paths:
            if gcut:
                path = path[:gcut]

            new.append(path[-1])



        # Copy to new location
        c = 0
        for ind in new:

            self.items[ind] = self.items[indicie[c]]

            if indicie[c] not in new: # Overwrite previous location
                if fill != None:
                    self.items[indicie[c]] = fill
                else:
                    self.items[indicie[c]] = self.filler

            c += 1


        return new

    def isreferenced(self, name):
        '''Returns True if the given string has a [ref] marker.'''
        return "[ref=" in name

    def ismarker(self, name):
        '''Returns True if given string is a place marker.'''
        if type(name) == str:
            if len(name) > 6:
                if "[ref=" in name:
                    return name[5:11] == "mArKeR"
                else:
                    return name[:6] == "mArKeR"
            else:
                return False
        else:
            return False

    def lsmarker(self, name):
        '''Returns the place marker number from the given string.'''

        return int(name[6:])

    def selector(self, touch, name, scope='literal'):
        '''Method used for selecting items within the RefLabel table.

        touch   -- Place holder for when selector is handled by on_touch events

        name    -- The name of the item that is selected

        scope   -- The scope in which the name given applies to:

                    literal - The name is the full ref name passed through on_selection (Used when the item is clicked within the label)

                    items   - The name is an indicie pointing to the location of the item within the self.items list

                    grid    - The name is an indicie pointing to the location of the item within the text grid

                    text    - The name is the text portion of the item
        '''
        if type(name) != list:
            name = [name]

        if scope != 'literal':
            check = []

            if scope == 'text':
                lst = self.splicer(bound=False)
                for item in name:
                    for i in lst:
                        if item == i[0]:
                            check.append(i)

            elif scope == 'items':
                lst = self.splicer(bound=False)
                if self.reverse:
                    lst.reverse()

                for ind in name:
                    if ind < len(lst):
                        check.append(lst[ind])

            elif scope == 'grid':
                lst = self.splicer(indPoint=self.lastInd)
                lst.sort(key=lambda x: x[1])

                for ind in name:
                    if ind < len(lst):
                        check.append(lst[ind])

            check = self.refget(self.referencer(check, reference=True))

        else:
            check = name

        if len(check) == 1:
            if self.ismarker(check[0]):
                indPoint = self.lsmarker(check[0])
            else:
                indPoint = self.lastInd
                if check[0] in self.selection:
                    self.selection.remove(check[0])
                else:
                    if not self.multi:
                        self.selection.clear()

                    self.selection.append(check[0])
        else:
            indPoint = self.lastInd
            for item in check:
                if item in self.selection:
                    self.selection.remove(item)
                else:
                    if not self.multi:
                        self.selection.clear()

                    self.selection.append(item)

        self.init(indicie=indPoint)

    def clearselection(self):
        '''Clears the current selection.'''
        self.selection.clear()
        self.selected.clear()

    def init(self, string=None, indicie=None, append=False, build='all', splice='split'):
        '''Sets the self.text variable with all RefLabel options.

        string      -- If set, sets the given string to self.text, ignoring all options

        indicie     -- Build the text string starting at the given indicie for the self.items list
        
        append      -- If True, replace what is being built, instead of replacing the whole text string

        build       -- What to build into the label, can be items, footer, header, both (header and footer), or all.

        splice      -- Passed on to splice option in self.splicer
        '''
        reset = False
        options = ("all", "both", "header", "footer")
        center_space = self.get_max_length()

        header = ''
        body = ''
        footer = ''
        text = ''

        if self.fill_items:
            remains = self.spaces('remaining')
            if remains > 0:
                self.itemfill(self.filler, remains, self.fill_method)


        if build == 'all' or build == 'items':
            if not string:
                refs = self.referencer(self.splicer(indicie, method=splice))
                if refs:
                    if self.center_items:
                        self.row_center = center_space
                    string = self.textcreator(refs)[:-1]
                else:
                    string = ''
            body = string
            

        if build in options:
            if self.header or self.footer:
                settings = (self.rows, self.references, self.markers, self.end_markers, self.orientation)
                reset = True

                jump = (self.rows - self.rows_used)

                self.rows = 1
                self.references = False
                self.markers = False
                self.end_markers = False
                self.orientation = 'lr-tb'

        if build in options[:2] or build == "header":
            if self.header:
                href = self.referencer(self.splicer(lst=self.header, method=splice))
                if self.center_header:
                    self.row_center = center_space

                header = self.textcreator(href)

        if build in options[:2] or build == "footer":
            if self.footer:
                fref = self.referencer(self.splicer(lst=self.footer, method=splice))
                if self.center_footer:
                    self.row_center = center_space

                fstring = self.textcreator(fref)[:-1]
                footer = "\n" * (jump + 1) + fstring

        if reset:
            self.rows = settings[0]
            self.references = settings[1]
            self.markers = settings[2]
            self.end_markers = settings[3]
            self.orientation = settings[4]

        if append:
            if self.footer_length:
                end = -(self.footer_length)
            else:
                end = None

            if build == 'all' or build == 'items':
                body = self.text[self.header_length:end] + body
            
            if build == "all":
                text = header + body + footer
            elif build == 'items':
                if not end:
                    end = len(self.text)
                text = self.text[:self.header_length] + body + self.text[end:]
            if build == 'both' or build == 'header':
                text = header + self.text[self.header_length:]
            if build == 'both' or build == 'footer':
                text = self.text[:-(self.footer_length)] + footer

        else:
            text = header + body + footer

        self.header_length = len(header)
        self.footer_length = len(footer)
        self.text = text

    def markpoints(self, string, grouping=True, retString=False):
        '''Returns a list containing tupled indicie pairs, locating markup text within the provided string.
        
        string      -- String to check for markup text locations
        
        grouping    -- If set to True, give back-to-back markups with one range

        retString   -- If set to True, prepend the list with the original string
        '''

        c = 0
        indicies = []

        while string.find('[', c) >= 0:
            point = string.find('[', c) 
            c = string.find(']', c) + 1

            if grouping: # Group back to back markups in one segment
                while c != len(string) and string[c] == '[':
                    c = string.find(']', c) + 1

            point = (point, c)

            indicies.append(point)


        if retString:
            return (string, indicies)

        return indicies

    def seglist(self, string, seperator=None, lead_in=True,  *markPoints):
        '''Returns a list of separated characters dictated by either markpoints or seperator.

        string      -- Supplied string to be segmented

        seperator   -- Seperate the string at the given character

        lead-in     -- If set to True, for each sagment that is a markup, include with it the first letter after the markup

        markPoints  -- The points to seperate within the list. Generated by self.markpoints(), or set manually with a list or tuple of tuples
        '''

        ret = []
        if markPoints:
            marker = 0
            for points in markPoints:
                ret.extend(list(string[marker:points[0]]))
                if lead_in:
                    marker = points[1] + 1
                else:
                    marker = points[1]
                ret.append(string[points[0]:marker])
            ret.extend(list(string[marker:len(string)]))
        else:
            ret.extend(list(string))

        if seperator != None:

            seps = []
            string = ''
            for item in ret:
                
                if len(item) > 1:
                    if  item[-1] == seperator:
                        string += item[:-1]
                        sep = True
                    else:
                        sep = False
                else:
                    sep = item == seperator

                if sep:
                    seps.append(string)
                    string = ''

                else:
                    string += item

            seps.append(string)

            return seps

        return ret

    def refstrip(self, string, ref=None):
        '''Returns a string with the stated markup removed.

        string  -- The string to remove markups from

        ref     -- The markup to remove. If None, then all markup is removed
        '''

        if type(string) != list:
            ret = ''
            for c in self.seglist(string, None, False, *self.markpoints(string, grouping=False)):

                if len(c) > 1:
                    if ref:
                        if ref not in c:
                            ret += c
                else:
                    ret += c
        else:
            ret = []
            for item in string:
                st = ''
                for c in self.seglist(item, None, False, *self.markpoints(item, grouping=False)):

                    if len(c) > 1:
                        if ref:
                            if ref not in c:
                                st += c
                    else:
                        st += c
                ret.append(st)

        return ret

    def refget(self, string):
        '''Returns a list of references contained in the given string or list.'''

        ret = []
        if type(string) != list:
            string = [string]

        for item in string:
            i = item.find("[ref=") + 5
            while i >= 5:
                ret.append(item[i:item.find(']', i)])
                i = item.find("[ref=", i) + 5

        return ret

    def shelf(self, *args):
        '''Method to control variables for repeating functions.'''

        if args[0] == 'counter':
            if args[1] not in self.counters:
                if len(args) <= 2:
                    count = 0
                else:
                    count = args[2]
                setattr(self, args[1], count)
                self.counters.append(args[1])
            else:
                return

        elif args[0] == 'retainer':
            if args[1] not in self.retainers:
                if len(args) > 2:
                    item = args[2]
                else:
                    item = None
                setattr(self, args[1], item)
                self.retainers.append(args[1])
            else:
                return

        elif args[0] == 'reset':
            for item in args[1:]:
                delattr(self, item)
                if item in self.counters:
                    self.counters.remove(item)
                if item in self.retainers:
                    self.retainers.remove(item)

        elif args[0] in self.counters:
            if len(args) != 1:
                if type(args[1]) == str:
                    exec('self.{0} = self.{0} {1}'.format(args[0], args[1]))
                else:
                    exec('self.{0} = {1}'.format(args[0], args[1]))
            else:
                return getattr(self, args[0])

        elif args[0] in self.retainers:
            if len(args) != 1:
                setattr(self, args[0], args[1])
            else:
                if hasattr(self, args[0]):
                    return getattr(self, args[0])
                else:
                    self.retainers.remove(args[0])
                    self.shelf(*args)

    def ticker(self, name, count=1, method='add', setter=True, ret=False, tps=1, start=0):
        '''A method that automatically sets an integer over time at the stated intervals.

        name    -- The name of the variable to increment or decrement

        count   -- The amount to increment or decrement the given variable

        method  -- Can be of add (increment) or remove (decrement)

        setter  -- If set to true, run self.init() each time the given variable is incremented

        tps     -- Integer stating the Ticks per Second

        start   -- The integer to start the given variable at
        '''

        if self.shelf("T{}".format(name)) == None:
            self.shelf('retainer', "T{}".format(name), name)
            self.shelf('counter', name, start)
            return Clock.schedule_interval(partial(self.ticker, name, count, method, setter), tps)
        else:
            if method == 'add':
                self.shelf(name, '+{}'.format(count))
            elif method == 'remove':
                self.shelf(name, '-{}'.format(count))

            if setter:
                self.init(indicie=self.lastInd)

    def on_orientation(self, *args):
        '''Changes orientation on the fly when self.orientation is changed.'''

        self.reverse = self.orientation[0] == 'b' or self.orientation[3] == 'b'
        self.skip = self._getskipkey() in RefLabel.skipTable
        self.shift = self._getshiftkey() in RefLabel.shiftTable
        
    def on_selection(self, instance, items):
        '''Sets self.selected according to reflabel options.'''

        if self.refMethod == 'name':
            count = 0
        elif self.refMethod == 'indicie':
            count = 1
        else:
            count = None

        ret = []
        self.selected.clear()

        if count != None:
            for item in items:
                if item[0] == '(':
                    ret.append(eval(item)[count])
                else:
                    ret.append(item)
        else:
            ret.extend(items)

        self.selected = ret

        if self.run_refFunctions:
            if len(items) >= self.select_length:
                if str(ret[-1]) in self._refFunctions:
                    self._refFunctions[str(ret[-1])]()

        self.select_length = len(items)

    def on_selected(self, instance, name):
        pass



    #spacer = StringProperty(" ")
    '''The character used to space out each column.'''

    #filler = StringProperty(" ")
    '''The character used as a filler when fill_items is set to True.''' 


    orientation = OptionProperty("lr-tb", options=["lr-tb", "lr-bt", "rl-tb", "rl-bt", "tb-lr", "tb-rl", "bt-lr", "bt-rl"])
    '''The order in which the items are placed within the grid.'''

    refMethod = OptionProperty("name", options=["name", "indicie"])
    '''When an item in the RefLabel is selected, this determines whether the items name is passed to self.selected, or its indicie within the indicie_scope.'''

    indicie_scope = OptionProperty("items", options=["items", "text"])
    '''If self.refMethod is set to indicie, the indicie given to selected would be based on the scope set. ''' 

    fill_method = OptionProperty("append", options=["append", "prepend", "center", "stitch"])
    '''When fill_items is set to True, determines how to fill the spaces within the item list:

        append  -- Place the filler at the end of the list

        prepend -- Place the filler at the beginning of the list

        center  -- Place the filler in the middle of the list

        stitch  -- Interweave the filler through the list'''


    items = ListProperty([])
    '''The items that are to be set within the reflabel text table.'''

    header = ListProperty([])
    '''A list of text that is not processed, save for constrictions from self.cols. It is placed as a single line above
    the reflabel text table.'''
    
    footer = ListProperty([])
    '''A list of text that is not processed, save for constrictions from self.cols. It is placed as a single line below
    the reflabel text table.'''

    markPoints = ListProperty([])
    '''A list of (location-indicie, <goto-indicie>) tuples for custom marker placement. 

        If goto-indicie is omitted, then the item will be marked with itself.'''

    selection = ListProperty([])
    '''The currently selected item(s) within the text table as (indicie,name) tuples.'''

    selected = ListProperty([])
    '''The currently selected item(s) within the text table as either name or indicie, as dictated by refMethod.'''
    
    highlight_color = ListProperty([0,0,1,1])
    '''The colour of the selected items within the text table when highlight is set to True.'''

    
    default = BooleanProperty(True)
    '''If True, set the default RefLabel item if the item list is empty.'''

    multi = BooleanProperty(False)
    '''If True, allow multiple items to be selected from the text table.'''

    markers = BooleanProperty(True)
    '''If True, allow custom markers from self.markPoints to be assigned within the text table.'''

    end_markers = BooleanProperty(True)
    '''If True, allow --prev-- and --next-- markers at the ends of the text table for when 
    the items list can not fit within the text table.'''

    highlight = BooleanProperty(True)
    '''If True, set the colour of selected items within the text table to highlight_color.'''

    references = BooleanProperty(True)
    '''If True, tag each item in the item list with [ref=] markers if they do not already have them.'''

    center_header = BooleanProperty(False)
    '''If True, center the header text line with the longest line within the text table.'''

    center_footer = BooleanProperty(False)
    '''If True, center the footer text line with the longest line within the text table.'''

    center_items = BooleanProperty(False)
    '''If True, center the text table with the longest line found within the text table.'''

    fill_items = BooleanProperty(False)
    '''If True, pad the text table with filler, according to fill_method.'''

    true_orientation = BooleanProperty(True)
    '''If True, Orient the table according to the items list. Otherwise orient against the current text table.'''

    run_refFunctions = BooleanProperty(True)
    '''If True, execute defined ref_* instance methods when its name is selected from the text table.'''



    rows = NumericProperty(5)
    '''The amount of rows contained within the text table.'''

    cols = NumericProperty(1)
    '''The amount of columns contained within the text table.'''
