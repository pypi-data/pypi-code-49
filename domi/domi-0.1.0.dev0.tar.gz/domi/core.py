class State:
    __slots__ = ('t_i', 't_e', 'n_i', 'n_e', ...)


class Observation(State):
    _shot_no
    _time


class Node(object):
    _state = None
    _backend = None
    
    @property
    def state(self):
        if self._state is None:
            state = mod.get_state()
            if state is None:
                raise ValueError("No state set. You can set a default")
            else:
                return state
        return self._state

    @state.setter
    def state(self, state):
        if isinstance(state, tuple):
            log.warning("Multiple states given. I will take the union.")
            state = Union(*state)

        self._state = copy(state)
        self._check_state()
        self._input = self._process_state()

    def _check_state(self):
        """
        Here you need to check for the required sub_states in self._state
        necessary for the execution of your code.
        """
        raise NotImplementedError()

    def _process_state(self):
        """
        This function has to be implemented to return a dictionary of the inputs
        for the code to be wrapped

        Returns:
            dict: parameters of the wrapped code
        """
        raise NotImplementedError()

    def __call__(self, state=None):
        """
        Examples:
            >>> vmec = VMEC()
            >>> extender = Extender()
            >>> flt = FLT()
            
            >>> initial_state = Observation(shot_no, time)
            >>> flt(extender(vmec(initial_state)))
            >>> flt.heat_load()

            >>> In1
            Alternatively:
            >>> with Graph() as g:
            ...
            ...     g.add(vmec)
            ...     g.add(extender)
            ...     g.add(flt)
            >>> g.run()

        """
        if state is not None:
            self.state = state

        try:
            backend_method = getattr(self,
                    '_run_{self._backend}'.format(**locals()))
        except:
            raise NotImplementedError("Can not find backend "
                                      "{self._backend}.".format(**locals()))
        self._result = backend_method()
        self._proces_result()
        return self._output_state


    def _process_result(self):
        """
        This takes the result dictionary and build the output_state. Needs to
        set self._output_state
        """
        raise NotImplementedError()

    def __str__(self):
        return str(self._state) + str(self.parameters)


class Union(Node):
    """
    A Union merges multiple states to one state.
    Examples:
        >>> n = Node()
        >>> n.state = (State(), State())
        >>> assert isinstance(n._output_state, State)
    """
    @state.setter
    def state(self, *state):
        self._state = state
        
    def __call__(self, state=None):
        if state is not None:
            self.state = state

        self._output_state = union(self.state)
        return self._output_state


class FLT(Node):
    """
    Examples:

        Default use case
        >>> state = mod.PlasmaState()
        >>> mod.set_state(state)

        >>> flt = mod.FLT()
        >>> flt.heat_load()
        >>> vmec = mod.VMEC()
        >>> vmec.B()

        Special Option for parallel processing and allowing different states
        >>> flt = mod.FLT()
        >>> flt.state = mod.State(...)
        >>> flt.update_state()

        >>> ircam = IRCAM()
        >>> ircam.state = ExperimentalState()
        >>> ircam.output_state
        >>> ircam.update_state()

        >>> overload = OL()
        >>> overload.state = ircam.output_state()
        >>> overload.save?
        >>> overload.state = flt.output_state()
        >>> overload.save?

        >>> stm = STM()
        >>> stm.state_flt = flt.output_state()

    """

    def parameters():
        

    def _process_state():
        raise NotImplementedError()

    def _run_local(self):
        raise NotImplementedError()

    def _run_web(self):
        raise NotImplementedError()
        

    def heat_load(self):
        raise NotImplementedError()


class VMEC(Node):
    def _run_cluster(self):


class IRCAM(Node, :
    @property
    def input(self):

    @input.setter
    def input(self, value):
        if not isinstance(value, )
        self._input = value

    def heat_load():
        pass
