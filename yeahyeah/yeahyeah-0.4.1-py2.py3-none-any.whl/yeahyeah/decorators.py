import click

from yeahyeah.context import YeahYeahContext

"""Decorator to pass YeahYeahContext to click function. Example:

    @pass_yeahyeah_context
    def foo(context: YeahYeahContext):
        click.echo(f"Got context {context}")

"""
pass_yeahyeah_context = click.make_pass_decorator(YeahYeahContext)
