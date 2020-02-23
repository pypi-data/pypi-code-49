import threading

from opentracing import Scope
from opentracing.scope_managers import ThreadLocalScopeManager


# import tornado.stack_context


# Implementation based on
# github.com/uber-common/opentracing-python-instrumentation/

class TornadoScopeManager(ThreadLocalScopeManager):
    """
    :class:`~opentracing.ScopeManager` implementation for **Tornado**
    that stores the :class:`~opentracing.Scope` using a custom
    :class:`StackContext`, falling back to thread-local storage if
    none was found.

    Using it under :func:`tracer_stack_context()` will
    also automatically propagate the active :class:`~opentracing.Span`
    from parent coroutines to their children:

    .. code-block:: python

        @tornado.gen.coroutine
        def child_coroutine():
            # No need to pass 'parent' and activate it here,
            # as it is automatically propagated.
            with tracer.start_active_span('child') as scope:
                ...

        @tornado.gen.coroutine
        def parent_coroutine():
            with tracer.start_active_span('parent') as scope:
                ...
                yield child_coroutine()
                ...

        with tracer_stack_context():
            loop.add_callback(parent_coroutine)


    .. note::
        The current version does not support :class:`~opentracing.Span`
        activation in children coroutines when the parent yields over
        **multiple** of them, as the context is effectively shared by all,
        and the active :class:`~opentracing.Span` state is messed up:

        .. code-block:: python

            @tornado.gen.coroutine
            def coroutine(input):
                # No span should be activated here.
                # The parent Span will remain active, though.
                with tracer.start_span('child', child_of=tracer.active_span):
                    ...

            @tornado.gen.coroutine
            def handle_request_wrapper():
                res1 = coroutine('A')
                res2 = coroutine('B')

                yield [res1, res2]
    """

    def activate(self, span, finish_on_close):
        """
        Make a :class:`~opentracing.Span` instance active.

        :param span: the :class:`~opentracing.Span` that should become active.
        :param finish_on_close: whether *span* should automatically be
            finished when :meth:`Scope.close()` is called.

        If no :func:`tracer_stack_context()` is detected, thread-local
        storage will be used to store the :class:`~opentracing.Scope`.
        Observe that in this case the active :class:`~opentracing.Span`
        will not be automatically propagated to the child corotuines.

        :return: a :class:`~opentracing.Scope` instance to control the end
            of the active period for the :class:`~opentracing.Span`.
            It is a programming error to neglect to call :meth:`Scope.close()`
            on the returned instance.
        """

        context = self._get_context()
        if context is None:
            return super(TornadoScopeManager, self).activate(span,
                                                             finish_on_close)

        scope = _TornadoScope(self, span, finish_on_close)
        context.active = scope

        return scope

    @property
    def active(self):
        """
        Return the currently active :class:`~opentracing.Scope` which
        can be used to access the currently active
        :attr:`Scope.span`.

        :return: the :class:`~opentracing.Scope` that is active,
            or ``None`` if not available.
        """

        context = self._get_context()
        if not context:
            return super(TornadoScopeManager, self).active

        return context.active

    def _get_context(self):
        return _TracerRequestContextManager.current_context()


class _TornadoScope(Scope):
    def __init__(self, manager, span, finish_on_close):
        super(_TornadoScope, self).__init__(manager, span)
        self._finish_on_close = finish_on_close
        self._to_restore = manager.active

    def close(self):
        context = self.manager._get_context()
        if context is None or context.active is not self:
            return

        context.active = self._to_restore

        if self._finish_on_close:
            self.span.finish()


class _TracerRequestContextManager(object):
    _state = threading.local()
    _state.context = None

    @classmethod
    def current_context(cls):
        return getattr(cls._state, 'context', None)

    def __init__(self, context):
        self._context = context

    def __enter__(self):
        self._prev_context = self.__class__.current_context()
        self.__class__._state.context = self._context
        return self._context

    def __exit__(self, *_):
        self.__class__._state.context = self._prev_context
        self._prev_context = None
        return False
