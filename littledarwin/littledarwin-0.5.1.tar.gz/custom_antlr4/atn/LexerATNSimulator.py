from __future__ import print_function
#
# [The "BSD license"]
#  Copyright (c) 2012 Terence Parr
#  Copyright (c) 2012 Sam Harwell
#  Copyright (c) 2014 Eric Vergnaud
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#  3. The name of the author may not be used to endorse or promote products
#     derived from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
#  IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
#  OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
#  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#/

# When we hit an accept state in either the DFA or the ATN, we
#  have to notify the character stream to start buffering characters
#  via {@link IntStream#mark} and record the current state. The current sim state
#  includes the current index into the input, the current line,
#  and current character position in that line. Note that the Lexer is
#  tracking the starting line and characterization of the token. These
#  variables track the "state" of the simulator when it hits an accept state.
#
#  <p>We track these variables separately for the DFA and ATN simulation
#  because the DFA simulation often has to fail over to the ATN
#  simulation. If the ATN simulation fails, we need the DFA to fall
#  back to its previously accepted state, if any. If the ATN succeeds,
#  then the ATN does the accept and the DFA simulator that invoked it
#  can simply return the predicted token type.</p>
#/
from builtins import chr
from builtins import str
from builtins import range
from builtins import object
from custom_antlr4 import Lexer
from custom_antlr4.PredictionContext import SingletonPredictionContext, PredictionContext
from custom_antlr4.Token import Token
from custom_antlr4.atn.ATN import ATN
from custom_antlr4.atn.ATNConfig import LexerATNConfig
from custom_antlr4.atn.ATNSimulator import ATNSimulator
from custom_antlr4.atn.ATNConfigSet import ATNConfigSet, OrderedATNConfigSet
from custom_antlr4.atn.ATNState import RuleStopState, ATNState
from custom_antlr4.atn.LexerActionExecutor import LexerActionExecutor
from custom_antlr4.atn.Transition import Transition
from custom_antlr4.dfa.DFAState import DFAState
from custom_antlr4.error.Errors import LexerNoViableAltException, UnsupportedOperationException

class SimState(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self.index = -1
        self.line = 0
        self.column = -1
        self.dfaState = None

class LexerATNSimulator(ATNSimulator):
    
    debug = False
    dfa_debug = False

    MIN_DFA_EDGE = 0
    MAX_DFA_EDGE = 127 # forces unicode to stay in ATN

    ERROR = None

    match_calls = 0

    def __init__(self, recog, atn, decisionToDFA, sharedContextCache):
        super(LexerATNSimulator, self).__init__(atn, sharedContextCache)
        self.decisionToDFA = decisionToDFA
        self.recog = recog
        # The current token's starting index into the character stream.
        #  Shared across DFA to ATN simulation in case the ATN fails and the
        #  DFA did not have a previous accept state. In this case, we use the
        #  ATN-generated exception object.
        self.startIndex = -1
        # line number 1..n within the input#/
        self.line = 1
        # The index of the character relative to the beginning of the line 0..n-1#/
        self.column = 0
        from custom_antlr4.Lexer import Lexer
        self.mode = Lexer.DEFAULT_MODE
        # Used during DFA/ATN exec to record the most recent accept configuration info
        self.prevAccept = SimState()


    def copyState(self, simulator ):
        self.column = simulator.column
        self.line = simulator.line
        self.mode = simulator.mode
        self.startIndex = simulator.startIndex

    def match(self, input , mode):
        self.match_calls += 1
        self.mode = mode
        mark = input.mark()
        try:
            self.startIndex = input.index
            self.prevAccept.reset()
            dfa = self.decisionToDFA[mode]
            if dfa.s0 is None:
                return self.matchATN(input)
            else:
                return self.execATN(input, dfa.s0)
        finally:
            input.release(mark)

    def reset(self):
        self.prevAccept.reset()
        self.startIndex = -1
        self.line = 1
        self.column = 0
        self.mode = Lexer.DEFAULT_MODE

    def matchATN(self, input):
        startState = self.atn.modeToStartState[self.mode]

        if self.debug:
            print("matchATN mode " + str(self.mode) + " start: " + str(startState))

        old_mode = self.mode
        s0_closure = self.computeStartState(input, startState)
        suppressEdge = s0_closure.hasSemanticContext
        s0_closure.hasSemanticContext = False

        next = self.addDFAState(s0_closure)
        if not suppressEdge:
            self.decisionToDFA[self.mode].s0 = next

        predict = self.execATN(input, next)

        if self.debug:
            print("DFA after matchATN: " + str(self.decisionToDFA[old_mode].toLexerString()))

        return predict

    def execATN(self, input, ds0):
        if self.debug:
            print("start state closure=" + str(ds0.configs))

        t = input.LA(1)
        s = ds0 # s is current/from DFA state

        while True: # while more work
            if self.debug:
                print(("execATN loop starting closure: %s\n", s.configs))

            # As we move src->trg, src->trg, we keep track of the previous trg to
            # avoid looking up the DFA state again, which is expensive.
            # If the previous target was already part of the DFA, we might
            # be able to avoid doing a reach operation upon t. If s!=null,
            # it means that semantic predicates didn't prevent us from
            # creating a DFA state. Once we know s!=null, we check to see if
            # the DFA state has an edge already for t. If so, we can just reuse
            # it's configuration set; there's no point in re-computing it.
            # This is kind of like doing DFA simulation within the ATN
            # simulation because DFA simulation is really just a way to avoid
            # computing reach/closure sets. Technically, once we know that
            # we have a previously added DFA state, we could jump over to
            # the DFA simulator. But, that would mean popping back and forth
            # a lot and making things more complicated algorithmically.
            # This optimization makes a lot of sense for loops within DFA.
            # A character will take us back to an existing DFA state
            # that already has lots of edges out of it. e.g., .* in comments.
            # print("Target for:" + str(s) + " and:" + str(t))
            target = self.getExistingTargetState(s, t)
            # print("Existing:" + str(target))
            if target is None:
                target = self.computeTargetState(input, s, t)
                # print("Computed:" + str(target))

            if target == self.ERROR:
                break

            if target.isAcceptState:
                self.captureSimState(self.prevAccept, input, target)
                if t == Token.EOF:
                    break

            if t != Token.EOF:
                self.consume(input)
                t = input.LA(1)

            s = target # flip; current DFA target becomes new src/from state

        return self.failOrAccept(self.prevAccept, input, s.configs, t)

    # Get an existing target state for an edge in the DFA. If the target state
    # for the edge has not yet been computed or is otherwise not available,
    # this method returns {@code null}.
    #
    # @param s The current DFA state
    # @param t The next input symbol
    # @return The existing target DFA state for the given input symbol
    # {@code t}, or {@code null} if the target state for this edge is not
    # already cached
    def getExistingTargetState(self, s, t):
        if s.edges is None or t < self.MIN_DFA_EDGE or t > self.MAX_DFA_EDGE:
            return None

        target = s.edges[t - self.MIN_DFA_EDGE]
        if self.debug and target is not None:
            print("reuse state "+s.stateNumber+ " edge to "+target.stateNumber)

        return target

    # Compute a target state for an edge in the DFA, and attempt to add the
    # computed state and corresponding edge to the DFA.
    #
    # @param input The input stream
    # @param s The current DFA state
    # @param t The next input symbol
    #
    # @return The computed target DFA state for the given input symbol
    # {@code t}. If {@code t} does not lead to a valid DFA state, this method
    # returns {@link #ERROR}.
    def computeTargetState(self, input, s, t):
        reach = OrderedATNConfigSet()

        # if we don't find an existing DFA state
        # Fill reach starting from closure, following t transitions
        self.getReachableConfigSet(input, s.configs, reach, t)

        if len(reach)==0: # we got nowhere on t from s
            if not reach.hasSemanticContext:
                # we got nowhere on t, don't throw out this knowledge; it'd
                # cause a failover from DFA later.
               self. addDFAEdge(s, t, self.ERROR)

            # stop when we can't match any more char
            return self.ERROR

        # Add an edge from s to target DFA found/created for reach
        return self.addDFAEdge(s, t, cfgs=reach)

    def failOrAccept(self, prevAccept , input, reach, t):
        if self.prevAccept.dfaState is not None:
            lexerActionExecutor = prevAccept.dfaState.lexerActionExecutor
            self.accept(input, lexerActionExecutor, self.startIndex, prevAccept.index, prevAccept.line, prevAccept.column)
            return prevAccept.dfaState.prediction
        else:
            # if no accept and EOF is first char, return EOF
            if t==Token.EOF and input.index==self.startIndex:
                return Token.EOF
            raise LexerNoViableAltException(self.recog, input, self.startIndex, reach)

    # Given a starting configuration set, figure out all ATN configurations
    #  we can reach upon input {@code t}. Parameter {@code reach} is a return
    #  parameter.
    def getReachableConfigSet(self, input, closure, reach, t):
        # this is used to skip processing for configs which have a lower priority
        # than a config that already reached an accept state for the same rule
        skipAlt = ATN.INVALID_ALT_NUMBER
        for cfg in closure:
            currentAltReachedAcceptState = ( cfg.alt == skipAlt )
            if currentAltReachedAcceptState and cfg.passedThroughNonGreedyDecision:
                continue

            if self.debug:
                print(("testing %s at %s\n", self.getTokenName(t), cfg.toString(self.recog, True)))

            for trans in cfg.state.transitions:          # for each transition
                target = self.getReachableTarget(trans, t)
                if target is not None:
                    lexerActionExecutor = cfg.lexerActionExecutor
                    if lexerActionExecutor is not None:
                        lexerActionExecutor = lexerActionExecutor.fixOffsetBeforeMatch(input.index - self.startIndex)

                    treatEofAsEpsilon = (t == Token.EOF)
                    config = LexerATNConfig(state=target, lexerActionExecutor=lexerActionExecutor, config=cfg)
                    if self.closure(input, config, reach, currentAltReachedAcceptState, True, treatEofAsEpsilon):
                        # any remaining configs for this alt have a lower priority than
                        # the one that just reached an accept state.
                        skipAlt = cfg.alt

    def accept(self, input, lexerActionExecutor, startIndex, index, line, charPos):
        if self.debug:
            print(("ACTION %s\n", lexerActionExecutor))

        # seek to after last char in token
        input.seek(index)
        self.line = line
        self.column = charPos
        if input.LA(1) != Token.EOF:
            self.consume(input)

        if lexerActionExecutor is not None and self.recog is not None:
            lexerActionExecutor.execute(self.recog, input, startIndex)

    def getReachableTarget(self, trans, t):
        if trans.matches(t, 0, 0xFFFE):
            return trans.target
        else:
            return None

    def computeStartState(self, input, p):
        initialContext = PredictionContext.EMPTY
        configs = OrderedATNConfigSet()
        for i in range(0,len(p.transitions)):
            target = p.transitions[i].target
            c = LexerATNConfig(state=target, alt=i+1, context=initialContext)
            self.closure(input, c, configs, False, False, False)
        return configs

    # Since the alternatives within any lexer decision are ordered by
    # preference, this method stops pursuing the closure as soon as an accept
    # state is reached. After the first accept state is reached by depth-first
    # search from {@code config}, all other (potentially reachable) states for
    # this rule would have a lower priority.
    #
    # @return {@code true} if an accept state is reached, otherwise
    # {@code false}.
    def closure(self, input, config, configs, currentAltReachedAcceptState,
                speculative, treatEofAsEpsilon):
        if self.debug:
            print("closure("+config.toString(self.recog, True)+")")

        if isinstance( config.state, RuleStopState ):
            if self.debug:
                if self.recog is not None:
                    print(("closure at %s rule stop %s\n", self.recog.getRuleNames()[config.state.ruleIndex], config))
                else:
                    print(("closure at rule stop %s\n", config))

            if config.context is None or config.context.hasEmptyPath():
                if config.context is None or config.context.isEmpty():
                    configs.add(config)
                    return True
                else:
                    configs.add(LexerATNConfig(state=config.state, config=config, context=PredictionContext.EMPTY))
                    currentAltReachedAcceptState = True

            if config.context is not None and not config.context.isEmpty():
                for i in range(0,len(config.context)):
                    if config.context.getReturnState(i) != PredictionContext.EMPTY_RETURN_STATE:
                        newContext = config.context.getParent(i) # "pop" return state
                        returnState = self.atn.states[config.context.getReturnState(i)]
                        c = LexerATNConfig(state=returnState, config=config, context=newContext)
                        currentAltReachedAcceptState = self.closure(input, c, configs,
                                    currentAltReachedAcceptState, speculative, treatEofAsEpsilon)

            return currentAltReachedAcceptState

        # optimization
        if not config.state.epsilonOnlyTransitions:
            if not currentAltReachedAcceptState or not config.passedThroughNonGreedyDecision:
                configs.add(config)

        for t in config.state.transitions:
            c = self.getEpsilonTarget(input, config, t, configs, speculative, treatEofAsEpsilon)
            if c is not None:
                currentAltReachedAcceptState = self.closure(input, c, configs, currentAltReachedAcceptState, speculative, treatEofAsEpsilon)

        return currentAltReachedAcceptState

    # side-effect: can alter configs.hasSemanticContext
    def getEpsilonTarget(self, input, config, t, configs, speculative, treatEofAsEpsilon):
        c = None
        if t.serializationType==Transition.RULE:
                newContext = SingletonPredictionContext.create(config.context, t.followState.stateNumber)
                c = LexerATNConfig(state=t.target, config=config, context=newContext)

        elif t.serializationType==Transition.PRECEDENCE:
                raise UnsupportedOperationException("Precedence predicates are not supported in lexers.")

        elif t.serializationType==Transition.PREDICATE:
                #  Track traversing semantic predicates. If we traverse,
                # we cannot add a DFA state for this "reach" computation
                # because the DFA would not test the predicate again in the
                # future. Rather than creating collections of semantic predicates
                # like v3 and testing them on prediction, v4 will test them on the
                # fly all the time using the ATN not the DFA. This is slower but
                # semantically it's not used that often. One of the key elements to
                # this predicate mechanism is not adding DFA states that see
                # predicates immediately afterwards in the ATN. For example,

                # a : ID {p1}? | ID {p2}? ;

                # should create the start state for rule 'a' (to save start state
                # competition), but should not create target of ID state. The
                # collection of ATN states the following ID references includes
                # states reached by traversing predicates. Since this is when we
                # test them, we cannot cash the DFA state target of ID.

                if self.debug:
                    print("EVAL rule "+ str(t.ruleIndex) + ":" + str(t.predIndex))
                configs.hasSemanticContext = True
                if self.evaluatePredicate(input, t.ruleIndex, t.predIndex, speculative):
                    c = LexerATNConfig(state=t.target, config=config)

        elif t.serializationType==Transition.ACTION:
                if config.context is None or config.context.hasEmptyPath():
                    # execute actions anywhere in the start rule for a token.
                    #
                    # TODO: if the entry rule is invoked recursively, some
                    # actions may be executed during the recursive call. The
                    # problem can appear when hasEmptyPath() is true but
                    # isEmpty() is false. In this case, the config needs to be
                    # split into two contexts - one with just the empty path
                    # and another with everything but the empty path.
                    # Unfortunately, the current algorithm does not allow
                    # getEpsilonTarget to return two configurations, so
                    # additional modifications are needed before we can support
                    # the split operation.
                    lexerActionExecutor = LexerActionExecutor.append(config.lexerActionExecutor,
                                    self.atn.lexerActions[t.actionIndex])
                    c = LexerATNConfig(state=t.target, config=config, lexerActionExecutor=lexerActionExecutor)

                else:
                    # ignore actions in referenced rules
                    c = LexerATNConfig(state=t.target, config=config)

        elif t.serializationType==Transition.EPSILON:
            c = LexerATNConfig(state=t.target, config=config)

        elif t.serializationType in [ Transition.ATOM, Transition.RANGE, Transition.SET ]:
            if treatEofAsEpsilon:
                if t.matches(Token.EOF, 0, 0xFFFF):
                    c = LexerATNConfig(state=t.target, config=config)

        return c

    # Evaluate a predicate specified in the lexer.
    #
    # <p>If {@code speculative} is {@code true}, this method was called before
    # {@link #consume} for the matched character. This method should call
    # {@link #consume} before evaluating the predicate to ensure position
    # sensitive values, including {@link Lexer#getText}, {@link Lexer#getLine},
    # and {@link Lexer#getcolumn}, properly reflect the current
    # lexer state. This method should restore {@code input} and the simulator
    # to the original state before returning (i.e. undo the actions made by the
    # call to {@link #consume}.</p>
    #
    # @param input The input stream.
    # @param ruleIndex The rule containing the predicate.
    # @param predIndex The index of the predicate within the rule.
    # @param speculative {@code true} if the current index in {@code input} is
    # one character before the predicate's location.
    #
    # @return {@code true} if the specified predicate evaluates to
    # {@code true}.
    #/
    def evaluatePredicate(self, input, ruleIndex, predIndex, speculative):
        # assume true if no recognizer was provided
        if self.recog is None:
            return True

        if not speculative:
            return self.recog.sempred(None, ruleIndex, predIndex)

        savedcolumn = self.column
        savedLine = self.line
        index = input.index
        marker = input.mark()
        try:
            self.consume(input)
            return self.recog.sempred(None, ruleIndex, predIndex)
        finally:
            self.column = savedcolumn
            self.line = savedLine
            input.seek(index)
            input.release(marker)

    def captureSimState(self, settings, input, dfaState):
        settings.index = input.index
        settings.line = self.line
        settings.column = self.column
        settings.dfaState = dfaState

    def addDFAEdge(self, from_, tk, to=None, cfgs=None):

        if to is None and cfgs is not None:
            # leading to this call, ATNConfigSet.hasSemanticContext is used as a
            # marker indicating dynamic predicate evaluation makes this edge
            # dependent on the specific input sequence, so the static edge in the
            # DFA should be omitted. The target DFAState is still created since
            # execATN has the ability to resynchronize with the DFA state cache
            # following the predicate evaluation step.
            #
            # TJP notes: next time through the DFA, we see a pred again and eval.
            # If that gets us to a previously created (but dangling) DFA
            # state, we can continue in pure DFA mode from there.
            #/
            suppressEdge = cfgs.hasSemanticContext
            cfgs.hasSemanticContext = False

            to = self.addDFAState(cfgs)

            if suppressEdge:
                return to

        # add the edge
        if tk < self.MIN_DFA_EDGE or tk > self.MAX_DFA_EDGE:
            # Only track edges within the DFA bounds
            return to

        if self.debug:
            print("EDGE " + str(from_) + " -> " + str(to) + " upon "+ chr(tk))

        if from_.edges is None:
            #  make room for tokens 1..n and -1 masquerading as index 0
            from_.edges = [ None ] * (self.MAX_DFA_EDGE - self.MIN_DFA_EDGE + 1)

        from_.edges[tk - self.MIN_DFA_EDGE] = to # connect

        return to


    # Add a new DFA state if there isn't one with this set of
    # configurations already. This method also detects the first
    # configuration containing an ATN rule stop state. Later, when
    # traversing the DFA, we will know which rule to accept.
    def addDFAState(self, configs):
        # the lexer evaluates predicates on-the-fly; by this point configs
        # should not contain any configurations with unevaluated predicates.
        assert not configs.hasSemanticContext

        proposed = DFAState(configs=configs)
        firstConfigWithRuleStopState = None
        for c in configs:
            if isinstance(c.state, RuleStopState):
                firstConfigWithRuleStopState = c
                break

        if firstConfigWithRuleStopState is not None:
            proposed.isAcceptState = True
            proposed.lexerActionExecutor = firstConfigWithRuleStopState.lexerActionExecutor
            proposed.prediction = self.atn.ruleToTokenType[firstConfigWithRuleStopState.state.ruleIndex]

        dfa = self.decisionToDFA[self.mode]
        existing = dfa.states.get(proposed, None)
        if existing is not None:
            return existing

        newState = proposed

        newState.stateNumber = len(dfa.states)
        configs.setReadonly(True)
        newState.configs = configs
        dfa.states[newState] = newState
        return newState

    def getDFA(self, mode):
        return self.decisionToDFA[mode]

    # Get the text matched so far for the current token.
    def getText(self, input):
        # index is first lookahead char, don't include.
        return input.getText(self.startIndex, input.index-1)

    def consume(self, input):
        curChar = input.LA(1)
        if curChar==ord('\n'):
            self.line += 1
            self.column = 0
        else:
            self.column += 1
        input.consume()

    def getTokenName(self, t):
        if t==-1:
            return "EOF"
        else:
            return "'" + chr(t) + "'"


