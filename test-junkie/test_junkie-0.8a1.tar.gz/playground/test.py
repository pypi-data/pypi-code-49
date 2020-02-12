from test_junkie.decorators import Suite, test


class Test:

    def te():

        pass


@Suite(parameters=[str, Test])
class ExampleSuite:

    @test(parameters=[str, Test])
    def archive_product(self, suite_parameter, parameter):
        # print(parameter.__class__)
        pass


if "__main__" == __name__:
    from test_junkie.runner import Runner
    runner = Runner([ExampleSuite], html_report="E:\\Development\\test_junkie\\playground\\report.html")
    runner.run()
